"""
Regenerate model_comparison_tfidf.png as a clean horizontal bar chart.
Shows within-model TF-IDF similarity for each of the 9 models, sorted by mean,
with a dashed reference line for the overall between-model mean.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Data from results/analysis_report.txt
models = {
    "GPT-4o Mini":        (0.8327, 0.0711),
    "Claude Sonnet 3.5":  (0.8194, 0.0621),
    "Claude Opus 4.5":    (0.8043, 0.1476),
    "o4-mini":            (0.7999, 0.0734),
    "GPT-4o":             (0.7996, 0.1057),
    "Claude Opus 4.6":    (0.7931, 0.1092),
    "Gemini 2.0 Flash":   (0.7804, 0.1183),
    "Llama 3.1 70B":      (0.7717, 0.1134),
    "Claude Sonnet 4.6":  (0.7095, 0.1651),
}

BETWEEN_MEAN = 0.7190

# Sort ascending so the highest bar is on top when flipped
names = list(models.keys())
means = [models[n][0] for n in names]
stds  = [models[n][1] for n in names]
order = np.argsort(means)
names = [names[i] for i in order]
means = [means[i] for i in order]
stds  = [stds[i]  for i in order]

fig, ax = plt.subplots(figsize=(7, 4.5))

colors = ['#4c78a8'] * len(names)
bars = ax.barh(names, means, xerr=stds, capsize=4,
               color=colors, alpha=0.82, error_kw=dict(elinewidth=1.2, capthick=1.2))

ax.axvline(BETWEEN_MEAN, color='#e45756', linestyle='--', linewidth=1.5,
           label=f'Between-model mean ({BETWEEN_MEAN:.3f})')

ax.set_xlabel('Mean TF-IDF Cosine Similarity', fontsize=11)
ax.set_title('Within-Model TF-IDF Similarity by Model', fontsize=12, pad=10)
ax.set_xlim(0.55, 1.02)
ax.tick_params(axis='y', labelsize=10)
ax.tick_params(axis='x', labelsize=9)

for i, (m, s) in enumerate(zip(means, stds)):
    ax.text(m + s + 0.006, i, f'{m:.3f}', va='center', fontsize=8.5, color='#333333')

ax.legend(fontsize=9, loc='lower right')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

out = Path('/Users/uditisharma/Desktop/capstone/results/figures/model_comparison_tfidf.png')
plt.savefig(out, dpi=180, bbox_inches='tight')
print(f"Saved to {out}")
