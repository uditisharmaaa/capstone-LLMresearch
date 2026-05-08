# CLAUDE.md

---

## Project

Uditi's senior capstone — a **scientific paper** on detecting AI-generated code in intro CS assignments (Connect4, Tic-Tac-Toe, Hangman). The deliverable is a publishable research contribution, not just a working tool.

The system compares submissions against known human and AI baselines to produce probability scores. Scope is intentionally narrow: only works for assignments where pre-ChatGPT human submissions exist as a reference.

---

## How to Work on This Project

### Scientific rigor
- Before stating a claim, argue against it internally. If it doesn't hold up, say so.
- Verify that statistical claims are correct (correct test, correct assumptions, not overstated).
- Don't dress up weak results. If something is inconclusive, say it's inconclusive.
- Compare against prior work honestly — our advantage over Hoq & Leinonen is multi-model coverage, not that we're universally better.

### Literature and research
- All confirmed papers live in `research/papers.md`. Read it before any literature discussion.
- Confirmed papers are in `research/papers.md` (9 papers). Always read that file before any literature discussion and verify any new citations via web search before adding them.
- Never cite or describe a paper from memory alone — hallucinated citations are a serious research integrity failure. Always verify title, authors, venue, year, and core claims via web search before referencing.
- Search proactively: AI code detection, authorship attribution, code stylometry, plagiarism detection, LLM output detection, CS education and academic integrity. Don't wait to be asked.
- Use `/find-papers` to run a structured search and add verified papers to `research/papers.md`.

### Code quality
- No bloated code. No abstractions that aren't earned. Three similar lines beats a premature abstraction.
- No unnecessary comments. Code should be readable by its structure and naming.
- No error handling for things that can't happen. No fallbacks for internal logic.
- Before adding anything, check if it conflicts with or duplicates what's already in the codebase.
- Follow PEP 8. Keep functions small and focused.

### Communication
- No sycophancy. Don't validate bad ideas. Push back when something is wrong or weak.
- Explain ML/stats concepts simply — intuition first, then mechanics.
- Don't summarize what was just done. Be terse.

### CLAUDE.md
- Update this file automatically whenever the project state changes (new data, new phases complete, new findings, new files).

---

## Role

Help across all dimensions:
- **Research** — suggest experiments, identify weak points in methodology, find novel angles
- **Concepts** — explain ML, stats, NLP at a beginner level when needed
- **Coding** — implement cleanly and correctly; check the codebase before writing anything new
- **Paper** — structure arguments, write clearly, hold a high bar (not AI slop)

---

## Paper Direction

Two research questions — both will be in the final paper:

**RQ1 (answerable now): Multi-model fingerprinting** — Do different AI models leave statistically distinguishable stylistic fingerprints in CS1 assignments? Analysis complete on 423 samples across 9 models. This is the novel primary contribution — no prior paper does multi-model fingerprinting at this scale on assignment-specific code.

**RQ2 (pending human data): AI vs. Human detection** — Can those fingerprints reliably distinguish AI-generated code from pre-ChatGPT student submissions? Requires professor's pre-2022 Connect4 submissions. Once that arrives: Random Forest / XGBoost classifier with probability scores (not binary labels).

The paper covers both. RQ1 is the methodological foundation; RQ2 is the applied payoff.

---

## Data ✅

**AI-generated Connect4 solutions in `data/raw/`:**

| Model | Era | Count | Directory | Notes |
|-------|-----|-------|-----------|-------|
| GPT-4o | 2024 | 70 | `gpt4o/` | |
| GPT-4o Mini | 2024 | 50 | `gpt4mini/` | |
| Claude Sonnet 3.5 | 2024 | 50 | `sonnet/` | |
| Gemini 2.0 Flash | 2024 | 50 | `gemini/` | |
| Llama 3.1 70B | 2024 | 50 | `llama/` | |
| Claude Opus 4.5 | 2025 | 28 | `opus/` | via OpenRouter |
| o4-mini | 2025 | 43 | `o4mini/` | via NYU Portkey |
| Claude Sonnet 4.6 | 2025 | 41 | `sonnet46/` | via NYU Portkey |
| Claude Opus 4.6 | 2025 | 41 | `opus46/` | via NYU Portkey |
| Gemini 2.5 Flash | 2025 | 29 | `gemini25f/` | EXCLUDED — truncated (~20 lines); thinking tokens exhausted budget |
| Gemini 2.5 Pro | 2025 | 28 | `gemini25p/` | EXCLUDED — same issue |

**Total valid for analysis: 423 files across 9 models.** 15 style variations per model. Metadata in `data/metadata.csv`. Generated via OpenRouter (Phase 1–2) and NYU Portkey AI Gateway (Phase 3–4).

**Fix for Gemini 2.5 regeneration (next semester):** Use `max_tokens=10000+` to leave budget for code after thinking tokens.

---

## Phases

| Phase | Status | Notes |
|-------|--------|-------|
| 1 — Data collection (original) | ✅ | 285 files, 6 models, via OpenRouter |
| 2 — Feature extraction | ✅ | Lexical (553), structural (120), TF-IDF in `src/features/` |
| 3 — Similarity analysis | ✅ | 423-sample run. Pairwise TF-IDF + edit distance, Mann-Whitney U, Cohen's d. Results in `results/` |
| 3b — Phase 3 data (2025 models) | ✅ | 153 new files (o4mini ×43, sonnet46 ×41, opus46 ×41, opus ×28) via NYU Portkey + OpenRouter |
| 4 — Human data | ⏳ | Pre-2022 Connect4 submissions in hand from professor; integration planned Fall 2026 |
| 5 — Multi-model classifier | 🔜 | Random Forest / XGBoost on 423 samples — Fall 2026 |
| 6 — AI vs Human classifier | 🔜 | Requires Phase 4 human data; probability scores not binary labels — Fall 2026 |
| 7 — Abstract / proposal | ✅ | Submitted. Revised with threats to validity, RQ2 methodology, cross-generation analysis, sample size caveats. `docs/proposal.tex` |
| 8 — Full scientific paper | 🔜 | Fall 2026 |

---

## Key Findings (423-sample TF-IDF analysis, May 2026)

**Dataset:** 423 Connect4 Python files across 9 models (Gemini 2.5 Flash/Pro excluded — thinking token budget consumed output; generated ~20-line truncated files).

**Within-model TF-IDF similarity (mean ± std):**
| Model | Era | N | Mean | Std |
|-------|-----|---|------|-----|
| GPT-4o Mini | 2024 | 50 | 0.833 | 0.071 |
| Claude Sonnet 3.5 | 2024 | 50 | 0.819 | 0.062 |
| Claude Opus 4.5 | 2025 | 28 | 0.804 | 0.148 |
| o4-mini | 2025 | 43 | 0.800 | 0.073 |
| GPT-4o | 2024 | 70 | 0.800 | 0.106 |
| Claude Opus 4.6 | 2025 | 41 | 0.793 | 0.109 |
| Gemini 2.0 Flash | 2024 | 50 | 0.780 | 0.118 |
| Llama 3.1 70B | 2024 | 50 | 0.772 | 0.113 |
| Claude Sonnet 4.6 | 2025 | 41 | 0.710 | 0.165 |

**Overall within vs. between-model:** mean diff = 0.074, Cohen's d = 0.720, p ≈ 0.

**Non-significant pairs (3):** GPT-4o Mini vs. Claude Opus 4.5 (p = 0.210), Claude Opus 4.5 vs. Claude Sonnet 3.5 (p = 0.467), Gemini vs. Llama (p = 0.314). 27 of 36 pairs significant at p < 0.001; 33 of 36 at any level.

**Novel contribution:** Prior work tested 1 model (Hoq et al. on Java CS1 programs; Xu & Sheng on competitive programming; GPTSniffer on ~10-line GitHub snippets). We test 9 models spanning 2024–2025 on ~110-line Python Connect4 implementations — the first multi-model fingerprinting study on assignment-specific CS1 code.

**Cross-generation note:** 2025-era models show mixed diversity patterns — o4-mini (std 0.073) is as tight as GPT-4o Mini, but Claude Sonnet 4.6 (std 0.165) is far more variable than its 2024 counterpart Sonnet 3.5 (std 0.062). Flagged for future analysis.

**Sample size caveat:** Claude Opus 4.5 n=28 is the smallest sample; its comparisons have lower statistical power. The GPT-4o Mini vs. Claude Opus 4.5 non-significance (p=0.210) may partly reflect this.

---

## Commands

```bash
python run_analysis.py                    # full analysis (includes CodeBERT)
python run_analysis.py --skip-embeddings  # faster, skips CodeBERT
```

---

## Constraints

- False positives are very costly — prioritize precision over recall
- Output probability scores, not binary guilty/not-guilty
- Human baseline must be pre-November 2022 (pre-ChatGPT)

---

## Schedule

- **Spring 2026 (current):** Proposal submitted. RQ1 analysis complete. Light semester — main deliverable was the proposal.
- **Fall 2026:** Full capstone work — RQ2 classifier, human baseline integration, paper writing, defense.

---

## User

Uditi Sharma, senior CS student, beginner in ML. Explain with intuition first. The goal is deep understanding, not just using tools — she needs to defend this to her professor and write a real paper.
