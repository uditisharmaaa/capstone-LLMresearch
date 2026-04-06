#!/usr/bin/env python3
"""
Main analysis script for AI-Generated Code Similarity Analysis.
Generates visualizations and statistical results for professor meeting.

Usage:
    python run_analysis.py [--skip-embeddings]

Options:
    --skip-embeddings    Skip CodeBERT embeddings (faster, uses TF-IDF only)
"""
import sys
import argparse
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from src.utils.preprocessing import load_all_generated_code, get_code_stats
from src.features.lexical import extract_lexical_features_batch, compute_tfidf_features
from src.features.structural import extract_structural_features_batch
from src.similarity.analysis import (
    compute_pairwise_similarity,
    compute_edit_distance_matrix,
    analyze_model_similarities,
    run_hypothesis_tests,
    get_within_group_similarities,
    get_between_group_similarities,
    summary_statistics,
)
from src.similarity.visualization import (
    plot_similarity_heatmap,
    plot_similarity_distribution,
    plot_model_comparison_boxplot,
    plot_2d_embedding,
    plot_edit_distance_comparison,
    create_summary_report,
)

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')


def main(skip_embeddings: bool = False):
    print("=" * 60)
    print("AI-GENERATED CODE SIMILARITY ANALYSIS")
    print("=" * 60)

    # Create output directories
    results_dir = Path("results")
    figures_dir = results_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    # =========================================================================
    # 1. LOAD DATA
    # =========================================================================
    print("\n[1/6] Loading generated code...")
    df = load_all_generated_code()
    stats = summary_statistics(df)

    print(f"  Loaded {stats['total_samples']} code files")
    print(f"  Models: {stats['by_model']}")
    print(f"  Average lines: {stats['avg_lines']:.1f}")
    print(f"  All files valid: {df['is_valid'].all()}")

    # =========================================================================
    # 2. EXTRACT LEXICAL FEATURES + TF-IDF
    # =========================================================================
    print("\n[2/6] Extracting lexical features...")
    lexical_df = extract_lexical_features_batch(df)
    print(f"  Extracted {len(lexical_df.columns)} lexical features")

    # TF-IDF for similarity
    tfidf_matrix, tfidf_vectorizer = compute_tfidf_features(df['code_clean'].tolist())
    print(f"  TF-IDF matrix shape: {tfidf_matrix.shape}")

    # =========================================================================
    # 3. EXTRACT STRUCTURAL (AST) FEATURES
    # =========================================================================
    print("\n[3/6] Extracting structural features...")
    structural_df = extract_structural_features_batch(df)
    print(f"  Extracted {len(structural_df.columns)} structural features")

    # =========================================================================
    # 4. COMPUTE SIMILARITIES
    # =========================================================================
    print("\n[4/6] Computing similarities...")

    # TF-IDF similarity
    tfidf_sim = compute_pairwise_similarity(tfidf_matrix, metric='cosine')
    print(f"  TF-IDF similarity matrix: {tfidf_sim.shape}")

    # Edit distance (replicating Hoq & Leinonen)
    print("  Computing edit distances (may take a moment)...")
    try:
        edit_distances = compute_edit_distance_matrix(df['code_no_comments'].tolist())
        has_edit_distance = True
        print(f"  Edit distance matrix: {edit_distances.shape}")
    except ImportError:
        print("  WARNING: python-Levenshtein not installed, skipping edit distance")
        has_edit_distance = False

    # CodeBERT embeddings (optional)
    has_embeddings = False
    if not skip_embeddings:
        print("  Computing CodeBERT embeddings (may take a few minutes)...")
        try:
            from src.features.semantic import extract_codebert_embeddings, reduce_embedding_dimensions
            embeddings = extract_codebert_embeddings(
                df['code_clean'].tolist(),
                batch_size=4,
            )
            embedding_sim = compute_pairwise_similarity(embeddings, metric='cosine')
            has_embeddings = True
            print(f"  Embedding matrix: {embeddings.shape}")
        except Exception as e:
            print(f"  WARNING: Could not compute embeddings: {e}")
            print("  Run with --skip-embeddings to skip this step")

    # =========================================================================
    # 5. STATISTICAL ANALYSIS
    # =========================================================================
    print("\n[5/6] Running statistical analysis...")

    models = df['model'].tolist()

    # Analyze TF-IDF similarities
    tfidf_analysis = analyze_model_similarities(tfidf_sim, models)
    tfidf_tests = run_hypothesis_tests(tfidf_sim, models)

    print("\n  TF-IDF Similarity Analysis:")
    print(tfidf_analysis[['comparison', 'mean_similarity', 'std_similarity']].to_string(index=False))

    print("\n  Hypothesis Tests (TF-IDF):")
    if 'within_vs_between' in tfidf_tests:
        result = tfidf_tests['within_vs_between']
        print(f"    Within-model mean: {result['group1_mean']:.4f}")
        print(f"    Between-model mean: {result['group2_mean']:.4f}")
        print(f"    Difference: {result['mean_difference']:.4f}")
        print(f"    Cohen's d: {result['cohens_d']:.4f}")
        print(f"    p-value: {result['mannwhitney_p']:.2e}")

    # Analyze embeddings if available
    if has_embeddings:
        embed_analysis = analyze_model_similarities(embedding_sim, models)
        embed_tests = run_hypothesis_tests(embedding_sim, models)

        print("\n  CodeBERT Embedding Similarity Analysis:")
        print(embed_analysis[['comparison', 'mean_similarity', 'std_similarity']].to_string(index=False))

        print("\n  Hypothesis Tests (Embeddings):")
        if 'within_vs_between' in embed_tests:
            result = embed_tests['within_vs_between']
            print(f"    Within-model mean: {result['group1_mean']:.4f}")
            print(f"    Between-model mean: {result['group2_mean']:.4f}")
            print(f"    Difference: {result['mean_difference']:.4f}")
            print(f"    Cohen's d: {result['cohens_d']:.4f}")
            print(f"    p-value: {result['mannwhitney_p']:.2e}")

    # Edit distance analysis
    if has_edit_distance:
        # Convert edit distance to similarity for comparison
        max_dist = edit_distances.max()
        edit_sim = 1 - (edit_distances / max_dist)
        edit_analysis = analyze_model_similarities(edit_sim, models)

        print("\n  Edit Distance Analysis (as similarity):")
        print(edit_analysis[['comparison', 'mean_similarity', 'std_similarity']].to_string(index=False))

        # Compute raw edit distances by group
        within_edit = get_within_group_similarities(edit_distances, models)
        print("\n  Mean Edit Distance by Model (raw):")
        for model, dists in within_edit.items():
            print(f"    {model}: {np.mean(dists):.1f} (+/- {np.std(dists):.1f})")

    # =========================================================================
    # 6. GENERATE VISUALIZATIONS
    # =========================================================================
    print("\n[6/6] Generating visualizations...")

    # Heatmap
    plot_similarity_heatmap(
        tfidf_sim, models,
        title="TF-IDF Code Similarity by Model",
        save_path=str(figures_dir / "similarity_heatmap_tfidf.png")
    )

    # Distribution plots
    within_sims = get_within_group_similarities(tfidf_sim, models)
    between_sims = {}
    unique_models = list(set(models))
    for i, m1 in enumerate(unique_models):
        for m2 in unique_models[i+1:]:
            key = f"{m1}_vs_{m2}"
            between_sims[key] = get_between_group_similarities(tfidf_sim, models, m1, m2)

    plot_similarity_distribution(
        within_sims, between_sims,
        title="TF-IDF Similarity Distributions",
        save_path=str(figures_dir / "similarity_distribution_tfidf.png")
    )

    # Model comparison
    plot_model_comparison_boxplot(
        tfidf_analysis,
        title="Model Similarity Comparison (TF-IDF)",
        save_path=str(figures_dir / "model_comparison_tfidf.png")
    )

    # 2D embedding visualization
    if has_embeddings:
        from sklearn.decomposition import PCA
        pca = PCA(n_components=2)
        embeddings_2d = pca.fit_transform(embeddings)

        plot_2d_embedding(
            embeddings_2d, models,
            title="CodeBERT Embedding Clusters by Model",
            save_path=str(figures_dir / "embedding_clusters_codebert.png")
        )

        plot_similarity_heatmap(
            embedding_sim, models,
            title="CodeBERT Embedding Similarity by Model",
            save_path=str(figures_dir / "similarity_heatmap_codebert.png")
        )

    # Edit distance comparison
    if has_edit_distance:
        hoq_baseline = {
            'gpt4o': 88.30,  # Hoq's ChatGPT-ChatGPT
            'gpt4mini': 88.30,
            'sonnet': 88.30,
        }
        plot_edit_distance_comparison(
            within_edit,
            hoq_baseline=hoq_baseline,
            title="Edit Distance Comparison with Hoq & Leinonen",
            save_path=str(figures_dir / "edit_distance_comparison.png")
        )

    # Generate text report
    report = create_summary_report(
        stats, tfidf_analysis, tfidf_tests,
        save_path=str(results_dir / "analysis_report.txt")
    )

    # Save feature DataFrames
    lexical_df.to_parquet(results_dir / "lexical_features.parquet", index=False)
    structural_df.to_parquet(results_dir / "structural_features.parquet", index=False)
    print(f"\n  Saved features to {results_dir}/")

    if has_embeddings:
        np.save(results_dir / "codebert_embeddings.npy", embeddings)
        print(f"  Saved CodeBERT embeddings to {results_dir}/codebert_embeddings.npy")

    # =========================================================================
    # SUMMARY
    # =========================================================================
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    print(f"\nResults saved to: {results_dir.absolute()}")
    print(f"Figures saved to: {figures_dir.absolute()}")
    print("\nKey Findings:")

    if 'within_vs_between' in tfidf_tests:
        result = tfidf_tests['within_vs_between']
        if result['mean_difference'] > 0 and result['mannwhitney_p'] < 0.05:
            print("  - Within-model similarity IS higher than between-model similarity")
            print(f"    (difference = {result['mean_difference']:.4f}, p = {result['mannwhitney_p']:.2e})")
            print("  - This supports H1: AI models produce distinct fingerprints")
        else:
            print("  - No significant difference between within/between model similarity")

    print("\nGenerated Figures:")
    for fig_path in sorted(figures_dir.glob("*.png")):
        print(f"  - {fig_path.name}")

    print("\n" + report)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run AI code similarity analysis")
    parser.add_argument('--skip-embeddings', action='store_true',
                        help='Skip CodeBERT embeddings (faster)')
    args = parser.parse_args()

    main(skip_embeddings=args.skip_embeddings)
