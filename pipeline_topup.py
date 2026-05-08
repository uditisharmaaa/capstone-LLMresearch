#!/usr/bin/env python3
"""
Top-up pipeline — brings o4mini, sonnet46, opus46, opus to 70 files each.

o4mini / sonnet46 / opus46  →  NYU Portkey AI Gateway
opus                        →  OpenRouter

Run from the project root:
    python pipeline_topup.py
"""

import concurrent.futures
import csv
import hashlib
import json
import os
import signal
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv
from portkey_ai import Portkey

load_dotenv()

# ─── Keys / endpoints ─────────────────────────────────────────────────────────

PORTKEY_API_KEY  = os.getenv("PORTKEY_API_KEY", "")
OPENROUTER_KEY   = os.getenv("OPENROUTER_API_KEY", "")
PORTKEY_BASE_URL = "https://ai-gateway.apps.cloud.rt.nyu.edu/v1"
OPENROUTER_URL   = "https://openrouter.ai/api/v1/chat/completions"

# ─── Generation plan ──────────────────────────────────────────────────────────

# Current counts: o4mini=29, sonnet46=28, opus46=28, opus=15  →  target 70 each
MODELS = [
    {"name": "@gpt-4o/o4-mini",                      "short": "o4mini",   "count": 41, "api": "portkey"},
    {"name": "@vertexai/anthropic.claude-sonnet-4-6", "short": "sonnet46", "count": 42, "api": "portkey"},
    {"name": "@vertexai/anthropic.claude-opus-4-6",   "short": "opus46",   "count": 42, "api": "portkey"},
    {"name": "anthropic/claude-opus-4.5",             "short": "opus",     "count": 55, "api": "openrouter"},
]

TOTAL_GENERATIONS   = sum(m["count"] for m in MODELS)  # 180
START_ID            = 428
DELAY_BETWEEN_CALLS = 1.5
RETRY_DELAY         = 5.0
PROGRESS_INTERVAL   = 25
REQUEST_TIMEOUT     = 120

STYLES = [
    ( 1, "Write in a simple, beginner-friendly style with clear variable names."),
    ( 2, "Write in a compact style, minimizing lines of code."),
    ( 3, "Write with detailed inline comments explaining every section."),
    ( 4, "Write in a professional style following PEP 8 conventions strictly."),
    ( 5, "Write with descriptive function names and minimal comments."),
    ( 6, "Write as concisely as possible, avoiding any redundancy."),
    ( 7, "Write in a teaching style, as if explaining to someone learning Python."),
    ( 8, "Write with a focus on code readability over brevity."),
    ( 9, "Write using only basic Python features a first-year student would know."),
    (10, "Write with a modular structure, breaking everything into small functions."),
    (11, "Write with extensive docstrings for every function."),
    (12, "Write in a functional style, avoiding global variables where possible."),
    (13, "Write prioritizing correctness and clarity over elegance."),
    (14, "Write with minimal whitespace and short variable names."),
    (15, "Write in a straightforward, no-frills style."),
]

BASE_PROMPT = (
    'You are a first-year computer science student completing a programming '
    'assignment. Write a complete Python3 implementation of the Connect 4 game '
    'with the following requirements:\n\n'
    '1. Create a 2D board with 7 columns and 6 rows, initialized with spaces\n'
    '2. Support exactly 2 players using checkers "X" and "O"\n'
    '3. Use constant global variables for board dimensions and number of players\n'
    '4. Randomly select which player goes first at the start\n'
    '5. Print the board with column labels A through G before the game starts '
    'and after each turn\n'
    "6. Clear the screen before printing using os.system('clear')\n"
    '7. Players input an uppercase letter (A-G) to choose a column\n'
    '8. Validate all input: reject letters outside A-G, reject full columns, '
    'reject non-letter input - do NOT end the turn on invalid input, ask again\n'
    '9. Drop the checker to the lowest available row in the chosen column\n'
    '10. After each move, check for a win: 4 in a row horizontally, '
    'vertically, or diagonally\n'
    '11. If the board fills with no winner, declare a draw\n'
    '12. When a player wins, print "[Player] won!" and end the game\n\n'
    'The board must look exactly like this format:\n'
    '   A   B   C   D   E   F   G\n'
    '+---+---+---+---+---+---+---+\n'
    '|   |   |   |   |   |   |   |\n'
    '+---+---+---+---+---+---+---+\n'
    '|   |   |   |   |   |   |   |\n'
    '+---+---+---+---+---+---+---+\n\n'
    'Provide ONLY the complete Python code. No explanations, no markdown '
    'code blocks, just raw Python code starting with import statements.'
)

# ─── Paths ────────────────────────────────────────────────────────────────────

DATA_DIR     = Path("data")
RAW_DIR      = DATA_DIR / "raw"
METADATA_CSV = DATA_DIR / "metadata.csv"
LOG_FILE     = DATA_DIR / "generation_log.txt"

CSV_FIELDS = [
    "generation_id", "timestamp", "model", "model_short", "style_index",
    "style_text", "full_prompt", "tokens_input", "tokens_output",
    "tokens_total", "cost_usd", "response_length_chars",
    "response_length_lines", "md5_hash", "filename", "filepath",
]

# ─── Runtime state ────────────────────────────────────────────────────────────

stats = {"successful": 0, "failed": 0}
shutdown_requested = False


def handle_sigint(*_):
    global shutdown_requested
    print("\n\n[!] Interrupt received – saving progress and exiting after this call.")
    shutdown_requested = True


# ─── Utilities ────────────────────────────────────────────────────────────────

def ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def ensure_dirs():
    for m in MODELS:
        (RAW_DIR / m["short"]).mkdir(parents=True, exist_ok=True)


def append_csv(row: dict):
    with open(METADATA_CSV, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=CSV_FIELDS).writerow(row)


def append_log(line: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def load_completed_ids() -> set:
    if not METADATA_CSV.exists():
        return set()
    completed = set()
    with open(METADATA_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                completed.add(int(row["generation_id"]))
            except (ValueError, KeyError):
                pass
    return completed


def build_provenance_header(meta: dict) -> str:
    lines = [
        "# " + "=" * 68,
        "# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD",
        "# " + "=" * 68,
        f"# generation_id  : {meta['generation_id']}",
        f"# filename        : {meta['filename']}",
        f"# timestamp       : {meta['timestamp']}",
        f"# model           : {meta['model']}",
        f"# model_short     : {meta['model_short']}",
        f"# style_index     : {meta['style_index']}",
        f"# style_text      : {meta['style_text']}",
        f"# tokens_input    : {meta['tokens_input']}",
        f"# tokens_output   : {meta['tokens_output']}",
        f"# tokens_total    : {meta['tokens_total']}",
        f"# cost_usd        : {meta['cost_usd']}",
        "# " + "-" * 68,
        "# full_prompt:",
    ]
    for prompt_line in meta["full_prompt"].splitlines():
        lines.append(f"#   {prompt_line}")
    lines.append("# " + "=" * 68)
    lines.append("")
    return "\n".join(lines) + "\n"


# ─── Plan builder ─────────────────────────────────────────────────────────────

def build_plan() -> list:
    queues = [[m] * m["count"] for m in MODELS]
    flat = []
    while any(queues):
        for q in queues:
            if q:
                flat.append(q.pop(0))

    tasks = []
    for i, model in enumerate(flat):
        sidx, stext = STYLES[i % len(STYLES)]
        full_prompt = BASE_PROMPT + "\n\n" + stext
        tasks.append({
            "id":          START_ID + i,
            "model_name":  model["name"],
            "model_short": model["short"],
            "api":         model["api"],
            "style_index": sidx,
            "style_text":  stext,
            "full_prompt": full_prompt,
        })
    return tasks


# ─── API calls ────────────────────────────────────────────────────────────────

def call_portkey(client: Portkey, model_name: str, prompt: str) -> dict:
    def _call():
        return client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=3000,
        )

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as ex:
        future = ex.submit(_call)
        try:
            resp = future.result(timeout=REQUEST_TIMEOUT)
        except concurrent.futures.TimeoutError:
            raise TimeoutError(f"Portkey call timed out after {REQUEST_TIMEOUT}s")

    usage = resp.usage
    return {
        "code":    resp.choices[0].message.content,
        "tok_in":  usage.prompt_tokens if usage else 0,
        "tok_out": usage.completion_tokens if usage else 0,
        "tok_tot": usage.total_tokens if usage else 0,
        "cost":    "0.000000",
    }


def call_openrouter(model_name: str, prompt: str) -> dict:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://research-project.local",
        "X-Title": "Capstone Research Pipeline",
    }
    payload = {
        "model":       model_name,
        "messages":    [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens":  3000,
    }
    resp = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=90)
    resp.raise_for_status()
    data    = resp.json()
    usage   = data.get("usage", {})
    tok_in  = usage.get("prompt_tokens", 0)
    tok_out = usage.get("completion_tokens", 0)
    tok_tot = usage.get("total_tokens", tok_in + tok_out)
    # rough cost estimate for claude-opus-4.5
    cost    = (tok_in / 1000) * 0.015 + (tok_out / 1000) * 0.075
    return {
        "code":    data["choices"][0]["message"]["content"],
        "tok_in":  tok_in,
        "tok_out": tok_out,
        "tok_tot": tok_tot,
        "cost":    f"{cost:.6f}",
    }


# ─── Connectivity checks ──────────────────────────────────────────────────────

def check_portkey(client: Portkey) -> bool:
    print("Testing Portkey ... ", end="", flush=True)
    try:
        resp = client.chat.completions.create(
            model="@gpt-4o/o4-mini",
            messages=[{"role": "user", "content": "Say hello in one word."}],
            max_tokens=50,
        )
        print(f"OK — {resp.choices[0].message.content.strip()!r}")
        return True
    except Exception as exc:
        print(f"FAILED: {exc}")
        return False


def check_openrouter() -> bool:
    print("Testing OpenRouter ... ", end="", flush=True)
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "model":    "openai/gpt-4o-mini",
            "messages": [{"role": "user", "content": "Say hello in one word."}],
            "max_tokens": 10,
        }
        resp = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=(10, 20))
        resp.raise_for_status()
        reply = resp.json()["choices"][0]["message"]["content"].strip()
        print(f"OK — {reply!r}")
        return True
    except Exception as exc:
        print(f"FAILED: {exc}")
        return False


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    global shutdown_requested
    signal.signal(signal.SIGINT, handle_sigint)

    if not PORTKEY_API_KEY:
        print("ERROR: PORTKEY_API_KEY not set in .env")
        sys.exit(1)
    if not OPENROUTER_KEY:
        print("ERROR: OPENROUTER_API_KEY not set in .env")
        sys.exit(1)

    ensure_dirs()

    portkey_client = Portkey(
        base_url=PORTKEY_BASE_URL,
        api_key=PORTKEY_API_KEY,
        timeout=90,
    )

    if not check_portkey(portkey_client):
        sys.exit(1)
    print("OpenRouter: skipping connectivity check, key present.")

    plan = build_plan()
    completed = load_completed_ids()
    tasks = [t for t in plan if t["id"] not in completed]

    print()
    print("=" * 52)
    print("TOP-UP GENERATION PLAN")
    print("=" * 52)
    for m in MODELS:
        print(f"  {m['short']:10s}  {m['count']:3d} files  [{m['api']}]")
    print(f"  {'TOTAL':10s}  {TOTAL_GENERATIONS:3d} files")
    print(f"  IDs: {START_ID} – {START_ID + TOTAL_GENERATIONS - 1}")
    print(f"  Skipping {len(completed) & len({t['id'] for t in plan})} already done")
    est_min = (len(tasks) * (DELAY_BETWEEN_CALLS + 6)) / 60
    print(f"  Estimated time: ~{est_min:.0f} minutes")
    print("=" * 52)
    print(f"\nStarting {len(tasks)} generation(s)...\n")

    start_time = time.time()

    for task in tasks:
        if shutdown_requested:
            print("\nShutdown requested – progress saved.")
            break

        gid         = task["id"]
        model       = task["model_name"]
        mshort      = task["model_short"]
        api         = task["api"]
        sidx        = task["style_index"]
        stext       = task["style_text"]
        full_prompt = task["full_prompt"]
        stem        = f"gen_{gid:04d}_{mshort}_{sidx:02d}"
        fname       = stem + ".py"
        fpath       = RAW_DIR / mshort / fname
        jpath       = RAW_DIR / mshort / (stem + ".json")

        success = False
        for attempt in range(2):
            try:
                if api == "portkey":
                    result = call_portkey(portkey_client, model, full_prompt)
                else:
                    result = call_openrouter(model, full_prompt)

                code    = result["code"]
                tok_in  = result["tok_in"]
                tok_out = result["tok_out"]
                tok_tot = result["tok_tot"]
                cost    = result["cost"]
                md5     = hashlib.md5(code.encode()).hexdigest()
                stamp   = ts()

                meta = {
                    "generation_id":         gid,
                    "timestamp":             stamp,
                    "model":                 model,
                    "model_short":           mshort,
                    "style_index":           sidx,
                    "style_text":            stext,
                    "full_prompt":           full_prompt,
                    "tokens_input":          tok_in,
                    "tokens_output":         tok_out,
                    "tokens_total":          tok_tot,
                    "cost_usd":              cost,
                    "response_length_chars": len(code),
                    "response_length_lines": code.count("\n"),
                    "md5_hash":              md5,
                    "filename":              fname,
                    "filepath":              str(fpath),
                }

                fpath.write_text(build_provenance_header(meta) + code, encoding="utf-8")
                jpath.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
                append_csv(meta)
                append_log(
                    f"[{stamp}] ID={gid:04d} | Model={mshort} | Style={sidx:02d} "
                    f"| Tokens={tok_tot} | MD5={md5[:8]} | Status=SUCCESS"
                )

                stats["successful"] += 1
                success = True
                break

            except Exception as exc:
                append_log(
                    f"[{ts()}] ID={gid:04d} | Model={mshort} | Style={sidx:02d} "
                    f"| Status=FAILED | Reason={exc}"
                )
                if attempt == 0:
                    print(f"  [attempt 1 failed, retrying in {RETRY_DELAY}s] {exc}")
                    time.sleep(RETRY_DELAY)

        if not success:
            stats["failed"] += 1

        done  = stats["successful"] + stats["failed"]
        label = "OK  " if success else "FAIL"
        print(
            f"  [{label}] [{done:3d}/{TOTAL_GENERATIONS}]  "
            f"id={gid:04d}  {mshort}  style={sidx:02d}"
        )

        if done % PROGRESS_INTERVAL == 0 and done > 0:
            elapsed = time.time() - start_time
            rate    = done / elapsed if elapsed > 0 else 1
            remain  = TOTAL_GENERATIONS - done
            print()
            print(f"  Progress: {done}/{TOTAL_GENERATIONS} | "
                  f"ETA: {remain / rate / 60:.0f} min")
            print()

        if not shutdown_requested:
            time.sleep(DELAY_BETWEEN_CALLS)

    print()
    print("=" * 52)
    print("TOP-UP COMPLETE")
    print(f"  Successful : {stats['successful']}")
    print(f"  Failed     : {stats['failed']}")
    print("=" * 52)
    print()
    print("File counts after top-up:")
    for m in MODELS:
        count = len(list((RAW_DIR / m["short"]).glob("*.py")))
        print(f"  {m['short']:10s}: {count} files")


if __name__ == "__main__":
    main()
