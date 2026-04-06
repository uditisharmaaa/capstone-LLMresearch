"""
Visualization tools for code similarity analysis.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Optional, Dict, Tuple
from pathlib import Path


def plot_similarity_heatmap(
    similarity_matrix: np.ndarray,
    labels: List[str],
    title: str = "Pairwise Similarity Matrix",
    figsize: Tuple[int, int] = (12, 10),
    save_path: Optional[str] = None
) -> plt.Figure:
    """
    Plot a heatmap of the similarity matrix.
    """
    fig, ax = plt.subplots(figsize=figsize)

    # Sort by labels for better visualization
    sorted_indices = np.argsort(labels)
    sorted_matrix = similarity_matrix[sorted_indices][:, sorted_indices]
    sorted_labels = [labels[i] for i in sorted_indices]

    sns.heatmap(
        sorted_matrix,
        ax=ax,
        cmap='RdYlBu_r',
        vmin=0,
        vmax=1,
        square=True,
        cbar_kws={'label': 'Similarity'},
    )

    ax.set_title(title, fontsize=14)
    ax.set_xlabel('Sample Index')
    ax.set_ylabel('Sample Index')

    # Add color bars for groups
    unique_labels = sorted(set(labels))
    colors = plt.cm.Set2(np.linspace(0, 1, len(unique_labels)))
    label_to_color = dict(zip(unique_labels, colors))

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Saved heatmap to {save_path}")

    return fig


def plot_similarity_distribution(
    within_sims: Dict[str, List[float]],
    between_sims: Optional[Dict[str, List[float]]] = None,
    title: str = "Similarity Distributions",
    figsize: Tuple[int, int] = (12, 6),
    save_path: Optional[str] = None
) -> plt.Figure:
    """
    Plot distributions of within-group and between-group similarities.
    """
    fig, axes = plt.subplots(1, 2, figsize=figsize)

    # Within-group distributions
    ax = axes[0]
    for group, sims in within_sims.items():
        if sims:
            ax.hist(sims, bins=30, alpha=0.5, label=f'{group} (n={len(sims)})', density=True)
    ax.set_xlabel('Similarity')
    ax.set_ylabel('Density')
    ax.set_title('Within-Model Similarity Distributions')
    ax.legend()

    # Combined comparison
    ax = axes[1]
    all_within = []
    for sims in within_sims.values():
        all_within.extend(sims)

    ax.hist(all_within, bins=30, alpha=0.5, label=f'Within-model (n={len(all_within)})', density=True)

    if between_sims:
        all_between = []
        for sims in between_sims.values():
            all_between.extend(sims)
        ax.hist(all_between, bins=30, alpha=0.5, label=f'Between-model (n={len(all_between)})', density=True)

    ax.set_xlabel('Similarity')
    ax.set_ylabel('Density')
    ax.set_title('Within vs Between Model Similarity')
    ax.legend()
    ax.axvline(np.mean(all_within), color='blue', linestyle='--', alpha=0.7)
    if between_sims and all_between:
        ax.axvline(np.mean(all_between), color='orange', linestyle='--', alpha=0.7)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Saved distribution plot to {save_path}")

    return fig


def plot_model_comparison_boxplot(
    analysis_df: pd.DataFrame,
    title: str = "Model Similarity Comparison",
    figsize: Tuple[int, int] = (10, 6),
    save_path: Optional[str] = None
) -> plt.Figure:
    """
    Plot boxplot comparing model similarities.
    """
    fig, ax = plt.subplots(figsize=figsize)

    # Separate within and between comparisons
    within = analysis_df[analysis_df['type'] == 'within']
    between = analysis_df[analysis_df['type'] == 'between']

    x_labels = []
    means = []
    stds = []
    colors = []

    for _, row in within.iterrows():
        x_labels.append(f"{row['model1']}\n(within)")
        means.append(row['mean_similarity'])
        stds.append(row['std_similarity'])
        colors.append('steelblue')

    for _, row in between.iterrows():
        x_labels.append(f"{row['model1']}\nvs\n{row['model2']}")
        means.append(row['mean_similarity'])
        stds.append(row['std_similarity'])
        colors.append('coral')

    x_pos = np.arange(len(x_labels))
    ax.bar(x_pos, means, yerr=stds, capsize=5, color=colors, alpha=0.7)

    ax.set_xticks(x_pos)
    ax.set_xticklabels(x_labels, fontsize=9)
    ax.set_ylabel('Mean Similarity')
    ax.set_title(title)
    ax.set_ylim(0, 1)

    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='steelblue', alpha=0.7, label='Within-model'),
        Patch(facecolor='coral', alpha=0.7, label='Between-model'),
    ]
    ax.legend(handles=legend_elements, loc='upper right')

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Saved comparison plot to {save_path}")

    return fig


def plot_2d_embedding(
    embeddings_2d: np.ndarray,
    labels: List[str],
    title: str = "Code Embedding Clustering",
    figsize: Tuple[int, int] = (10, 8),
    save_path: Optional[str] = None
) -> plt.Figure:
    """
    Plot 2D visualization of code embeddings colored by group.
    """
    fig, ax = plt.subplots(figsize=figsize)

    unique_labels = sorted(set(labels))
    colors = plt.cm.Set2(np.linspace(0, 1, len(unique_labels)))
    label_to_color = dict(zip(unique_labels, colors))

    for label in unique_labels:
        mask = [l == label for l in labels]
        ax.scatter(
            embeddings_2d[mask, 0],
            embeddings_2d[mask, 1],
            c=[label_to_color[label]],
            label=label,
            alpha=0.6,
            s=50,
        )

    ax.set_xlabel('Dimension 1')
    ax.set_ylabel('Dimension 2')
    ax.set_title(title)
    ax.legend()

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Saved embedding plot to {save_path}")

    return fig


def plot_edit_distance_comparison(
    distances_by_group: Dict[str, np.ndarray],
    hoq_baseline: Optional[Dict[str, float]] = None,
    title: str = "Edit Distance Comparison",
    figsize: Tuple[int, int] = (10, 6),
    save_path: Optional[str] = None
) -> plt.Figure:
    """
    Plot edit distance comparison, optionally with Hoq & Leinonen baseline.
    """
    fig, ax = plt.subplots(figsize=figsize)

    # Our results
    x_labels = list(distances_by_group.keys())
    means = [np.mean(d) for d in distances_by_group.values()]
    stds = [np.std(d) for d in distances_by_group.values()]

    x_pos = np.arange(len(x_labels))
    width = 0.35

    bars1 = ax.bar(x_pos - width/2, means, width, yerr=stds, capsize=5,
                   label='Our Results (Python, Connect4)', alpha=0.7, color='steelblue')

    # Hoq baseline if provided
    if hoq_baseline:
        hoq_values = [hoq_baseline.get(k, 0) for k in x_labels]
        bars2 = ax.bar(x_pos + width/2, hoq_values, width,
                       label='Hoq & Leinonen (Java, simple)', alpha=0.7, color='coral')

    ax.set_xticks(x_pos)
    ax.set_xticklabels(x_labels)
    ax.set_ylabel('Mean Edit Distance')
    ax.set_title(title)
    ax.legend()

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Saved edit distance plot to {save_path}")

    return fig


def create_summary_report(
    stats: Dict,
    analysis_df: pd.DataFrame,
    test_results: Dict,
    save_path: Optional[str] = None
) -> str:
    """
    Create a text summary report of the analysis.
    """
    lines = []
    lines.append("=" * 60)
    lines.append("AI-GENERATED CODE SIMILARITY ANALYSIS REPORT")
    lines.append("=" * 60)
    lines.append("")

    # Dataset summary
    lines.append("DATASET SUMMARY")
    lines.append("-" * 40)
    lines.append(f"Total samples: {stats['total_samples']}")
    lines.append(f"By model: {stats['by_model']}")
    lines.append(f"Average lines: {stats['avg_lines']:.1f}")
    lines.append(f"Average characters: {stats['avg_chars']:.1f}")
    lines.append("")

    # Similarity analysis
    lines.append("SIMILARITY ANALYSIS")
    lines.append("-" * 40)
    for _, row in analysis_df.iterrows():
        lines.append(f"{row['comparison']}: {row['mean_similarity']:.4f} (+/- {row['std_similarity']:.4f})")
    lines.append("")

    # Hypothesis tests
    lines.append("HYPOTHESIS TESTS")
    lines.append("-" * 40)
    for test_name, result in test_results.items():
        lines.append(f"\n{test_name}:")
        lines.append(f"  Group 1 mean: {result['group1_mean']:.4f}")
        lines.append(f"  Group 2 mean: {result['group2_mean']:.4f}")
        lines.append(f"  Mean difference: {result['mean_difference']:.4f}")
        lines.append(f"  Effect size (Cohen's d): {result['cohens_d']:.4f}")
        lines.append(f"  Mann-Whitney p-value: {result['mannwhitney_p']:.2e}")

        # Interpret
        if result['mannwhitney_p'] < 0.001:
            sig = "highly significant (p < 0.001)"
        elif result['mannwhitney_p'] < 0.05:
            sig = "significant (p < 0.05)"
        else:
            sig = "not significant"
        lines.append(f"  Significance: {sig}")

    lines.append("")
    lines.append("=" * 60)

    report = "\n".join(lines)

    if save_path:
        with open(save_path, 'w') as f:
            f.write(report)
        print(f"Saved report to {save_path}")

    return report


if __name__ == "__main__":
    # Test with dummy data
    print("Visualization module loaded successfully.")
    print("Use with actual analysis results to generate plots.")
