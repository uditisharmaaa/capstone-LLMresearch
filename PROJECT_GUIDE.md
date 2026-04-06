# Capstone Project Guide: AI-Generated Code Detection

## Table of Contents
1. [Project Scope](#project-scope)
2. [What is This Project About?](#what-is-this-project-about)
3. [The Big Picture](#the-big-picture)
4. [What We've Built So Far](#what-weve-built-so-far)
5. [Technical Concepts Explained](#technical-concepts-explained)
6. [Our Results So Far](#our-results-so-far)
7. [How Our Work Compares to Existing Research](#how-our-work-compares-to-existing-research)
8. [Future Plans](#future-plans)
9. [How to Run the Code](#how-to-run-the-code)
10. [Project Structure](#project-structure)

---

## Project Scope

### What This Project IS
This is an AI code detection system for **specific intro CS assignments** where we have:
- **Pre-ChatGPT student submissions** (from professor's archive, ~2019 or earlier)
- **AI-generated solutions** (that we generate using GPT-4o, Claude, etc.)

We are building detection for **3 specific assignments**:
1. Connect4 (in progress)
2. Tic-Tac-Toe (planned)
3. Hangman (planned)

### What This Project is NOT
- ❌ A general-purpose AI detector that works on any code
- ❌ A system that works on assignments we haven't trained on
- ❌ A binary "guilty/innocent" classifier

### Why This Scope?
- **Realistic:** Professors have archives of old submissions for standard assignments
- **Controlled:** Same assignment = fair comparison between human and AI
- **Practical:** Intro CS courses reuse assignments year after year
- **Achievable:** Well-defined scope for a senior capstone

---

## What is This Project About?

### The Problem
Students are using AI tools like ChatGPT to write code for their assignments. Traditional plagiarism checkers (like MOSS or Turnitin) can't detect this because:
- Each AI-generated solution is **unique** (not copied from anywhere)
- The code is **original** every time the AI generates it
- There's no "source" to compare against

### Our Hypothesis
Even though each AI solution is unique, we believe AI-generated code has **hidden patterns** or "fingerprints" that make it different from human-written code. Think of it like handwriting - even if two people write the same sentence, their handwriting style is different.

### Our Goal
Build a system that can:
1. Detect these AI fingerprints in code **for specific assignments**
2. Show **how similar** a submission is to known AI-generated code
3. Give instructors a **probability score** (e.g., "75% likely AI-assisted") instead of just "yes/no"

### Requirements for Each Assignment
For each assignment we want to detect AI usage on, we need:
```
┌─────────────────────────────────────────────────────────┐
│              REQUIRED DATA PER ASSIGNMENT               │
├─────────────────────────┬───────────────────────────────┤
│  Pre-ChatGPT Student    │    AI-Generated               │
│  Submissions            │    Solutions                  │
│  (from professor)       │    (we generate)              │
│  Must be ~2019 or       │    Multiple models +          │
│  earlier                │    style variations           │
└─────────────────────────┴───────────────────────────────┘
```

---

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         OUR APPROACH                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   [AI-Generated Code]              [Human-Written Code]              │
│   (We have 100 samples)            (Getting from professor)         │
│          │                                   │                       │
│          └───────────────┬───────────────────┘                       │
│                          ▼                                           │
│              ┌─────────────────────┐                                 │
│              │  EXTRACT FEATURES   │                                 │
│              │  (Find patterns in  │                                 │
│              │   the code)         │                                 │
│              └──────────┬──────────┘                                 │
│                         ▼                                            │
│              ┌─────────────────────┐                                 │
│              │  MEASURE SIMILARITY │                                 │
│              │  (How alike are     │                                 │
│              │   the codes?)       │                                 │
│              └──────────┬──────────┘                                 │
│                         ▼                                            │
│              ┌─────────────────────┐                                 │
│              │  FIND CLUSTERS      │                                 │
│              │  (Do AI codes group │                                 │
│              │   together?)        │                                 │
│              └──────────┬──────────┘                                 │
│                         ▼                                            │
│              ┌─────────────────────┐                                 │
│              │  BUILD CLASSIFIER   │                                 │
│              │  (Train a model to  │                                 │
│              │   detect AI code)   │                                 │
│              └─────────────────────┘                                 │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## What We've Built So Far

### Phase 1: Data Collection ✅ COMPLETE
**What:** Generated 100 Connect4 game implementations using AI

**Details:**
- **70 solutions** from GPT-4o (OpenAI's best model)
- **20 solutions** from GPT-4o Mini (OpenAI's smaller/faster model)
- **10 solutions** from Claude 3.5 Sonnet (Anthropic's model)
- Each solution uses one of **15 different coding styles** (e.g., "beginner-friendly", "compact", "heavily commented")

**Why multiple styles?** Students might ask the AI to "write like a beginner" to avoid detection. We test if this actually works.

**Files:**
- `pipeline.py` - The script that generated all the code
- `data/raw/gpt4o/` - 70 GPT-4o generated files
- `data/raw/gpt4mini/` - 20 GPT-4o Mini generated files
- `data/raw/sonnet/` - 10 Claude Sonnet generated files
- `data/metadata.csv` - Information about each generation (model, style, cost, etc.)

---

### Phase 2: Feature Extraction ✅ COMPLETE
**What:** Extract measurable patterns from each code file

We extract **three types of features**:

#### A. Lexical Features (Surface-Level Patterns)
These are things you can see just by looking at the code text:

| Feature | What It Measures | Example |
|---------|------------------|---------|
| Line count | How long is the code? | 85 lines vs 120 lines |
| Average line length | Are lines short or long? | 40 chars vs 80 chars |
| Keyword frequency | How often does `if`, `for`, `while` appear? | 5% if-statements vs 10% |
| Comment density | How much is commented? | 10% comments vs 30% |
| Variable naming style | snake_case vs camelCase? | `my_var` vs `myVar` |

**File:** `src/features/lexical.py`

#### B. Structural Features (Code Structure Patterns)
These look at the **structure** of the code, ignoring names and formatting:

| Feature | What It Measures | Why It Matters |
|---------|------------------|----------------|
| AST depth | How nested is the code? | AI tends to write flatter code |
| Function count | How many functions? | AI often uses more functions |
| Cyclomatic complexity | How many decision paths? | Measures code complexity |
| Control flow pattern | Sequence of if/for/while | AI has consistent patterns |

**What is AST?** 
AST = Abstract Syntax Tree. It's a tree representation of code that captures its structure. Think of it like a sentence diagram from English class, but for code.

```
Code: if x > 0: return x
         
AST:  If-Statement
      ├── Condition: x > 0
      └── Body: Return(x)
```

**File:** `src/features/structural.py`

#### C. Semantic Features (Meaning-Based Patterns)
These capture what the code **means** or **does**, not just how it looks:

**What is CodeBERT?**
CodeBERT is like "Google Translate for code." It's a pre-trained AI model that can understand code. We use it to convert each code file into a **768-number summary** (called an "embedding") that captures the code's meaning.

```
Code: "def add(a, b): return a + b"
         ↓ CodeBERT
Embedding: [0.23, -0.45, 0.12, ..., 0.78]  (768 numbers)
```

Two code files that do similar things will have similar embeddings, even if they look completely different.

**File:** `src/features/semantic.py`

---

### Phase 3: Similarity Analysis ✅ COMPLETE
**What:** Measure how similar each pair of code files is

#### What is "Similarity"?
We convert each code file into a list of numbers (features). Then we measure how "close" two codes are using **cosine similarity**:

```
Code A features: [0.5, 0.3, 0.8]
Code B features: [0.4, 0.3, 0.9]

Cosine similarity = how aligned are these vectors?
                  = 0.98 (very similar!)
```

- **1.0** = Identical
- **0.0** = Completely different
- **0.7+** = Quite similar

#### What We Computed
For all 100 code files, we computed:
1. **TF-IDF Similarity** - Based on word/token frequencies
2. **CodeBERT Similarity** - Based on semantic meaning
3. **Edit Distance** - How many changes to transform one code into another (like spell-check distance)

**Files:** `src/similarity/analysis.py`, `src/similarity/visualization.py`

---

### Phase 4: Statistical Testing ✅ COMPLETE
**What:** Test if the patterns we see are statistically significant (not just random chance)

#### Key Question
> Do code files from the **same AI model** look more similar to each other than code from **different models**?

#### Statistical Tests We Used

**Mann-Whitney U Test:**
A way to compare two groups without assuming they follow a normal distribution. It answers: "Is Group A generally higher/lower than Group B?"

**Cohen's d (Effect Size):**
Measures how **big** the difference is:
- 0.2 = Small effect
- 0.5 = Medium effect
- 0.8 = Large effect

**p-value:**
The probability that we'd see this result by random chance:
- p < 0.05 = Significant (less than 5% chance it's random)
- p < 0.001 = Highly significant (less than 0.1% chance)

---

## Technical Concepts Explained

### TF-IDF (Term Frequency - Inverse Document Frequency)

**Plain English:** A way to measure how important each word is in a document.

**How it works:**
1. **Term Frequency (TF):** How often does this word appear in this code?
2. **Inverse Document Frequency (IDF):** How rare is this word across ALL codes?

**Example:**
- The word `for` appears in almost every code → Low IDF → Not distinctive
- The word `enumerate` appears in only some codes → High IDF → Distinctive

**Result:** Each code becomes a vector of numbers showing how distinctive each word is.

---

### Embeddings

**Plain English:** Converting something (text, code, images) into a list of numbers that captures its "essence."

**Analogy:** Think of GPS coordinates. "New York City" becomes [40.7, -74.0]. Cities that are close geographically have similar coordinates. Similarly, code that does similar things has similar embeddings.

**CodeBERT Embeddings:**
- Input: A code snippet (up to 512 tokens)
- Output: 768 numbers representing the code's meaning
- Similar code → Similar numbers

---

### Clustering

**Plain English:** Grouping similar things together automatically.

**What we're testing:** Do AI-generated codes naturally group together? Do GPT-4o codes cluster separately from Claude codes?

**Visualization:** We use PCA (Principal Component Analysis) to squash the 768-dimensional embeddings into 2D so we can plot them on a graph.

---

### Machine Learning Classification

**Plain English:** Teaching a computer to categorize things based on examples.

**Our plan:**
1. Show the computer lots of examples: "This is AI code" and "This is human code"
2. The computer learns the patterns
3. Given new code, it predicts: "This looks 73% like AI code"

**Models we'll use:**
- **Random Forest:** Makes predictions by averaging many simple decision trees
- **XGBoost:** Similar but more sophisticated, often wins ML competitions
- **Neural Networks:** More complex, can find subtle patterns

---

## Our Results So Far

### Key Finding 1: Different AI Models Have Different "Fingerprints"

| Model | Within-Model Similarity (TF-IDF) | Interpretation |
|-------|----------------------------------|----------------|
| Claude (Sonnet) | 0.883 | Most consistent - similar outputs each time |
| GPT-4o Mini | 0.831 | Middle - moderate variation |
| GPT-4o | 0.785 | Most varied - different each time |

**Statistical Significance:** All pairwise comparisons are **highly significant** (p < 0.001)

**What this means:** Even without human code to compare against, we can already tell the AI models apart!

---

### Key Finding 2: CodeBERT Shows Even Stronger Model Separation

Using semantic embeddings:
- Within-model similarity: **0.9969**
- Between-model similarity: **0.9957**
- p-value: **1.38e-93** (essentially zero chance this is random)

**What this means:** At a semantic level, each model has a distinct "style" of solving problems.

---

### Key Finding 3: Our Code is More Complex Than Prior Research

| Study | Assignment Type | Avg Edit Distance |
|-------|----------------|-------------------|
| Hoq & Leinonen 2024 | Simple conditionals (10 lines) | 88 |
| **Our Project** | Connect4 game (93 lines) | 1,147-1,350 |

**What this means:** We're tackling harder problems than previous research, which is more realistic for actual assignments.

---

### Generated Visualizations

All saved in `results/figures/`:

| File | What It Shows |
|------|---------------|
| `embedding_clusters_codebert.png` | 2D plot showing how different models cluster |
| `similarity_heatmap_tfidf.png` | 100x100 heatmap of pairwise similarities |
| `similarity_heatmap_codebert.png` | Same but with semantic embeddings |
| `model_comparison_tfidf.png` | Bar chart comparing model similarities |
| `similarity_distribution_tfidf.png` | Distribution curves of similarities |
| `edit_distance_comparison.png` | Our results vs prior research |

---

## How Our Work Compares to Existing Research

### The Hoq & Leinonen Paper (SIGCSE 2024)
*"Detecting ChatGPT-Generated Code Submissions in a CS1 Course"*

**What they did:**
- Used 3,162 student Java submissions + 3,000 ChatGPT generations
- Trained classifiers (SVM, XGBoost, ASTNN)
- Achieved 97% accuracy detecting AI code

**Their limitations → Our improvements:**

| Their Limitation | Our Improvement |
|------------------|-----------------|
| Only tested ChatGPT (one model) | We test GPT-4o, GPT-4o Mini, and Claude |
| Only Java code | We use Python |
| Only simple 10-line problems | We use complex 90+ line games |
| Binary yes/no classification | We give probability scores |
| No semantic embeddings | We use CodeBERT for meaning-based analysis |
| No visualization of why | We show clustering to explain decisions |

---

## Future Plans

### Target: 3 Intro CS Assignments

We are building detection for these specific assignments (where we have/will have pre-ChatGPT data):

| Assignment | Status | Human Data | AI Data |
|------------|--------|------------|---------|
| Connect4 | In Progress | Waiting | ✅ 100 samples |
| Tic-Tac-Toe | Planned | Need from professor | To generate |
| Hangman | Planned | Need from professor | To generate |

### Immediate Next Steps

#### 1. Get Pre-ChatGPT Student Submissions for Connect4
**What:** Connect4 code from 2019 or earlier (before ChatGPT existed)
**Why:** This is definitively human-written code to compare against
**Status:** Waiting for professor to provide access

#### 2. Test Main Hypothesis on Connect4
**Question:** Does AI code cluster separately from human code?
```
Prediction:
┌─────────────────┐     ┌─────────────────┐
│   AI Cluster    │     │  Human Cluster  │
│  ●●●●●●●●●●●    │     │   ○○○○○○○○○○    │
│    ●●●●●●●      │     │    ○○○○○○○      │
└─────────────────┘     └─────────────────┘
```

#### 3. Build Classification Model for Connect4
- Train Random Forest / XGBoost on combined features
- Output probability scores, not just yes/no
- Test on held-out data to measure accuracy
- **Priority:** High precision (minimize false accusations)

---

### After Connect4 Works: Expand to Other Assignments

#### 4. Tic-Tac-Toe
- Get pre-ChatGPT submissions from professor
- Generate AI solutions (50-100 samples)
- Build separate detection model
- Simpler than Connect4 - good baseline

#### 5. Hangman
- Get pre-ChatGPT submissions from professor
- Generate AI solutions (50-100 samples)
- Build separate detection model
- Different domain (string manipulation)

---

### Robustness Testing (Per Assignment)

For each assignment, test:
- Can students defeat detection by renaming variables?
- Does asking AI to "write like a beginner" work?
- Do style variations actually hide AI fingerprints?
- Does the model work across different AI models?

---

### Final Deliverables

#### Research Paper
- Document methodology and findings
- Compare with Hoq & Leinonen results
- Present results for all 3 assignments
- Discuss limitations (assignment-specific nature)

#### Demo System
- Takes a submission + assignment type
- Returns: probability score + nearest AI examples
- Works for Connect4, Tic-Tac-Toe, Hangman

---

## How to Run the Code

### Prerequisites
```bash
# Install required packages
pip install scikit-learn pandas numpy matplotlib seaborn python-Levenshtein pyarrow torch transformers
```

### Run the Full Analysis
```bash
# With CodeBERT embeddings (slower but better results)
python run_analysis.py

# Without embeddings (faster, for quick testing)
python run_analysis.py --skip-embeddings
```

### Output
- `results/figures/` - All visualizations
- `results/analysis_report.txt` - Text summary
- `results/lexical_features.parquet` - Extracted features
- `results/structural_features.parquet` - AST features
- `results/codebert_embeddings.npy` - Semantic embeddings

---

## Project Structure

```
capstone/
├── pipeline.py                 # Phase 1: Data generation script
├── run_analysis.py             # Main analysis script (run this!)
├── PROJECT_GUIDE.md            # This file
│
├── data/
│   ├── raw/                    # Generated code files
│   │   ├── gpt4o/              # 70 GPT-4o solutions
│   │   ├── gpt4mini/           # 20 GPT-4o Mini solutions
│   │   └── sonnet/             # 10 Claude solutions
│   ├── metadata.csv            # Generation metadata
│   └── features/               # (Future: extracted features)
│
├── src/
│   ├── utils/
│   │   └── preprocessing.py    # Load and clean code files
│   ├── features/
│   │   ├── lexical.py          # Surface-level features
│   │   ├── structural.py       # AST-based features
│   │   └── semantic.py         # CodeBERT embeddings
│   └── similarity/
│       ├── analysis.py         # Similarity computation
│       └── visualization.py    # Plotting functions
│
├── results/
│   ├── figures/                # Generated plots
│   ├── analysis_report.txt     # Summary report
│   └── *.parquet               # Saved features
│
└── notebooks/                  # (Future: Jupyter notebooks)
```

---

## Glossary

| Term | Definition |
|------|------------|
| **AST** | Abstract Syntax Tree - tree representation of code structure |
| **CodeBERT** | Pre-trained AI model that understands code |
| **Cosine Similarity** | Measure of angle between two vectors (1 = same, 0 = perpendicular) |
| **Embedding** | Converting data into a list of numbers that capture meaning |
| **Cohen's d** | Effect size measure (0.2 small, 0.5 medium, 0.8 large) |
| **p-value** | Probability result is due to chance (< 0.05 = significant) |
| **TF-IDF** | Term Frequency-Inverse Document Frequency - word importance measure |
| **Clustering** | Grouping similar items together automatically |
| **Classification** | Predicting categories (AI vs Human) |
| **Random Forest** | ML model using many decision trees |
| **XGBoost** | Advanced gradient boosting ML model |

---

## Questions?

If anything is unclear, ask! This project combines:
- **Software Engineering** (building the pipeline)
- **Natural Language Processing** (analyzing code as text)
- **Machine Learning** (training classifiers)
- **Statistics** (hypothesis testing)

It's a lot, but each piece builds on the others.

---

*Last updated: April 2026*
