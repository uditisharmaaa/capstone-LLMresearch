# CLAUDE.md - Project Context for AI Assistant

## Project Overview

This is Uditi's senior year capstone project on **detecting AI-generated code in academic submissions**. The project focuses on **specific intro CS assignments** where we have both pre-ChatGPT student submissions and AI-generated solutions.

**Key constraint:** This is NOT a general-purpose AI detector. It only works for assignments where we have:
1. Pre-ChatGPT human submissions (from professor's archive, ~2019 or earlier)
2. AI-generated solutions (that we generate ourselves)

## Project Scope

### What We're Building
- Detection system for **specific intro CS assignments**
- Compares new submissions against known human and AI baselines
- Outputs similarity scores and probability estimates
- Target assignments: Connect4, Tic-Tac-Toe, Hangman (intro CS level)

### What We're NOT Building
- General-purpose AI code detector
- System that works on arbitrary/unseen assignments
- Binary "guilty/innocent" classifier (we provide probabilities)

## Current Status

### Phase 1: Data Collection ✅ COMPLETE
- **100 AI-generated Connect4 solutions**
  - 70 from GPT-4o
  - 20 from GPT-4o Mini  
  - 10 from Claude 3.5 Sonnet
- 15 coding style variations applied
- All stored in `data/raw/{model}/`
- Metadata in `data/metadata.csv`
- Cost: $0.73 total

### Phase 2: Feature Extraction ✅ COMPLETE
- **Lexical features** (553 features): TF-IDF, keyword frequencies, line metrics, naming patterns
- **Structural features** (69 features): AST depth, node counts, cyclomatic complexity, control flow
- **Semantic features** (768 features): CodeBERT embeddings
- All extractors in `src/features/`

### Phase 3: Similarity Analysis ✅ COMPLETE
- Pairwise similarity matrices computed
- Edit distance analysis (replicating Hoq & Leinonen methodology)
- Statistical tests run (Mann-Whitney U, Cohen's d)
- Visualizations generated in `results/figures/`

### Phase 4: Human Data Integration ⏳ WAITING
- Need pre-ChatGPT student submissions from professor
- Expected "within a few days" (as of April 5, 2026)
- Will be Connect4 submissions from 2019 or earlier

### Phase 5: Classification Model 🔜 TODO
- Train Random Forest / XGBoost on combined features
- Evaluate accuracy, precision, recall, F1
- Priority: High precision (minimize false accusations)

## Key Findings So Far

### Finding 1: Different AI Models Have Distinguishable Fingerprints
| Model | Within-Model Similarity (TF-IDF) |
|-------|----------------------------------|
| Claude (Sonnet) | 0.883 (most consistent) |
| GPT-4o Mini | 0.831 |
| GPT-4o | 0.785 (most varied) |

All pairwise comparisons are **highly significant** (p < 0.001).

### Finding 2: CodeBERT Shows Strong Model Separation
- Within-model vs between-model: p = 1.38e-93
- Cohen's d = 0.57 (medium effect)

### Finding 3: Statistical Confirmation
Different AI models produce statistically distinguishable code patterns. This is novel - the Hoq paper only tested one model (ChatGPT).

## Related Work

### Hoq & Leinonen (SIGCSE 2024)
- Paper: "Detecting ChatGPT-Generated Code Submissions in a CS1 Course"
- Their approach: Binary classification with SVM, XGBoost, ASTNN, SANN
- Their best result: 97% accuracy with SANN
- Their limitation: Only tested ChatGPT, simple 10-line Java problems

### How We Differ
| Aspect | Hoq & Leinonen | Our Project |
|--------|----------------|-------------|
| AI Models | ChatGPT only | GPT-4o, GPT-4o Mini, Claude |
| Language | Java | Python |
| Complexity | ~10 lines | ~93 lines (Connect4) |
| Output | Binary yes/no | Probability scores |
| Features | TF-IDF + AST | + CodeBERT embeddings |

## Technical Stack

```
Python 3.9+
├── Data: pandas, numpy, pyarrow (parquet)
├── ML: scikit-learn, transformers, torch
├── Visualization: matplotlib, seaborn
├── Code Analysis: ast (stdlib), radon
├── Statistics: scipy
├── Text: python-Levenshtein
```

## Project Structure

```
capstone/
├── pipeline.py              # Data generation (Phase 1)
├── run_analysis.py          # Main analysis script
├── CLAUDE.md                # THIS FILE
├── PROJECT_GUIDE.md         # Simple overview for user
│
├── data/
│   ├── raw/                 # AI-generated code
│   │   ├── gpt4o/           # 70 files
│   │   ├── gpt4mini/        # 20 files
│   │   └── sonnet/          # 10 files
│   ├── metadata.csv         # Generation metadata
│   └── student_submissions/ # [FUTURE] Human code
│
├── src/
│   ├── utils/preprocessing.py
│   ├── features/
│   │   ├── lexical.py       # TF-IDF, keywords, etc.
│   │   ├── structural.py    # AST analysis
│   │   └── semantic.py      # CodeBERT embeddings
│   └── similarity/
│       ├── analysis.py      # Similarity computation
│       └── visualization.py # Plotting
│
├── results/
│   ├── figures/             # All generated plots
│   ├── analysis_report.txt
│   ├── lexical_features.parquet
│   ├── structural_features.parquet
│   └── codebert_embeddings.npy
│
└── docs/
    ├── index.html           # Project documentation
    └── COMPLETE_TUTORIAL.html # ML/NLP tutorial for user
```

## Key Files to Know

### pipeline.py
- Generates AI code via OpenRouter API
- Applies 15 style variations
- Saves with provenance headers
- Can resume interrupted runs

### run_analysis.py
- Main entry point for analysis
- Run with `python run_analysis.py`
- Use `--skip-embeddings` for faster runs without CodeBERT

### src/features/semantic.py
- CodeBERT embedding extraction
- Requires torch and transformers
- Uses `microsoft/codebert-base` model
- Outputs 768-dim vectors

## User Context

- **User:** Uditi Sharma (senior CS student)
- **Project type:** Senior capstone
- **Advisor:** Professor (has pre-ChatGPT student submissions)
- **User's ML background:** Beginner - needs concepts explained simply
- **User's goal:** Understand project well enough to present and defend to professor

## Important Constraints

1. **No general AI detection** - Only works for specific assignments with both human and AI baselines
2. **Minimize false positives** - Accusing innocent students is very costly
3. **Probability scores, not binary** - More transparent and fair
4. **Pre-ChatGPT baseline required** - Human submissions must be from before Nov 2022

## Next Steps (When Human Data Arrives)

1. Load and preprocess student submissions
2. Extract same features (lexical, structural, semantic)
3. Compute cross-group similarities (AI vs human)
4. Test main hypothesis: Does AI code cluster separately from human code?
5. Train classifier if hypothesis confirmed
6. Evaluate and document results

## Commands to Remember

```bash
# Run full analysis with CodeBERT
python run_analysis.py

# Run fast analysis (skip embeddings)
python run_analysis.py --skip-embeddings

# View documentation
open docs/COMPLETE_TUTORIAL.html

# Check results
ls results/figures/
cat results/analysis_report.txt
```

## Questions the Professor Might Ask

1. "Why similarity-based instead of direct classification?"
   → More transparent, provides probabilities, adapts to new models

2. "How do you handle students who modify AI code?"
   → Multi-feature approach: even if names change, AST and semantics may persist

3. "What's your false positive rate?"
   → TBD - need human data to calculate. We prioritize precision over recall.

4. "Does this generalize to other assignments?"
   → No - this is assignment-specific by design. That's the scope.

5. "How is this different from MOSS?"
   → MOSS compares submissions to each other. We compare against AI baseline.

## Notes for Future Sessions

- User prefers simple, non-mathematical explanations
- User needs to present to professor - help them understand deeply, not just use tools
- The project scope is intentionally narrow (specific assignments only)
- Pre-ChatGPT data is the critical missing piece right now
- All 100 generated files are syntactically valid (8 were fixed from markdown blocks)
