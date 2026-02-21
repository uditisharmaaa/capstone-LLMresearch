#!/usr/bin/env python3
"""
Capstone Research Pipeline
Generates AI-written Connect 4 solutions via OpenRouter for similarity analysis.

Output layout
─────────────
data/
├── raw/
│   ├── gpt4o/
│   │   ├── gen_0001_gpt4o_01.py       ← generated code WITH provenance header
│   │   ├── gen_0001_gpt4o_01.json     ← full metadata sidecar
│   │   └── ...
│   ├── gpt4mini/
│   └── sonnet/
├── metadata.csv                        ← one row per generation (all models)
├── generation_log.txt                  ← one line per generation
└── validation_report.txt               ← written after all generations finish
"""

import csv
import hashlib
import json
import py_compile
import signal
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

# ─── Configuration ────────────────────────────────────────────────────────────

API_KEY = "REDACTED_API_KEY"   # ← paste your key here
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://research-project.local",
    "X-Title": "Capstone Research Pipeline",
}

TOTAL_GENERATIONS   = 100
DELAY_BETWEEN_CALLS = 1.5   # seconds between successful calls
RETRY_DELAY         = 5.0   # seconds before retry on failure
PROGRESS_INTERVAL   = 50    # print summary every N completions

# Model definitions – counts must sum to TOTAL_GENERATIONS
MODELS = [
    {"name": "openai/gpt-4o",               "short": "gpt4o",    "count": 70},
    {"name": "openai/gpt-4o-mini",          "short": "gpt4mini", "count": 20},
    {"name": "anthropic/claude-3.5-sonnet", "short": "sonnet",   "count": 10},
]

# Approximate cost rates per 1 K tokens (input / output)
COST_PER_1K = {
    "openai/gpt-4o":                {"input": 0.0025,  "output": 0.01},
    "openai/gpt-4o-mini":           {"input": 0.00015, "output": 0.0006},
    "anthropic/claude-3.5-sonnet":  {"input": 0.003,   "output": 0.015},
}

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

DATA_DIR       = Path("data")
RAW_DIR        = DATA_DIR / "raw"
METADATA_CSV   = DATA_DIR / "metadata.csv"
LOG_FILE       = DATA_DIR / "generation_log.txt"
VALIDATION_TXT = DATA_DIR / "validation_report.txt"

CSV_FIELDS = [
    "generation_id", "timestamp", "model", "model_short", "style_index",
    "style_text", "full_prompt", "tokens_input", "tokens_output",
    "tokens_total", "cost_usd", "response_length_chars",
    "response_length_lines", "md5_hash", "filename", "filepath",
]

# ─── Runtime state ────────────────────────────────────────────────────────────

stats = {"successful": 0, "failed": 0, "total_cost": 0.0, "total_tokens": 0}
shutdown_requested = False


def handle_sigint(*_):
    global shutdown_requested
    print("\n\n[!] Interrupt received – will save progress and exit after this call.")
    shutdown_requested = True


# ─── Utilities ────────────────────────────────────────────────────────────────

def ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def ensure_dirs():
    for m in MODELS:
        (RAW_DIR / m["short"]).mkdir(parents=True, exist_ok=True)


def init_csv():
    if not METADATA_CSV.exists():
        with open(METADATA_CSV, "w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=CSV_FIELDS).writeheader()


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


def estimate_cost(model_name: str, tok_in: int, tok_out: int) -> float:
    rates = COST_PER_1K.get(model_name, {"input": 0.001, "output": 0.002})
    return (tok_in / 1000) * rates["input"] + (tok_out / 1000) * rates["output"]


def build_provenance_header(meta: dict) -> str:
    """
    Returns a Python comment block that is prepended to every generated file.
    This makes each file self-documenting — provenance survives even if the
    CSV/JSON sidecar is lost.
    """
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
    lines.append("")   # blank line before actual code
    return "\n".join(lines) + "\n"


# ─── Plan builder ─────────────────────────────────────────────────────────────

def build_plan() -> list:
    """
    Returns an ordered list of generation tasks.
    Models are interleaved (round-robin) so failures spread evenly.
    Styles cycle across all tasks.
    """
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
            "id":          i + 1,
            "model_name":  model["name"],
            "model_short": model["short"],
            "style_index": sidx,
            "style_text":  stext,
            "full_prompt": full_prompt,
        })
    return tasks


# ─── API ──────────────────────────────────────────────────────────────────────

def call_api(model_name: str, prompt: str) -> dict:
    payload = {
        "model":       model_name,
        "messages":    [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens":  3000,
    }
    resp = requests.post(API_URL, headers=HEADERS, json=payload, timeout=90)
    resp.raise_for_status()
    return resp.json()


def test_connectivity() -> bool:
    print("Testing API connectivity … ", end="", flush=True)
    payload = {
        "model":       "openai/gpt-4o-mini",
        "messages":    [{"role": "user", "content": "Say hello in one word."}],
        "temperature": 0.7,
        "max_tokens":  20,
    }
    try:
        resp = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
        resp.raise_for_status()
        reply = resp.json()["choices"][0]["message"]["content"].strip()
        print(f"OK — model replied: {reply!r}")
        return True
    except Exception as exc:
        print(f"FAILED\nError: {exc}")
        return False


# ─── Validation ───────────────────────────────────────────────────────────────

def run_validation():
    lines = []
    sep = "=" * 60
    lines += [sep, "VALIDATION REPORT", f"Generated : {ts()}", sep]

    raw_files = sorted(RAW_DIR.rglob("*.py"))
    lines.append(f"\n1. FILE COUNT: {len(raw_files)} .py files across all model subfolders")
    for m in MODELS:
        count = len(list((RAW_DIR / m["short"]).glob("*.py")))
        lines.append(f"   {m['short']:10s}: {count} files")

    # 2. Sidecar JSON check
    json_files = sorted(RAW_DIR.rglob("*.json"))
    lines.append(f"\n2. SIDECAR JSONs: {len(json_files)} (should match file count)")

    # 3. Syntax check
    ok = bad = 0
    syntax_errs = []
    for fp in raw_files:
        try:
            py_compile.compile(str(fp), doraise=True)
            ok += 1
        except py_compile.PyCompileError as e:
            bad += 1
            syntax_errs.append(f"   {fp.name}: {e}")
    lines.append(f"\n3. SYNTAX CHECK: {ok} pass / {bad} fail")
    lines.extend(syntax_errs[:20])

    # 4. Duplicates (hash of code only — strip the provenance header first)
    hashes: dict[str, list] = {}
    for fp in raw_files:
        raw = fp.read_text(encoding="utf-8")
        # Skip the header comment block to compare only the generated code
        code_only = "\n".join(
            ln for ln in raw.splitlines() if not ln.startswith("#")
        ).strip()
        h = hashlib.md5(code_only.encode()).hexdigest()
        hashes.setdefault(h, []).append(fp.name)
    dupes = {h: v for h, v in hashes.items() if len(v) > 1}
    total_dupes = sum(len(v) - 1 for v in dupes.values())
    lines.append(f"\n4. DUPLICATES (code-only MD5): {total_dupes} duplicate(s) in {len(dupes)} group(s)")
    for names in list(dupes.values())[:5]:
        lines.append(f"   {', '.join(names)}")

    # 5. Cost + distribution from CSV
    total_cost = 0.0
    model_dist: dict[str, int] = {}
    style_dist: dict[int, int] = {}
    if METADATA_CSV.exists():
        with open(METADATA_CSV, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                try:
                    total_cost += float(row.get("cost_usd") or 0)
                    m = row.get("model", "unknown")
                    model_dist[m] = model_dist.get(m, 0) + 1
                    si = int(row.get("style_index") or 0)
                    style_dist[si] = style_dist.get(si, 0) + 1
                except ValueError:
                    pass
    lines.append(f"\n5. TOTAL COST: ${total_cost:.4f}")
    lines.append("\n6. DISTRIBUTION BY MODEL:")
    for m, c in sorted(model_dist.items()):
        lines.append(f"   {m}: {c}")
    lines.append("   DISTRIBUTION BY STYLE:")
    for si in sorted(style_dist):
        lines.append(f"   Style {si:02d}: {style_dist[si]}")

    lines.append("\n" + sep)
    report = "\n".join(lines)
    print(report)
    VALIDATION_TXT.write_text(report, encoding="utf-8")
    print(f"\nValidation report saved → {VALIDATION_TXT}")


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    global shutdown_requested
    signal.signal(signal.SIGINT, handle_sigint)

    if not API_KEY or API_KEY == "YOUR_OPENROUTER_API_KEY_HERE":
        print(
            "ERROR: Open pipeline.py and set your OpenRouter API key "
            "in the API_KEY variable near the top of the file."
        )
        sys.exit(1)

    ensure_dirs()

    if not test_connectivity():
        sys.exit(1)

    # Build plan and print summary
    plan = build_plan()
    style_plan_counts: dict[int, int] = {}
    for t in plan:
        style_plan_counts[t["style_index"]] = style_plan_counts.get(t["style_index"], 0) + 1

    avg_in, avg_out = 700, 1800
    est_cost = sum(
        estimate_cost(m["name"], avg_in, avg_out) * m["count"] for m in MODELS
    )
    est_min = (TOTAL_GENERATIONS * (DELAY_BETWEEN_CALLS + 5)) / 60

    print()
    print("=" * 50)
    print("GENERATION PLAN")
    print("=" * 50)
    print(f"Total generations : {TOTAL_GENERATIONS}")
    print("Model breakdown   :")
    for m in MODELS:
        print(f"  {m['name']}: {m['count']}  →  data/raw/{m['short']}/")
    print("Style breakdown   :")
    for si in sorted(style_plan_counts):
        print(f"  Style {si:02d}: {style_plan_counts[si]}")
    print(f"Estimated cost    : ${est_cost:.2f}  (budget: $6.00)")
    print(f"Estimated time    : ~{est_min:.0f} minutes")
    print("Provenance        : header comment + .json sidecar per file")
    print("=" * 50)

    # Resume / fresh-start logic
    init_csv()
    completed = load_completed_ids()
    if completed:
        print(f"\nResuming – skipping {len(completed)} already-completed generation(s).")
        with open(METADATA_CSV, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                try:
                    stats["total_cost"]   += float(row.get("cost_usd") or 0)
                    stats["total_tokens"] += int(row.get("tokens_total") or 0)
                    stats["successful"]   += 1
                except ValueError:
                    pass
    else:
        print("\nStarting generation …")

    # ── Generation loop ───────────────────────────────────────────────────────
    start_time = time.time()
    tasks = [t for t in plan if t["id"] not in completed]

    for task in tasks:
        if shutdown_requested:
            print("\nShutdown requested – progress saved.")
            break

        gid         = task["id"]
        model       = task["model_name"]
        mshort      = task["model_short"]
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
                data    = call_api(model, full_prompt)
                code    = data["choices"][0]["message"]["content"]
                usage   = data.get("usage", {})
                tok_in  = usage.get("prompt_tokens", 0)
                tok_out = usage.get("completion_tokens", 0)
                tok_tot = usage.get("total_tokens", tok_in + tok_out)
                cost    = estimate_cost(model, tok_in, tok_out)
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
                    "cost_usd":              f"{cost:.6f}",
                    "response_length_chars": len(code),
                    "response_length_lines": code.count("\n"),
                    "md5_hash":              md5,
                    "filename":              fname,
                    "filepath":              str(fpath),
                }

                # 1. Write .py with embedded provenance header
                header = build_provenance_header(meta)
                fpath.write_text(header + code, encoding="utf-8")

                # 2. Write .json sidecar (identical fields, machine-readable)
                jpath.write_text(
                    json.dumps(meta, indent=2, ensure_ascii=False),
                    encoding="utf-8",
                )

                # 3. Append to master CSV
                append_csv(meta)

                # 4. Append to log
                append_log(
                    f"[{stamp}] ID={gid:04d} | Model={mshort} | Style={sidx:02d} "
                    f"| Tokens={tok_tot} | Cost=${cost:.4f} | MD5={md5[:8]} | Status=SUCCESS"
                )

                stats["successful"]   += 1
                stats["total_cost"]   += cost
                stats["total_tokens"] += tok_tot
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
        pct   = done / TOTAL_GENERATIONS * 100
        label = "OK  " if success else "FAIL"
        print(
            f"  [{label}] [{done:3d}/{TOTAL_GENERATIONS}] {pct:5.1f}%  "
            f"id={gid:04d}  {mshort}  style={sidx:02d}  "
            f"cost=${stats['total_cost']:.4f}"
        )

        if done % PROGRESS_INTERVAL == 0 and done > 0:
            elapsed  = time.time() - start_time
            rate     = done / elapsed if elapsed > 0 else 1
            remain   = TOTAL_GENERATIONS - done
            avg_tok  = stats["total_tokens"] / done if done else 0
            avg_cost = stats["total_cost"]   / done if done else 0
            print()
            print("=" * 48)
            print(f"PROGRESS: {done}/{TOTAL_GENERATIONS} ({pct:.1f}%)")
            print(f"Successful: {stats['successful']} | Failed: {stats['failed']}")
            print(f"Total cost so far: ${stats['total_cost']:.4f}")
            print(f"Avg tokens per generation: {avg_tok:.0f}")
            print(f"Estimated remaining cost: ${avg_cost * remain:.2f}")
            print(f"Estimated time remaining: {remain / rate / 60:.0f} minutes")
            print("=" * 48)
            print()

        if not shutdown_requested:
            time.sleep(DELAY_BETWEEN_CALLS)

    # ── Final summary ─────────────────────────────────────────────────────────
    print()
    print("=" * 50)
    print("GENERATION COMPLETE")
    print(f"  Successful : {stats['successful']}")
    print(f"  Failed     : {stats['failed']}")
    print(f"  Total cost : ${stats['total_cost']:.4f}")
    print("=" * 50)

    print("\nRunning post-generation validation …\n")
    run_validation()


if __name__ == "__main__":
    main()
