"""
Similarity analysis for comparing code across groups.
Computes pairwise similarities and statistical tests.
"""
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
from pathlib import Path
from scipy import stats
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances


def compute_pairwise_similarity(
    features: np.ndarray,
    metric: str = 'cosine'
) -> np.ndarray:
    """
    Compute pairwise similarity matrix.

    Args:
        features: Feature matrix of shape (n_samples, n_features)
        metric: 'cosine' or 'euclidean'

    Returns:
        Similarity matrix of shape (n_samples, n_samples)
    """
    if metric == 'cosine':
        return cosine_similarity(features)
    elif metric == 'euclidean':
        distances = euclidean_distances(features)
        return 1 / (1 + distances)
    else:
        raise ValueError(f"Unknown metric: {metric}")


def compute_edit_distance_matrix(codes: List[str], strip_comments: bool = True) -> np.ndarray:
    """
    Compute pairwise Levenshtein edit distances.
    This replicates Hoq & Leinonen's methodology for comparison.
    """
    try:
        from Levenshtein import distance as levenshtein_distance
    except ImportError:
        raise ImportError("python-Levenshtein required. Install with: pip install python-Levenshtein")

    import re

    def strip_code_comments(code: str) -> str:
        """Remove comments from code."""
        # Remove single-line comments
        code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)
        # Remove docstrings
        code = re.sub(r'"""[\s\S]*?"""', '', code)
        code = re.sub(r"'''[\s\S]*?'''", '', code)
        return code

    n = len(codes)
    matrix = np.zeros((n, n))

    processed_codes = codes
    if strip_comments:
        processed_codes = [strip_code_comments(c) for c in codes]

    for i in range(n):
        for j in range(i + 1, n):
            dist = levenshtein_distance(processed_codes[i], processed_codes[j])
            matrix[i, j] = dist
            matrix[j, i] = dist

    return matrix


def get_within_group_similarities(
    similarity_matrix: np.ndarray,
    groups: List[str]
) -> Dict[str, List[float]]:
    """
    Extract within-group similarities for each group.

    Args:
        similarity_matrix: Pairwise similarity matrix
        groups: List of group labels for each sample

    Returns:
        Dict mapping group name to list of pairwise similarities
    """
    unique_groups = list(set(groups))
    group_indices = {g: [i for i, x in enumerate(groups) if x == g] for g in unique_groups}

    within_group_sims = {}

    for group, indices in group_indices.items():
        sims = []
        for i, idx1 in enumerate(indices):
            for idx2 in indices[i + 1:]:
                sims.append(similarity_matrix[idx1, idx2])
        within_group_sims[group] = sims

    return within_group_sims


def get_between_group_similarities(
    similarity_matrix: np.ndarray,
    groups: List[str],
    group1: str,
    group2: str
) -> List[float]:
    """
    Extract similarities between two specific groups.
    """
    indices1 = [i for i, g in enumerate(groups) if g == group1]
    indices2 = [i for i, g in enumerate(groups) if g == group2]

    sims = []
    for i in indices1:
        for j in indices2:
            sims.append(similarity_matrix[i, j])

    return sims


def statistical_comparison(
    group1_sims: List[float],
    group2_sims: List[float]
) -> Dict[str, float]:
    """
    Perform statistical comparison between two groups of similarities.

    Returns:
        Dict with statistical test results
    """
    # Mann-Whitney U test (non-parametric)
    u_stat, u_pvalue = stats.mannwhitneyu(
        group1_sims, group2_sims, alternative='two-sided'
    )

    # Effect size (Cohen's d)
    mean1, mean2 = np.mean(group1_sims), np.mean(group2_sims)
    std_pooled = np.sqrt((np.var(group1_sims) + np.var(group2_sims)) / 2)
    cohens_d = (mean1 - mean2) / std_pooled if std_pooled > 0 else 0

    # T-test (for comparison)
    t_stat, t_pvalue = stats.ttest_ind(group1_sims, group2_sims)

    return {
        'group1_mean': mean1,
        'group2_mean': mean2,
        'group1_std': np.std(group1_sims),
        'group2_std': np.std(group2_sims),
        'mean_difference': mean1 - mean2,
        'cohens_d': cohens_d,
        'mannwhitney_u': u_stat,
        'mannwhitney_p': u_pvalue,
        'ttest_t': t_stat,
        'ttest_p': t_pvalue,
        'n_group1': len(group1_sims),
        'n_group2': len(group2_sims),
    }


def analyze_model_similarities(
    similarity_matrix: np.ndarray,
    models: List[str]
) -> pd.DataFrame:
    """
    Analyze similarities within and between different AI models.

    Returns DataFrame with comparison statistics.
    """
    unique_models = list(set(models))
    within_group = get_within_group_similarities(similarity_matrix, models)

    results = []

    # Within-group statistics
    for model in unique_models:
        if within_group[model]:
            results.append({
                'comparison': f'{model} (within)',
                'type': 'within',
                'model1': model,
                'model2': model,
                'mean_similarity': np.mean(within_group[model]),
                'std_similarity': np.std(within_group[model]),
                'n_pairs': len(within_group[model]),
            })

    # Between-group statistics
    for i, model1 in enumerate(unique_models):
        for model2 in unique_models[i + 1:]:
            between_sims = get_between_group_similarities(
                similarity_matrix, models, model1, model2
            )
            if between_sims:
                results.append({
                    'comparison': f'{model1} vs {model2}',
                    'type': 'between',
                    'model1': model1,
                    'model2': model2,
                    'mean_similarity': np.mean(between_sims),
                    'std_similarity': np.std(between_sims),
                    'n_pairs': len(between_sims),
                })

    return pd.DataFrame(results)


def run_hypothesis_tests(
    similarity_matrix: np.ndarray,
    models: List[str]
) -> Dict[str, Dict]:
    """
    Run hypothesis tests comparing model similarities.

    Tests:
    - H1: Within-model similarity > Between-model similarity
    - For each model pair
    """
    within_group = get_within_group_similarities(similarity_matrix, models)
    unique_models = list(set(models))

    results = {}

    # Aggregate all within-group similarities
    all_within = []
    for sims in within_group.values():
        all_within.extend(sims)

    # Aggregate all between-group similarities
    all_between = []
    for i, model1 in enumerate(unique_models):
        for model2 in unique_models[i + 1:]:
            all_between.extend(
                get_between_group_similarities(similarity_matrix, models, model1, model2)
            )

    # H1: Within > Between
    if all_within and all_between:
        results['within_vs_between'] = statistical_comparison(all_within, all_between)

    # Compare each pair of models
    for i, model1 in enumerate(unique_models):
        for model2 in unique_models[i + 1:]:
            if within_group.get(model1) and within_group.get(model2):
                results[f'{model1}_vs_{model2}'] = statistical_comparison(
                    within_group[model1], within_group[model2]
                )

    return results


def summary_statistics(df: pd.DataFrame) -> Dict:
    """Generate summary statistics for the dataset."""
    return {
        'total_samples': len(df),
        'by_model': df['model'].value_counts().to_dict(),
        'by_style': df['style_index'].value_counts().to_dict(),
        'avg_lines': df['line_count'].mean(),
        'avg_chars': df['char_count'].mean(),
    }


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from src.utils.preprocessing import load_all_generated_code

    df = load_all_generated_code()
    print(f"Loaded {len(df)} files")
    print(f"\nSummary: {summary_statistics(df)}")

    # Quick test with TF-IDF similarity
    from sklearn.feature_extraction.text import TfidfVectorizer

    vectorizer = TfidfVectorizer(max_features=500)
    tfidf_matrix = vectorizer.fit_transform(df['code_clean']).toarray()

    sim_matrix = compute_pairwise_similarity(tfidf_matrix, metric='cosine')
    print(f"\nSimilarity matrix shape: {sim_matrix.shape}")

    # Analyze by model
    model_analysis = analyze_model_similarities(sim_matrix, df['model'].tolist())
    print(f"\nModel similarity analysis:\n{model_analysis}")

    # Hypothesis tests
    print("\nHypothesis tests:")
    tests = run_hypothesis_tests(sim_matrix, df['model'].tolist())
    for name, result in tests.items():
        print(f"\n{name}:")
        print(f"  Mean diff: {result['mean_difference']:.4f}")
        print(f"  Cohen's d: {result['cohens_d']:.4f}")
        print(f"  p-value: {result['mannwhitney_p']:.4e}")
