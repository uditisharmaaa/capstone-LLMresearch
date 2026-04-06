"""
Semantic feature extraction using pre-trained code models.
Captures code meaning/functionality using CodeBERT embeddings.
"""
import numpy as np
import pandas as pd
from typing import List, Optional, Tuple
from pathlib import Path
import warnings

# Try importing torch and transformers
try:
    import torch
    from transformers import AutoTokenizer, AutoModel
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False
    warnings.warn("PyTorch/Transformers not installed. Semantic features will be unavailable.")


class CodeBERTEmbedder:
    """
    Generate code embeddings using CodeBERT or similar models.
    """

    def __init__(self, model_name: str = "microsoft/codebert-base", device: str = None):
        if not TORCH_AVAILABLE:
            raise ImportError("PyTorch and Transformers required for semantic features.")

        self.model_name = model_name
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")

        print(f"Loading {model_name} on {self.device}...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name).to(self.device)
        self.model.eval()
        print("Model loaded successfully.")

    def get_embedding(self, code: str, max_length: int = 512) -> np.ndarray:
        """
        Get embedding for a single code snippet.

        Returns a 768-dimensional vector (for CodeBERT base).
        """
        # Tokenize
        inputs = self.tokenizer(
            code,
            return_tensors="pt",
            truncation=True,
            max_length=max_length,
            padding=True,
        ).to(self.device)

        # Get embeddings
        with torch.no_grad():
            outputs = self.model(**inputs)

        # Use mean pooling over sequence dimension
        # outputs.last_hidden_state shape: [batch, seq_len, hidden_dim]
        embeddings = outputs.last_hidden_state.mean(dim=1)

        return embeddings.cpu().numpy().flatten()

    def get_embeddings_batch(
        self,
        codes: List[str],
        batch_size: int = 8,
        max_length: int = 512,
        show_progress: bool = True
    ) -> np.ndarray:
        """
        Get embeddings for multiple code snippets.

        Returns array of shape (n_samples, embedding_dim).
        """
        all_embeddings = []

        for i in range(0, len(codes), batch_size):
            batch = codes[i:i + batch_size]

            if show_progress:
                print(f"Processing batch {i // batch_size + 1}/{(len(codes) + batch_size - 1) // batch_size}")

            # Tokenize batch
            inputs = self.tokenizer(
                batch,
                return_tensors="pt",
                truncation=True,
                max_length=max_length,
                padding=True,
            ).to(self.device)

            # Get embeddings
            with torch.no_grad():
                outputs = self.model(**inputs)

            # Mean pooling
            embeddings = outputs.last_hidden_state.mean(dim=1)
            all_embeddings.append(embeddings.cpu().numpy())

        return np.vstack(all_embeddings)


def extract_codebert_embeddings(
    codes: List[str],
    model_name: str = "microsoft/codebert-base",
    batch_size: int = 8,
    device: str = None
) -> np.ndarray:
    """
    Extract CodeBERT embeddings for a list of code snippets.

    Args:
        codes: List of code strings
        model_name: HuggingFace model name
        batch_size: Batch size for processing
        device: 'cuda' or 'cpu'

    Returns:
        np.ndarray of shape (n_samples, 768)
    """
    embedder = CodeBERTEmbedder(model_name=model_name, device=device)
    return embedder.get_embeddings_batch(codes, batch_size=batch_size)


def extract_semantic_features_batch(
    df: pd.DataFrame,
    code_column: str = 'code_clean',
    model_name: str = "microsoft/codebert-base",
    batch_size: int = 8,
) -> pd.DataFrame:
    """
    Extract semantic embeddings for all code in a DataFrame.

    Returns DataFrame with embedding columns and filepath.
    """
    codes = df[code_column].tolist()
    embeddings = extract_codebert_embeddings(codes, model_name=model_name, batch_size=batch_size)

    # Create DataFrame with embedding columns
    embedding_df = pd.DataFrame(
        embeddings,
        columns=[f'emb_{i}' for i in range(embeddings.shape[1])]
    )
    embedding_df['filepath'] = df['filepath'].values

    return embedding_df


def compute_embedding_similarity(
    embeddings: np.ndarray,
    metric: str = 'cosine'
) -> np.ndarray:
    """
    Compute pairwise similarity matrix for embeddings.

    Args:
        embeddings: Array of shape (n_samples, embedding_dim)
        metric: 'cosine' or 'euclidean'

    Returns:
        Similarity matrix of shape (n_samples, n_samples)
    """
    from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

    if metric == 'cosine':
        return cosine_similarity(embeddings)
    elif metric == 'euclidean':
        # Convert distance to similarity
        distances = euclidean_distances(embeddings)
        return 1 / (1 + distances)
    else:
        raise ValueError(f"Unknown metric: {metric}")


def reduce_embedding_dimensions(
    embeddings: np.ndarray,
    n_components: int = 50,
    method: str = 'pca'
) -> Tuple[np.ndarray, any]:
    """
    Reduce embedding dimensions for visualization or efficiency.

    Args:
        embeddings: Array of shape (n_samples, 768)
        n_components: Target dimensions
        method: 'pca' or 'umap'

    Returns:
        Reduced embeddings and fitted reducer
    """
    if method == 'pca':
        from sklearn.decomposition import PCA
        reducer = PCA(n_components=n_components)
    elif method == 'umap':
        try:
            import umap
            reducer = umap.UMAP(n_components=n_components, metric='cosine')
        except ImportError:
            raise ImportError("umap-learn required for UMAP reduction")
    else:
        raise ValueError(f"Unknown method: {method}")

    reduced = reducer.fit_transform(embeddings)
    return reduced, reducer


if __name__ == "__main__":
    if not TORCH_AVAILABLE:
        print("PyTorch not available. Install with: pip install torch transformers")
        exit(1)

    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from src.utils.preprocessing import load_all_generated_code

    df = load_all_generated_code()
    print(f"Loaded {len(df)} files")

    # Test on first 5 files
    sample_codes = df['code_clean'].head(5).tolist()

    print("\nExtracting CodeBERT embeddings for 5 samples...")
    embeddings = extract_codebert_embeddings(sample_codes, batch_size=2)
    print(f"Embedding shape: {embeddings.shape}")

    # Compute similarity
    similarity = compute_embedding_similarity(embeddings)
    print(f"\nSimilarity matrix:\n{similarity}")
