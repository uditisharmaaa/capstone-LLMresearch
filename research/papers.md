# Research Papers

Reference file for all verified papers related to this project.
**Rule:** Never add a paper without verifying it via web search. No hallucinated citations.

---

## Format

Each entry must include:
- Full citation (authors, title, venue, year)
- Verified URL or DOI
- What they actually found (not extrapolated)
- Relevance to this project

---

## Confirmed Papers

### Prather et al. (ITiCSE-WGR 2023)
**Citation:** Prather, J., Denny, P., Leinonen, J., Becker, B.A., Albluwi, I., Craig, M., Keuning, H., Kiesler, N., Kohn, T., Luxton-Reilly, A., MacNeil, S., Petersen, A., Pettit, R., Reeves, B.N., & Savelka, J. (2023). The Robots Are Here: Navigating the Generative AI Revolution in Computing Education. *Proceedings of the 2023 Working Group Reports on Innovation and Technology in Computer Science Education (ITiCSE-WGR '23)*. ACM.
**URL:** https://doi.org/10.1145/3623762.3633499 | arXiv:2310.00658
**Findings:**
- 20-country working group study on AI tool adoption in computing education
- Documents widespread and growing AI tool use among computing students
- Surveys students and instructors across multiple institutions and countries
- Most authoritative large-scale report on AI adoption in CS education (2023)

**Relevance:** Best available citation for widespread AI adoption in CS courses. Replaces the previously incorrect Zastudil et al. citation. Use to support motivation: AI tool use is common and growing.

**Note on incorrect prior citation:** "Cheaters or AI-Enhanced Learners: Consequences of ChatGPT for Programming Education" is authored by Humble, Boustedt, Holmgren, Milutinovic, Seipel, and Ostberg (University of Gavle), published in EJEL vol. 22, no. 2, pp. 16-29, 2024 -- NOT by Zastudil et al. Zastudil, Rogalska, Kapp, Vaughn, and MacNeil wrote "Generative AI in Computing Education: Perspectives of Students and Instructors" (IEEE FIE 2023, arXiv:2308.04309), which is a qualitative interview study with no usage percentage data. Neither paper supports a specific "25%+" claim.

---

### Hoq et al. (2024)
**Citation:** Hoq, M., Shi, Y., Leinonen, J., Babalola, D., Lynch, C., & Akram, B. (2024). Detecting ChatGPT-Generated Code Submissions in a CS1 Course. *Proceedings of the 55th ACM Technical Symposium on Computer Science Education (SIGCSE 2024)*.
**URL:** https://dl.acm.org/doi/10.1145/3626252.3630826
**Findings:**
- Binary classification of ChatGPT vs human code in a CS1 Java course
- Features: TF-IDF, AST-based (ASTNN), SANN (style-based neural network)
- Best result: 97% accuracy with SANN
- Dataset: ~10-line Java solutions to simple CS1 problems
- Only tested ChatGPT (GPT-3.5); no other models

**Relevance:** Primary prior work. We extend it by: (1) testing 6 models, (2) using Python, (3) using longer/more complex programs, (4) adding CodeBERT embeddings, (5) outputting probabilities not binary labels.

**Limitations of their work we should address:**
- Single model tested — generalizes poorly
- Very short programs (10 lines) — trivially distinguishable
- Binary output — not appropriate for academic integrity use

---

### Shi et al. (ICSE 2025) — DetectCodeGPT
**Citation:** Shi, Y., Zhang, H., Wan, C., & Gu, X. (2025). Between Lines of Code: Unraveling the Distinct Patterns of Machine and Human Programmers. *Proceedings of the 47th International Conference on Software Engineering (ICSE 2025)*. IEEE.
**URL:** https://arxiv.org/abs/2401.06461
**GitHub:** https://github.com/YerbaPage/DetectCodeGPT
**Findings:**
- Zero-shot detection — no labeled training data needed
- Core method: NPR (Normalized Perturbed Log Rank). Perturbs code by inserting spaces/newlines; machine-generated code scores drop more under perturbation than human code (it's more "optimal" under the LLM that generated it)
- Tested on 6 open-source models under 7B parameters (Incoder, Phi-1, StarCoder, WizardCoder, CodeGen2, CodeLlama)
- Dataset: Python functions from CodeSearchNet and The Vault (GitHub open-source)
- Best AUROC: 0.9308 (CodeSearchNet, T=0.2), averaging 0.8308 across all settings
- 7.6% relative AUROC improvement over strongest baseline (Log Rank)
- Explicitly did NOT test GPT-4o, Claude, or other large proprietary models

**Relevance:** Strong related work — most rigorous zero-shot approach for this problem, published at ICSE 2025. Directly relevant for comparison and positioning.

**How we differ / their gap we fill:**
- They only tested small open-source models (<7B); we test GPT-4o, Claude, Gemini — the models actually used by students
- They use generic GitHub functions; we use assignment-specific CS1 submissions with a pre-ChatGPT human baseline
- Their method is zero-shot (no human baseline); ours is supervised with known human examples
- High-temperature (T=1.0) remains hard for them; we address diversity through 15 style variations

---

### Xu & Sheng (2025) — CodeVision
**Citation:** Xu, Z., & Sheng, V. S. (2025). CodeVision: Detecting LLM-Generated Code Using 2D Token Probability Maps and Vision Models. *arXiv preprint arXiv:2501.03288*.
**URL:** https://arxiv.org/abs/2501.03288
**Status:** arXiv preprint (not peer-reviewed venue as of Jan 2025)
**Findings:**
- Converts code into 2D matrices of per-token log probabilities (via OpenAI API), then classifies those matrices as images using vision models (ViT, ResNet)
- Dataset: 28,342 samples from Project CodeNet; 6 languages (C, C++, Go, Java, Python, Ruby); LLM code generated with GPT-3.5-turbo-instruct and GPT-4-turbo
- Best results: AUC 0.97–0.99 across languages with ResNet; outperforms DetectGPT (0.97) and GPTZero
- Inference is fast (0.000064 sec/sample for ResNet) but requires OpenAI API preprocessing (13 sec/sample)
- Code Translation attack causes 0.25 AUC drop — largest vulnerability

**Relevance:** Novel approach using vision models; strong results but meaningful limitations.

**How we differ / their limitations:**
- Requires OpenAI API for log probabilities — external dependency, ongoing cost, not reproducible without API access
- Treats any non-LLM GitHub code as "human" — no verified pre-ChatGPT student baseline
- General algorithmic problems (CodeNet), not assignment-specific educational submissions
- No analysis of multi-model distinguishability — they detect AI vs human, not which AI
- Not yet peer-reviewed (arXiv only as of Jan 2025)

---

### Nguyen et al. (JSS 2024) — GPTSniffer
**Citation:** Nguyen, P.T., Di Rocco, J., Di Sipio, C., Rubei, R., Di Ruscio, D., & Di Penta, M. (2024). Is this Snippet Written by ChatGPT? An Empirical Study with a CodeBERT-Based Classifier. *Journal of Systems and Software*, Vol. 214. Also presented at ESEM 2024.
**URL:** https://doi.org/10.1016/j.jss.2024.112059 | arXiv: https://arxiv.org/abs/2307.09381 | GitHub: https://github.com/MDEGroup/GPTSniffer
**Findings:**
- Fine-tuned CodeBERT as a binary classifier (human vs. ChatGPT-generated code) — same core approach as ours
- Key insight: using *paired* snippets (human + AI solving the same problem) as training data achieves F1=1.0 vs. ~0.73 unpaired
- Outperforms GPTZero and OpenAI Text Classifier by large margin — those tools are trained on natural language and fail on code
- Multi-language (Java, Python, others from CodeSearchNet)

**Relevance:** Most directly comparable to our CodeBERT approach. Critical to cite and differentiate from.

**How we differ:**
- They test only ChatGPT (GPT-3.5); we test 6 models including GPT-4o, Claude, Gemini
- Their dataset is GitHub snippets; ours is CS1 assignment submissions with pre-ChatGPT human baseline
- Paired training insight is directly applicable to our setup — worth replicating

---

### Xu & Sheng (AAAI 2024) — AIGCode
**Citation:** Xu, Z., & Sheng, V.S. (2024). Detecting AI-Generated Code Assignments Using Perplexity of Large Language Models. *Proceedings of the AAAI Conference on Artificial Intelligence*, Vol. 38, No. 21, pp. 23155–23162.
**URL:** https://doi.org/10.1609/aaai.v38i21.30361
**Also:** Student abstract companion — Xu, Z., Xu, R., & Sheng, V.S. (2024). ChatGPT-Generated Code Assignment Detection Using Perplexity of Large Language Models. *AAAI 2024*, pp. 23688–23689. DOI: https://doi.org/10.1609/aaai.v38i21.30527
**Findings:**
- Problem framing is identical to ours: detecting AI-generated code in academic assignment submissions
- Method (AIGCode): targeted masking perturbation + CodeBERT fill-in; scores combine perplexity, perplexity variance, and burstiness
- Dataset: IBM CodeNet (filtered to 10–100 line programs in C, C++, C#, Java, JavaScript, Python)
- Tested against text-davinci-003 only
- Average AUC: 0.87 vs. GPTZero's 0.56

**Relevance:** Closest paper to our problem framing — assignment-specific code detection in an educational context. Must cite prominently.

**How we differ:**
- They test one model (text-davinci-003); we test 6 including current GPT-4o and Claude
- They use CodeNet (competitive programming); we use real CS1 student submissions
- They output AUC scores; we aim for probability scores with interpretability

---

### Oedingen et al. (AI Journal 2024)
**Citation:** Oedingen, M., Engelhardt, R.C., Denz, R., Hammer, M., & Konen, W. (2024). ChatGPT Code Detection: Techniques for Uncovering the Source of Code. *AI (MDPI)*, Vol. 5, No. 3, pp. 1066–1094.
**URL:** https://arxiv.org/abs/2405.15512
**Findings:**
- Benchmarks multiple detection techniques including embedding features + DNN, Random Forest, XGBoost, and a white-box Bayes classifier
- Black-box (embeddings + classifier): 98% accuracy
- Interpretable white-box: 85–88% accuracy
- Humans cannot detect AI code at above-chance rates
- Published in peer-reviewed AI journal (MDPI), not just arXiv

**Relevance:** Surveys the same technique space we're using (embeddings + classifiers). Strong evidence that Random Forest / XGBoost approaches work well. Good benchmark to compare against.

**How we differ:**
- Multi-model (we test 6 models; they test ChatGPT)
- We have a real pre-ChatGPT student submission baseline; their human data is from GitHub
- Their interpretable Bayes classifier approach is interesting — worth considering for our classifier phase

---

### Wang et al. (2023) — AIGC Detectors on Code
**Citation:** Wang, J., Liu, S., Xie, X., & Li, Y. (2023). Evaluating AIGC Detectors on Code Content. *arXiv preprint arXiv:2304.05193*.
**URL:** https://arxiv.org/abs/2304.05193
**Findings:**
- Evaluated 6 existing AIGC detectors (3 commercial, 3 open-source) on code
- Finding: all existing detectors perform significantly worse on code than on natural language text
- Fine-tuning within-domain helps; cross-domain generalization stays poor
- Humans cannot detect AI code at above-chance rates (confirmed independently)
- Dataset: ~492,500 samples (ChatGPT-generated Q&A, code summarization, code generation)

**Relevance:** Provides the core motivation for why code needs specialized detectors — general-purpose tools fail. Strong justification for our code-specific approach.

---

### Feng et al. (EMNLP 2020) — CodeBERT
**Citation:** Feng, Z., Guo, D., Tang, D., Duan, N., Feng, X., Gong, M., Shou, L., Qin, B., Liu, T., Jiang, D., & Zhou, M. (2020). CodeBERT: A Pre-Trained Model for Programming and Natural Languages. *Findings of ACL: EMNLP 2020*, pp. 1536–1547.
**URL:** https://doi.org/10.18653/v1/2020.findings-emnlp.139 | arXiv: https://arxiv.org/abs/2002.08155
**Findings:**
- RoBERTa-base architecture (125M params, 768-dim hidden size) pre-trained on NL-PL pairs from CodeSearchNet (2.1M bimodal + 6.4M unimodal examples across 6 languages)
- Two pre-training objectives: Masked Language Modeling (MLM) on NL-PL pairs + Replaced Token Detection (RTD) on all code
- 768-dim embedding = [CLS] token hidden state at final layer — represents aggregated sequence meaning
- Evaluated on: NL code search (MRR 0.7603), code documentation generation (BLEU 17.83)
- Does NOT use AST — treats code as flat token sequence; authors acknowledge this as a limitation
- Variable names, comments, token order all affect the embedding (no renaming invariance)

**Relevance:** We use CodeBERT embeddings as our semantic features. Must cite as the foundation.

**Critical caveat for our paper:**
CodeBERT was designed for NL↔code semantic matching (e.g., "does this docstring describe this function?"). Using [CLS] embeddings to compare two code files for authorship/style similarity is an *extension* the paper does not make. Our finding — that within-model AI code clusters together in CodeBERT embedding space — is a valid empirical result, but we must frame it as an empirical observation, not something CodeBERT was designed to do. We cannot claim "CodeBERT captures coding style" as a theoretical given; we can claim "we empirically find that CodeBERT embeddings separate AI models with p=1.38e-93."

---

## Papers Found — Verify Before Citing

Found via CodeVision (arXiv:2501.03288) references. Titles and arXiv IDs are real but details not independently verified yet. Do not cite without running web search first.

| Paper | arXiv / DOI | Why relevant |
|-------|-------------|--------------|
| Yang et al. (2023) — "Zero-shot detection of machine-generated codes" | arXiv:2310.05103 | Zero-shot code detection, relevant methodology comparison |
| Ye et al. (2024) — "Uncovering LLM-Generated Code: A Zero-Shot Synthetic Code Detector via Code Rewriting" | arXiv:2405.16133 | Zero-shot via code rewriting; structural patterns |
| Mitchell et al. (2023) — "DetectGPT: Zero-shot machine-generated text detection using probability curvature" | ICML 2023 | Foundational detection method, widely cited |
| Feng et al. (2020) — CodeBERT original paper | arXiv:2002.08155 | We use CodeBERT embeddings — must cite the original |
| Suresh et al. (2024) — "Is Watermarking LLM-Generated Code Robust?" | arXiv:2403.17983 | Robustness of code transformations — relevant to modified AI code |

---

## How to Add a Paper

1. Web search the paper to confirm it exists with correct details
2. Copy the format above
3. Fill in all fields — no field left blank
4. Add to "Confirmed Papers" section only after verification
