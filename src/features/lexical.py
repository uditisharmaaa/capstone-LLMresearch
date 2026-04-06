"""
Lexical feature extraction for code similarity analysis.
Captures surface-level text patterns in code.
"""
import re
import keyword
import numpy as np
import pandas as pd
from collections import Counter
from typing import Dict, List, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


# Python keywords and builtins to track
PYTHON_KEYWORDS = set(keyword.kwlist)
PYTHON_BUILTINS = {'print', 'len', 'range', 'int', 'str', 'list', 'dict',
                   'set', 'tuple', 'float', 'bool', 'input', 'open', 'enumerate',
                   'zip', 'map', 'filter', 'sorted', 'reversed', 'sum', 'max', 'min',
                   'abs', 'round', 'type', 'isinstance', 'hasattr', 'getattr'}


def extract_line_features(code: str) -> Dict[str, float]:
    """Extract line-based features."""
    lines = code.split('\n')
    line_lengths = [len(line) for line in lines]

    non_empty_lines = [line for line in lines if line.strip()]
    non_empty_lengths = [len(line) for line in non_empty_lines]

    return {
        'total_lines': len(lines),
        'non_empty_lines': len(non_empty_lines),
        'empty_line_ratio': 1 - len(non_empty_lines) / max(len(lines), 1),
        'avg_line_length': np.mean(line_lengths) if line_lengths else 0,
        'std_line_length': np.std(line_lengths) if line_lengths else 0,
        'max_line_length': max(line_lengths) if line_lengths else 0,
        'min_non_empty_length': min(non_empty_lengths) if non_empty_lengths else 0,
    }


def extract_whitespace_features(code: str) -> Dict[str, float]:
    """Extract whitespace and indentation features."""
    lines = code.split('\n')

    # Indentation analysis
    indents = []
    for line in lines:
        if line.strip():  # Non-empty line
            leading = len(line) - len(line.lstrip())
            indents.append(leading)

    # Check for tabs vs spaces
    uses_tabs = '\t' in code
    uses_spaces = any(line.startswith(' ') for line in lines if line.strip())

    return {
        'avg_indent': np.mean(indents) if indents else 0,
        'max_indent': max(indents) if indents else 0,
        'indent_levels': len(set(indents)),
        'uses_tabs': int(uses_tabs),
        'uses_spaces': int(uses_spaces),
        'trailing_whitespace_lines': sum(1 for line in lines if line.rstrip() != line),
    }


def extract_keyword_features(code: str) -> Dict[str, float]:
    """Extract Python keyword usage features."""
    # Tokenize roughly
    tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code)

    keyword_counts = Counter(t for t in tokens if t in PYTHON_KEYWORDS)
    builtin_counts = Counter(t for t in tokens if t in PYTHON_BUILTINS)

    total_tokens = len(tokens)

    features = {
        'total_tokens': total_tokens,
        'unique_tokens': len(set(tokens)),
        'keyword_count': sum(keyword_counts.values()),
        'builtin_count': sum(builtin_counts.values()),
        'keyword_ratio': sum(keyword_counts.values()) / max(total_tokens, 1),
    }

    # Add individual keyword counts (normalized)
    for kw in ['if', 'else', 'elif', 'for', 'while', 'def', 'return', 'class',
               'import', 'from', 'try', 'except', 'with', 'and', 'or', 'not']:
        features[f'kw_{kw}'] = keyword_counts.get(kw, 0) / max(total_tokens, 1) * 100

    return features


def extract_syntax_features(code: str) -> Dict[str, float]:
    """Extract syntax pattern features."""
    # Count specific patterns
    patterns = {
        'function_defs': len(re.findall(r'\bdef\s+\w+\s*\(', code)),
        'class_defs': len(re.findall(r'\bclass\s+\w+', code)),
        'list_comprehensions': len(re.findall(r'\[.*\bfor\b.*\bin\b.*\]', code)),
        'dict_comprehensions': len(re.findall(r'\{.*\bfor\b.*\bin\b.*\}', code)),
        'lambda_functions': len(re.findall(r'\blambda\b', code)),
        'ternary_operators': len(re.findall(r'\bif\b.*\belse\b', code)),  # inline if-else
        'f_strings': len(re.findall(r'f["\']', code)),
        'docstrings': len(re.findall(r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'', code)),
        'single_line_comments': len(re.findall(r'#.*$', code, re.MULTILINE)),
        'assignments': len(re.findall(r'[^=!<>]=[^=]', code)),
        'comparisons': len(re.findall(r'==|!=|<=|>=|<|>', code)),
        'arithmetic_ops': len(re.findall(r'[+\-*/%]', code)),
    }

    return patterns


def extract_naming_features(code: str) -> Dict[str, float]:
    """Extract variable/function naming style features."""
    # Find all identifiers (variable and function names)
    identifiers = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', code)

    # Filter out keywords and builtins
    identifiers = [i for i in identifiers if i not in PYTHON_KEYWORDS
                   and i not in PYTHON_BUILTINS and len(i) > 1]

    if not identifiers:
        return {
            'avg_identifier_length': 0,
            'snake_case_ratio': 0,
            'camel_case_ratio': 0,
            'single_char_ratio': 0,
            'all_caps_ratio': 0,
        }

    # Classify naming styles
    snake_case = sum(1 for i in identifiers if '_' in i and i.islower())
    camel_case = sum(1 for i in identifiers if re.match(r'^[a-z]+[A-Z]', i))
    single_char = sum(1 for i in identifiers if len(i) == 1)
    all_caps = sum(1 for i in identifiers if i.isupper() and len(i) > 1)

    return {
        'avg_identifier_length': np.mean([len(i) for i in identifiers]),
        'snake_case_ratio': snake_case / len(identifiers),
        'camel_case_ratio': camel_case / len(identifiers),
        'single_char_ratio': single_char / len(identifiers),
        'all_caps_ratio': all_caps / len(identifiers),
        'unique_identifier_ratio': len(set(identifiers)) / len(identifiers),
    }


def extract_all_lexical_features(code: str) -> Dict[str, float]:
    """Extract all lexical features from code."""
    features = {}
    features.update(extract_line_features(code))
    features.update(extract_whitespace_features(code))
    features.update(extract_keyword_features(code))
    features.update(extract_syntax_features(code))
    features.update(extract_naming_features(code))
    return features


def compute_tfidf_features(codes: List[str], max_features: int = 500) -> Tuple[np.ndarray, TfidfVectorizer]:
    """
    Compute TF-IDF features for a list of code snippets.
    Uses code tokens as vocabulary.
    """
    # Custom tokenizer for code
    def code_tokenizer(code):
        # Split on whitespace and common operators
        tokens = re.findall(r'\b\w+\b|[+\-*/%=<>!&|^~]+|[(){}\[\],;:]', code)
        return tokens

    vectorizer = TfidfVectorizer(
        tokenizer=code_tokenizer,
        max_features=max_features,
        ngram_range=(1, 2),  # Unigrams and bigrams
        lowercase=False,
    )

    tfidf_matrix = vectorizer.fit_transform(codes)
    return tfidf_matrix.toarray(), vectorizer


def compute_ngram_features(codes: List[str], n: int = 3, max_features: int = 200) -> Tuple[np.ndarray, CountVectorizer]:
    """Compute character n-gram features."""
    vectorizer = CountVectorizer(
        analyzer='char',
        ngram_range=(n, n),
        max_features=max_features,
    )

    ngram_matrix = vectorizer.fit_transform(codes)
    return ngram_matrix.toarray(), vectorizer


def extract_lexical_features_batch(df: pd.DataFrame, code_column: str = 'code_clean') -> pd.DataFrame:
    """
    Extract lexical features for all code in a DataFrame.

    Returns DataFrame with feature columns.
    """
    feature_records = []

    for idx, row in df.iterrows():
        features = extract_all_lexical_features(row[code_column])
        features['filepath'] = row['filepath']
        feature_records.append(features)

    feature_df = pd.DataFrame(feature_records)

    # Compute TF-IDF
    tfidf_matrix, _ = compute_tfidf_features(df[code_column].tolist())
    tfidf_df = pd.DataFrame(
        tfidf_matrix,
        columns=[f'tfidf_{i}' for i in range(tfidf_matrix.shape[1])]
    )

    # Combine
    result = pd.concat([feature_df.reset_index(drop=True), tfidf_df], axis=1)
    return result


if __name__ == "__main__":
    # Test on a sample
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from src.utils.preprocessing import load_all_generated_code

    df = load_all_generated_code()
    print(f"Loaded {len(df)} files")

    # Extract features for first file
    sample_code = df.iloc[0]['code_clean']
    features = extract_all_lexical_features(sample_code)
    print(f"\nLexical features for first file:")
    for k, v in sorted(features.items()):
        print(f"  {k}: {v:.3f}" if isinstance(v, float) else f"  {k}: {v}")
