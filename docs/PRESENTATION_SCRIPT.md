# Presentation Script

Use this script to walk your professor through the presentation. Each section corresponds to a slide. The presentation is at `docs/presentation.html` - just open it in a browser and scroll through.

---

## Slide 1: Title

> "Hi Professor, thank you for meeting with me. I'd like to walk you through my progress on my capstone project - detecting AI-generated code in academic submissions."

---

## Slide 2: The Problem

> "The problem we're tackling is that students are using tools like ChatGPT to write their code. Traditional plagiarism tools like MOSS can't catch this because every time an AI generates code, it's unique - there's no source document being copied. Each generation is completely original.
>
> My hypothesis is that even though the code looks different each time, AI-generated code has hidden patterns - like fingerprints - that distinguish it from human-written code. 
>
> Think of it like handwriting - even if two people write the exact same sentence, you can tell their handwriting apart. Similarly, even if GPT-4o and Claude both write a Connect4 game, I believe there are subtle patterns in how they structure code, name variables, and solve problems that we can detect."

---

## Slide 3: Our Approach

> "Importantly, I'm not building a general-purpose AI detector that works on any code. That's too ambitious and probably impossible. Instead, I'm building detection for specific assignments where we have two things:
>
> First, pre-ChatGPT student submissions - code written before November 2022 when ChatGPT was released. This is definitively human-written code because AI tools didn't exist yet.
>
> Second, AI-generated solutions that I generate myself using current AI models. By controlling this, I know exactly what AI code looks like for this specific assignment.
>
> The assignments I'm targeting are Connect4 and other intro CS assignments like snake game - standard assignments that get reused year after year. This is realistic because professors have archives of old submissions."

---

## Slide 4: Project Timeline

> "Here's where I am in the project. I've completed three phases: data collection, feature extraction, and similarity analysis. 
>
> I'm currently blocked on phase 4 - I need the pre-ChatGPT student submissions to test my main hypothesis. Once I have those, I can see if AI code actually clusters separately from human code, and then build the classifier.
>
> The key insight so far is that even without human data, I've already discovered that different AI models have distinguishable patterns - which I'll show you in the findings."

---

## Slide 5: Data Collection

> "For data collection, I generated 100 Connect4 solutions using three different AI models: 70 from GPT-4o, which is OpenAI's flagship model; 20 from GPT-4o Mini, which is their smaller and faster model; and 10 from Claude 3.5 Sonnet, which is Anthropic's model.
>
> I used multiple models because prior research only tested ChatGPT. I wanted to answer a new question: do different AI models have different fingerprints? As I'll show, the answer is yes.
>
> I also used 15 different style variations. For example, I asked the AI to 'write like a beginner' or 'add lots of comments' or 'make it compact.' Why? Because a student might try this to avoid detection. I wanted to test if style variations actually hide the AI fingerprint.
>
> The total cost for all 100 generations was only 73 cents - this is very reproducible."

---

## Slide 6: Feature Extraction

> "Next, I extracted 1,390 features from each code file. Think of features as measurable characteristics - things we can quantify about each piece of code.
>
> **Lexical features** - 553 of them - are surface-level patterns. This includes TF-IDF, which measures how distinctive each word or token is. For example, the word 'for' appears in almost every program so it's not distinctive, but a specific variable name like 'board_state' might be more distinctive. I also measure things like average line length, how often different keywords appear, and naming conventions like snake_case versus camelCase.
>
> **Structural features** - 69 of them - capture code structure by parsing the Abstract Syntax Tree, or AST. The AST is like a diagram of the code's structure - it shows how deeply nested the code is, how many functions there are, how complex the control flow is. This captures patterns that survive even if you rename all the variables.
>
> **Semantic features** - 768 of them - come from CodeBERT, which is a pre-trained neural network that understands code. It converts each file into a 768-dimensional vector - basically 768 numbers that capture what the code means and does, not just how it looks. Two programs that solve the problem the same way will have similar vectors, even if the code looks completely different on the surface."

---

## Slide 7: Structural (AST) Features by Model

**How we made this:** Parsed each of the 100 code files using Python's `ast` module to build the Abstract Syntax Tree, then counted nodes, measured depth, etc. Plotted as box plots grouped by model.

> "Now let me show you something we haven't discussed yet - the actual feature values by model. This is new analysis that goes beyond just similarity scores.
>
> This graph shows **structural features** - things extracted from the AST, the Abstract Syntax Tree. The AST captures the structure of the code independent of what things are named.
>
> **Key findings with statistical significance:**
>
> **Function Count** is highly significant at p < 0.001. GPT-4o uses the most functions - averaging 9.3 per file - while GPT-4o Mini uses the fewest at 7.3. This means GPT-4o tends to break code into more modular pieces.
>
> **Total AST Nodes** is also significant at p < 0.001. This is a measure of overall code complexity. GPT-4o produces the most complex code by this metric.
>
> **Max AST Depth** is significant at p < 0.05. Sonnet has slightly shallower nesting than the others.
>
> Interestingly, **loop count and condition count don't differ significantly** - all models use similar numbers of if-statements and loops. The structural differences are in modularity and complexity, not control flow."

---

## Slide 8: Lexical Features by Model

**How we made this:** Analyzed the raw text of each code file - counted lines, tokens, measured line lengths, whitespace patterns. No parsing needed, just text analysis. Plotted as box plots grouped by model.

> "This graph shows **lexical features** - surface-level patterns you can see by looking at the code text.
>
> **Total Lines** differs significantly at p < 0.01. Sonnet writes the longest code at 104 lines on average, while GPT-4o Mini writes the shortest at 84 lines. GPT-4o is in between at 94 lines.
>
> **Unique Tokens** shows Sonnet uses the largest vocabulary - 96 unique tokens versus 84-87 for the others. This could mean Sonnet uses more varied variable names or function names.
>
> **Empty Line Ratio** is significant at p < 0.05 - GPT-4o uses more whitespace and blank lines in its code.
>
> What's interesting is that **average line length is similar across all models** at about 28-29 characters. So the models differ in how much code they write and how they structure it, but individual lines are about the same length.
>
> These structural and lexical differences give us concrete features that differ between models - which will help when we build the classifier."

---

## Slide 9: Key Finding #1 (TF-IDF Similarity)

> "Now let's look at similarity analysis. Here's my first key finding: different AI models produce code with statistically distinguishable patterns.
>
> Let me explain what 'within-model similarity' means. I took all 70 GPT-4o outputs and compared every pair - that's about 2,400 comparisons. For each pair, I calculated how similar they are using cosine similarity, where 1.0 means identical and 0.0 means completely different. Then I averaged all those similarities.
>
> **Within-model similarity tells us: when the same AI model generates code multiple times, how consistent is it?**
>
> The results show Claude is most consistent at 0.883 - when you ask Claude the same question multiple times, you get very similar code each time. GPT-4o Mini is in the middle at 0.831. GPT-4o is most varied at 0.785 - it produces more diverse outputs.
>
> But the key question is: are these differences statistically significant, or just random noise?
>
> The statistical tests confirm these are real differences. The comparison between Claude and GPT-4o has a p-value of 7.32e-10 - that's 0.000000000732 - essentially zero chance this happened by random chance. Cohen's d is 1.12, which is a large effect size, meaning the difference is substantial, not just detectable.
>
> **What this means for detection: each AI model has a distinct 'signature' in the code it produces. This is novel - prior research didn't compare multiple models.**"

---

## Slide 10: Key Finding #2

> "My second key finding comes from the CodeBERT semantic analysis, which captures what the code means rather than just how it looks.
>
> Here I compared within-model similarity versus between-model similarity.
>
> **Within-model similarity** is what I just explained - comparing GPT-4o outputs to other GPT-4o outputs, Claude to Claude, etc. The average is 0.9969.
>
> **Between-model similarity** compares across models - GPT-4o outputs to Claude outputs, for example. The average is slightly lower at 0.9957.
>
> The difference looks small - only 0.0012 - but with 100 samples and thousands of comparisons, we can detect even small systematic differences.
>
> The statistical test gives a p-value of 1.38e-93. That's a 1 followed by 93 zeros in the denominator - essentially zero probability this is random. Cohen's d is 0.57, which is a medium effect size.
>
> **What this means: at a semantic level - the level of what the code actually does - each model has a distinct 'style' of solving problems. Even when they produce code that looks different on the surface, there are deeper patterns we can detect.**"

---

## Slide 11: Bar Chart - Model Comparison

**How we made this:** Computed TF-IDF vectors for all 100 files, then calculated cosine similarity for every pair. Grouped similarities into "within-model" (e.g., GPT-4o vs GPT-4o) and "between-model" (e.g., GPT-4o vs Claude), then averaged each group.

> "Let me walk you through the visual evidence, starting with this bar chart.
>
> This graph directly shows what I mean by 'within-model' versus 'between-model' similarity.
>
> The **blue bars** show within-model similarity. For example, the first blue bar labeled 'sonnet (within)' shows: when I take all 10 Claude Sonnet outputs and compare every pair to each other, what's the average similarity? It's about 0.88 - quite high.
>
> The **orange bars** show between-model similarity. For example, 'sonnet vs gpt4o' shows: when I compare Claude outputs to GPT-4o outputs, what's the average? It's lower - about 0.79.
>
> The **key insight** is that blue bars are consistently taller than orange bars. Code from the same model is more similar to itself than to code from other models. That's the 'fingerprint' effect - each model has a distinct style.
>
> Also notice Claude (sonnet) has the tallest blue bar - it's the most consistent. GPT-4o has the shortest blue bar with the largest error bars - it's the most varied."

---

## Slide 12: Distribution - How Similarity is Spread

**How we made this:** Same TF-IDF cosine similarities as the bar chart, but plotted as histograms to show the full distribution of values, not just averages.

> "This graph shows the same data in a different way - as distributions.
>
> The **left panel** shows each model's consistency separately. Think of it as 'how spread out are the similarities within each model?'
>
> The blue histogram for Sonnet is a tall narrow spike near 0.95 - when you compare Claude outputs to each other, you almost always get very high similarity. It's very consistent.
>
> The green histogram for GPT-4o is much wider - similarities range from 0.5 to 0.95. GPT-4o produces much more varied outputs each time.
>
> The **right panel** combines everything into two groups: all within-model comparisons (blue) versus all between-model comparisons (orange). The dashed line shows the average.
>
> You can see there's a lot of overlap - that's expected since all models are solving the same problem. But the blue distribution is shifted slightly to the right of orange, confirming that within-model similarity is higher on average."

---

## Slide 13: Heatmap - Every File Compared

**How we made this:** Same TF-IDF similarity matrix (100x100), visualized as a heatmap. Files sorted by model so same-model comparisons appear in diagonal blocks.

> "This is a heatmap - a 100 by 100 grid where every cell represents one comparison.
>
> Each row is one file, each column is one file. The cell where they intersect shows how similar those two files are. Brighter colors - red and orange - mean higher similarity, closer to 1.0. Darker blue means lower similarity.
>
> The diagonal from top-left to bottom-right is always brightest because that's each file compared to itself - always 1.0.
>
> **The interesting pattern here is the bright cross** - those horizontal and vertical bright lines. This shows that certain specific files are very similar to MANY other files, across all models. These are probably 'standard' solutions - common ways to implement Connect4 that all AI models tend to converge on.
>
> The within-model versus between-model difference is statistically real - we proved that with the bar chart and p-values - but it's subtle enough that it doesn't dominate what we see visually here. The cross pattern from these 'standard solution' files is more visually prominent."

---

## Slide 14: Clustering - Visualizing CodeBERT Embeddings

**How we made this:** Fed each code file through CodeBERT (Microsoft's pre-trained model) to get 768-dimensional embeddings. Used PCA to reduce 768 dimensions to 2 for visualization. Each dot = one file, colored by model.

> "This scatter plot visualizes the CodeBERT semantic embeddings.
>
> Each dot is one of the 100 code files. Green dots are GPT-4o, orange are GPT-4o Mini, and blue are Claude Sonnet.
>
> **Here's the challenge:** CodeBERT converts each file into 768 numbers. We can't visualize 768 dimensions, so I used PCA - Principal Component Analysis - to compress those 768 dimensions down to just 2. That's what 'Dimension 1' and 'Dimension 2' represent - they're the two most important directions that capture the most variation.
>
> **What to look for:** If different models have different fingerprints, same-colored dots should cluster together rather than being randomly mixed.
>
> Looking at the graph, there is some grouping - the blue Sonnet dots are mostly in the upper area, green GPT-4o dots spread across the middle and bottom. But it's not perfect separation.
>
> That's actually expected - all three models are solving the same Connect4 problem, so they're fundamentally similar. The statistical tests are more sensitive than our eyes - they confirm the clustering is real and significant, even if it's not visually dramatic."

---

## Slide 15: Edit Distance - Comparison to Prior Research

**How we made this:** Computed Levenshtein edit distance (character-level) between all pairs of code files within each model. Compared our average distances to the values reported in the Hoq & Leinonen paper.

> "This last graph compares our work to Hoq and Leinonen's prior research.
>
> **What is edit distance?** It's the minimum number of character changes - insertions, deletions, or replacements - needed to transform one piece of code into another. It's like the spell-check distance you're familiar with, but for entire files instead of single words.
>
> **Blue bars** are our results with Connect4 code, which averages about 93 lines. **Orange bars** are from the Hoq & Leinonen paper, which used simple 10-line Java problems.
>
> The difference is dramatic: our edit distances are around 1,150 to 1,350, while theirs were around 88. That's 10 to 15 times larger.
>
> **Why does this matter?** It shows we're tackling much more complex, realistic code than prior research. Simple 10-line problems like 'check if a number is even' aren't representative of real intro CS assignments. Connect4 with game logic, win detection, and user interaction is much more realistic."

---

## Slide 16: Comparison to Prior Research (Table)

> "This slide summarizes the key differences between my project and the Hoq & Leinonen paper in table form.
>
> **Models tested:** They only used ChatGPT. I'm testing three different models - GPT-4o, GPT-4o Mini, and Claude - which lets me answer new questions about whether models have different fingerprints.
>
> **Code complexity:** They used simple 10-line Java problems - things like 'check if a number is even.' My Connect4 solutions average 93 lines with game logic, win detection, and user interaction. This is much more realistic for actual assignments.
>
> **Output type:** They gave binary yes/no classifications. I'm providing probability scores - for example, '73% likely AI-generated.' This is more transparent and fairer, especially when we're uncertain.
>
> **Semantic analysis:** They used TF-IDF and AST features, but no deep learning embeddings. I'm using CodeBERT to capture meaning-level patterns that survive surface-level obfuscation."

---

## Slide 17: Next Steps

> "Here's what happens when I get the pre-ChatGPT student submissions.
>
> First, I'll load them and extract the exact same 1,390 features - lexical, structural, and semantic. This gives us an apples-to-apples comparison.
>
> Then I'll test my main hypothesis: **does AI code cluster separately from human code?** If my hypothesis is correct, when I plot human code alongside AI code, I should see two distinct clusters - not a mixed blob.
>
> If the hypothesis holds, I'll train a Random Forest or XGBoost classifier on the combined features. The classifier will learn to distinguish AI from human based on all 1,390 features.
>
> My priority is **high precision** - minimizing false accusations. In this context, falsely accusing an innocent student is much worse than missing a cheater. So I'll tune the model to be conservative - only flagging submissions when we're very confident.
>
> After Connect4 works, I'll replicate the process for other intro CS assignments like Snake game."

---

## Slide 18: Anticipated Questions

*Be ready to expand on any of these:*

**Q: Why similarity-based instead of direct classification?**
> "There are three reasons. First, it's more transparent - I can show exactly which AI samples a submission is most similar to, not just a black-box 'yes.' Second, it provides probabilities instead of binary decisions, which is fairer when we're uncertain. Third, it's more adaptable - when a new AI model comes out, I can add samples from it without retraining the entire classifier."

**Q: How do you handle students who modify AI code?**
> "This is why I use three types of features that capture different aspects. If a student renames all the variables, the lexical TF-IDF features will change - but the AST structural features won't, because the code structure is the same. And the CodeBERT semantic embedding captures what the code does, not what things are named. So even with modifications, some fingerprint may persist. That said, heavy modification is an open question I'll test with the human data."

**Q: Does this generalize to other assignments?**
> "No, and that's intentional. Each assignment needs its own baseline of human and AI code. But this is actually realistic - professors reuse the same assignments year after year, so they can build up baselines over time. The methodology generalizes even if the model doesn't."

**Q: How is this different from MOSS?**
> "MOSS - Measure of Software Similarity - compares student submissions against each other to find copying between students. I'm doing something completely different: comparing against a known AI baseline. MOSS can't detect AI-generated code because there's no 'source' being copied - each AI generation is unique. My approach creates that baseline intentionally."

**Q: What about false positives?**
> "This is my biggest concern. Falsely accusing an innocent student has serious consequences. That's why I'm outputting probability scores, not binary decisions. And when I train the classifier, I'll prioritize precision over recall - meaning I'd rather miss some AI code than falsely accuse a human. The professor can then set their own threshold based on how certain they want to be."

---

## Slide 19: Summary

> "To summarize my progress:
>
> I've generated 100 AI solutions for Connect4 using three different models - GPT-4o, GPT-4o Mini, and Claude. I extracted nearly 1,400 features per file across lexical, structural, and semantic dimensions.
>
> The key finding is that **different AI models have statistically distinguishable patterns**. This is novel - prior research only looked at one model. The statistical significance is extremely high, with p-values essentially at zero and medium to large effect sizes.
>
> The blocking item right now is the pre-ChatGPT student data. Once I have that, I can test whether AI code clusters separately from human code, which is the core hypothesis that the entire detection system depends on."

---

## Slide 20: Future Research Questions

> "Before I wrap up, I want to share some research questions that emerged from this analysis. These are things I'd like to investigate further, and they show how the findings open up new directions.
>
> **From the heatmap cross pattern:** Why do certain files match everything? I'd like to analyze which style variations produce these 'standard' solutions. And interestingly, we might be able to use these convergence points as stronger detection signals - if a submission matches these common AI patterns, that's a red flag.
>
> **From the model consistency differences:** Claude is much more consistent than GPT-4o. Does that make Claude-generated code easier to detect? And can we go beyond just 'is this AI?' to identify which specific model generated the code?
>
> **From style variations:** Which styles actually make AI code harder to detect? If a student asks for 'beginner style,' does that really help evade detection, or does the AI fingerprint persist anyway?
>
> **Robustness questions:** At what point does modified AI code become 'human enough' to evade detection? Do fingerprints transfer across different assignments - if I train on Connect4, does it work on Snake? And as OpenAI and Anthropic release newer models, do the fingerprints change?
>
> These are all testable questions that could extend this work."

---

## Slide 21: Questions

> "That's my progress so far. Do you have any questions?"

---

## Tips for the Presentation

1. **Open the presentation beforehand** - run `open docs/presentation.html` in terminal
2. **Have the terminal ready** to show `python run_analysis.py` if asked
3. **Have the results folder open** to show the actual PNG figures if needed
4. **Know your numbers**: 100 samples, 1,390 features, p < 0.001, Cohen's d = 0.57-1.12
5. **Emphasize what's novel**: multiple models, semantic embeddings, probability scores
6. **Practice explaining within-model vs between-model similarity** - this is the core concept
7. **The presentation is 21 slides** - budget about 1-2 minutes per slide for a 25-40 minute presentation
8. **Slides 7-8 show actual feature values**, slides 11-15 show similarity graphs - take your time on these, they're the visual evidence

## Glossary - Know These Terms

**TF-IDF (Term Frequency-Inverse Document Frequency)**: Measures how distinctive each word is. Words that appear in every file (like 'for' or 'if') get low scores. Words that appear in only some files get high scores. This helps identify distinctive vocabulary patterns.

**Cohen's d (Effect Size)**: Measures how big a difference is, not just whether it exists. 0.2 = small effect (barely noticeable), 0.5 = medium effect (noticeable), 0.8 = large effect (obvious). Our values range from 0.49 to 1.12 - medium to large.

**p-value**: The probability of seeing this result if there were actually no real difference (just random noise). A p-value of 0.05 means 5% chance it's random. Our p-values like 1.38e-93 mean essentially 0% chance - the differences are definitely real.

**Cosine Similarity**: Measures the angle between two vectors. 1.0 = identical direction (maximally similar), 0.0 = perpendicular (unrelated), -1.0 = opposite. We use this to compare feature vectors.

**CodeBERT**: A pre-trained transformer model from Microsoft, similar to GPT but designed to understand code. It converts code into 768-dimensional vectors where semantically similar code has similar vectors.

**AST (Abstract Syntax Tree)**: A tree representation of code structure. It captures what the code does structurally (if statements, loops, function calls) without caring about variable names or formatting.

**Within-model similarity**: How similar are outputs from the SAME model? (GPT-4o vs GPT-4o, Claude vs Claude)

**Between-model similarity**: How similar are outputs from DIFFERENT models? (GPT-4o vs Claude)

## If Asked About Limitations

- "This only works for assignments where we have baseline data - both pre-ChatGPT human code and AI-generated samples. It won't work on arbitrary new assignments."
- "We're not making binary guilty/innocent decisions - just providing probability scores for instructors to interpret."
- "Heavy modification of AI code is an open question. If a student substantially rewrites AI output, it may not be detectable - but at some point, that's arguably their own work."
- "The 15 style variations I tested may not cover all ways students try to disguise AI code."
- "False positives are my biggest concern. I'm prioritizing precision over recall - better to miss some AI code than falsely accuse innocent students."

---

## Future Research Questions to Explore

These questions emerged from the analysis and could guide future work or discussion with your professor:

### Questions from the Heatmap Cross Pattern
1. **What causes the "standard solution" convergence?** Which specific style variations or prompts cause all AI models to produce nearly identical code?
2. **Can convergence points be detection signals?** If certain code patterns appear across all AI models, are those patterns rare in human code? Could matching them be a strong indicator?
3. **Is there a "canonical AI solution"?** Do all AI models converge on a similar algorithmic approach (e.g., how they check for wins in Connect4)?

### Questions from Model Consistency Differences
4. **Is consistent = detectable?** Claude produces very similar outputs each time. Does this make Claude-generated code easier to detect than varied GPT-4o output?
5. **Model identification, not just detection?** Can we build a classifier that identifies WHICH model generated the code? This could be useful for understanding AI tool usage patterns.
6. **Why is GPT-4o more varied?** Is it temperature settings? Training data? Architecture? Understanding this could inform detection strategies.

### Questions from Style Variations
7. **Which styles evade detection best?** Of the 15 style variations, which ones produce code that's hardest to distinguish from human code?
8. **Does "beginner style" actually work?** Students might ask AI to "write like a beginner." Does this actually change the fingerprint, or do deeper patterns persist?
9. **Style vs model - which matters more?** Is the variation from style differences larger or smaller than the variation from model differences?

### Questions about Human vs AI (Once You Have Human Data)
10. **Do humans cluster separately from AI?** The core hypothesis. When plotted together, do human and AI submissions form distinct groups?
11. **Are some humans "AI-like"?** Are there human submissions that look unusually similar to AI code? What characterizes them?
12. **Are some AI outputs "human-like"?** Which AI-generated files are hardest to distinguish from human code? What makes them different?

### Robustness Questions
13. **Modification threshold?** If a student takes AI code and modifies it, at what point does it become undetectable? 10% changed? 30%? 50%?
14. **Which features survive modification?** If someone renames all variables, TF-IDF changes but AST structure stays. Which features are most robust to surface-level changes?
15. **Cross-assignment transfer?** If you train on Connect4, does detection work on Snake game? Or does each assignment need its own model?
16. **Temporal drift?** GPT-4o today vs GPT-4o in 6 months - do fingerprints change as models are updated?

### Practical Deployment Questions
17. **What probability threshold should instructors use?** 50%? 70%? 90%? How should this be calibrated?
18. **How should results be presented to instructors?** Raw probability? Percentile? Comparison to nearest AI samples?
19. **What's the false positive rate on edge cases?** Students who use AI for help but write their own code, students who naturally write "clean" code, etc.
20. **Can students game the system?** If they know how detection works, can they deliberately evade it?

### Theoretical Questions
21. **What IS the AI fingerprint?** At a fundamental level, what makes AI code different? Vocabulary? Structure? Problem-solving approach?
22. **Is detection an arms race?** As detection improves, will AI models adapt to be less detectable? Will this become a cat-and-mouse game?
23. **Ethical boundaries?** At what point is using AI assistance acceptable vs cheating? Where's the line?

---

*Use these questions to demonstrate depth of thinking if your professor asks "what would you do next?" or "what are the limitations?"*
