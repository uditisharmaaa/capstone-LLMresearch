"""
Preprocessing utilities for loading and cleaning generated code.
"""
import os
import re
import ast
import pandas as pd
from pathlib import Path
from typing import Dict, List, Tuple, Optional


def strip_provenance_header(code: str) -> str:
    """Remove the provenance comment header from generated code."""
    lines = code.split('\n')

    # Find the end of the provenance header (line with just '# ===...')
    header_end = 0
    in_header = False

    for i, line in enumerate(lines):
        if line.startswith('# ====') and 'PROVENANCE' in lines[i+1] if i+1 < len(lines) else False:
            in_header = True
        if in_header and line.startswith('# ====') and i > 0:
            # Check if this is the closing line
            if i > 5:  # We're past the opening
                header_end = i + 1
                break

    # If we found a header, skip it
    if header_end > 0:
        # Skip empty lines after header
        while header_end < len(lines) and lines[header_end].strip() == '':
            header_end += 1
        return '\n'.join(lines[header_end:])

    return code


def strip_comments(code: str) -> str:
    """Remove all comments from Python code."""
    # Remove single-line comments
    code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)
    # Remove docstrings (triple quotes)
    code = re.sub(r'"""[\s\S]*?"""', '', code)
    code = re.sub(r"'''[\s\S]*?'''", '', code)
    # Remove empty lines
    lines = [line for line in code.split('\n') if line.strip()]
    return '\n'.join(lines)


def is_valid_python(code: str) -> bool:
    """Check if code is syntactically valid Python."""
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False


def load_code_file(filepath: str, strip_header: bool = True) -> str:
    """Load a Python file and optionally strip the provenance header."""
    with open(filepath, 'r') as f:
        code = f.read()

    if strip_header:
        code = strip_provenance_header(code)

    return code


def load_all_generated_code(data_dir: str = "data/raw") -> pd.DataFrame:
    """
    Load all generated code files into a DataFrame.

    Returns DataFrame with columns:
        - filepath: path to the file
        - filename: just the filename
        - model: model used (gpt4o, gpt4mini, sonnet)
        - style_index: style variation index
        - code_raw: full code including header
        - code_clean: code without header
        - code_no_comments: code without comments
        - is_valid: whether code parses
        - line_count: number of lines
        - char_count: number of characters
    """
    records = []

    for model_dir in ['gpt4o', 'gpt4mini', 'sonnet', 'gemini', 'llama', 'opus']:
        dir_path = Path(data_dir) / model_dir
        if not dir_path.exists():
            continue

        for filepath in sorted(dir_path.glob("*.py")):
            # Parse filename: gen_0001_gpt4o_01.py
            parts = filepath.stem.split('_')
            if len(parts) >= 4:
                gen_id = int(parts[1])
                model = parts[2]
                style_idx = int(parts[3])
            else:
                continue

            code_raw = filepath.read_text()
            code_clean = strip_provenance_header(code_raw)
            code_no_comments = strip_comments(code_clean)

            records.append({
                'filepath': str(filepath),
                'filename': filepath.name,
                'generation_id': gen_id,
                'model': model,
                'style_index': style_idx,
                'code_raw': code_raw,
                'code_clean': code_clean,
                'code_no_comments': code_no_comments,
                'is_valid': is_valid_python(code_clean),
                'line_count': len(code_clean.split('\n')),
                'char_count': len(code_clean),
            })

    return pd.DataFrame(records)


def get_code_stats(df: pd.DataFrame) -> Dict:
    """Get summary statistics for loaded code."""
    return {
        'total_files': len(df),
        'valid_files': df['is_valid'].sum(),
        'by_model': df.groupby('model').size().to_dict(),
        'avg_lines': df['line_count'].mean(),
        'avg_chars': df['char_count'].mean(),
        'min_lines': df['line_count'].min(),
        'max_lines': df['line_count'].max(),
    }


if __name__ == "__main__":
    # Test loading
    df = load_all_generated_code()
    print(f"Loaded {len(df)} code files")
    print(f"\nStats: {get_code_stats(df)}")
    print(f"\nSample code (first 500 chars):\n{df.iloc[0]['code_clean'][:500]}")
