# Evaluating Similarity Patterns in AI-Generated and Student-Submitted Academic Work

A capstone research project investigating whether AI-generated solutions to identical academic assignments exhibit measurable similarity patterns — and whether those patterns can distinguish AI-assisted work from human-written submissions.

---

## Project Overview

With the rise of Large Language Models (LLMs), students increasingly use AI tools to assist with assignments. Unlike traditional plagiarism, AI-generated solutions are typically original in wording and therefore bypass conventional plagiarism checkers.

This project studies whether multiple AI-generated solutions to the **same assignment** share detectable lexical, structural, or semantic patterns — and whether those patterns cluster differently from human-written work. The goal is not to label individual submissions as AI-generated, but to assess the feasibility of similarity-based indicators for AI assistance.

---

## Phase 1: Data Collection (Complete)

### What Was Generated

100 Python implementations of a **Connect 4** game were generated across three LLMs using the [OpenRouter API](https://openrouter.ai):

| Model | Generations |
|---|---|
| OpenAI GPT-4o | 70 |
| OpenAI GPT-4o Mini | 20 |
| Anthropic Claude 3.5 Sonnet | 10 |

Each model was prompted with **15 distinct coding style variations** (beginner-friendly, PEP 8 compliant, functional, heavily commented, compact, etc.) applied cyclically to introduce controlled stylistic diversity while keeping the task identical.

### Results

- **100/100** generations completed successfully (0 API failures)
- **91/100** files pass Python syntax validation
- **0** exact duplicates detected across all 100 generations
- **$0.73** total API cost (vs. $6.00 budget)
- ~277,000 characters of generated code across ~9,200 lines

### Output Layout

```
data/
├── raw/
│   ├── gpt4o/          # 70 generated files + JSON sidecars
│   ├── gpt4mini/       # 20 generated files + JSON sidecars
│   └── sonnet/         # 10 generated files + JSON sidecars
├── metadata.csv        # One row per generation (model, style, tokens, cost, MD5, etc.)
├── generation_log.txt  # Compact execution trace
└── validation_report.txt  # Post-generation QA summary
```

Each generated `.py` file includes an embedded provenance header (generation ID, timestamp, model, style, token counts, cost, full prompt) and a paired `.json` sidecar with the same metadata in machine-readable form.

---

## Phase 2: Similarity Analysis (Upcoming)

Planned analyses:

- **Lexical similarity** — TF-IDF and Jaccard similarity across token sets
- **Structural similarity** — Abstract Syntax Tree (AST) comparison to identify shared control flow and function structure independent of variable naming
- **Semantic similarity** — Code embeddings (e.g., CodeBERT) with cosine similarity to capture meaning beyond surface text
- **Cross-group comparison** — Compare AI-generated similarity distributions against human-written student submissions
- **Visualization** — PCA / UMAP clustering to visually inspect grouping by model, style, and authorship type

---

## Setup

### Prerequisites

- Python 3.9+
- An [OpenRouter](https://openrouter.ai) API key

### Installation

```bash
git clone <your-repo-url>
cd capstone
pip install requests python-dotenv
```

### Configuration

Create a `.env` file in the project root (this file is gitignored and should never be committed):

```
OPENROUTER_API_KEY=your_key_here
```

### Running the Pipeline

```bash
python pipeline.py
```

The pipeline is resumable — if interrupted, re-running it will skip already-completed generations.

---

## Repository Structure

```
capstone/
├── pipeline.py          # Data collection pipeline
├── data/                # All generated outputs and metadata
├── .env                 # API key (gitignored — not committed)
├── .gitignore
└── README.md
```

---

## Research Context

**Assignment used:** Implement a Connect 4 game in Python
**Why Connect 4?** It is a well-defined, self-contained programming task with a clear specification, making it suitable for generating multiple comparable solutions with controlled variation.

**Scope:** This project does not attempt to build a production AI-detection tool. It aims to rigorously assess whether similarity-based signals exist and are statistically meaningful — contributing to a more transparent, evidence-based framework for understanding AI use in academic settings.

---

## Author

Uditi Sharma
Capstone Project — 2025/2026
