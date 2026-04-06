"""
Structural feature extraction using Abstract Syntax Trees (AST).
Captures program structure independent of naming and formatting.
"""
import ast
import numpy as np
import pandas as pd
from collections import Counter
from typing import Dict, List, Optional, Any
from pathlib import Path


# AST node types to track
AST_NODE_TYPES = [
    'FunctionDef', 'AsyncFunctionDef', 'ClassDef', 'Return', 'Delete',
    'Assign', 'AugAssign', 'AnnAssign', 'For', 'AsyncFor', 'While',
    'If', 'With', 'AsyncWith', 'Raise', 'Try', 'Assert', 'Import',
    'ImportFrom', 'Global', 'Nonlocal', 'Expr', 'Pass', 'Break', 'Continue',
    'BoolOp', 'BinOp', 'UnaryOp', 'Lambda', 'IfExp', 'Dict', 'Set',
    'ListComp', 'SetComp', 'DictComp', 'GeneratorExp', 'Await', 'Yield',
    'YieldFrom', 'Compare', 'Call', 'FormattedValue', 'JoinedStr',
    'Constant', 'Attribute', 'Subscript', 'Starred', 'Name', 'List',
    'Tuple', 'Slice',
]


class ASTFeatureExtractor(ast.NodeVisitor):
    """Visitor to extract features from AST."""

    def __init__(self):
        self.node_counts = Counter()
        self.max_depth = 0
        self.current_depth = 0
        self.function_count = 0
        self.class_count = 0
        self.loop_count = 0
        self.condition_count = 0
        self.try_count = 0
        self.return_count = 0
        self.call_count = 0
        self.nesting_depths = []

    def generic_visit(self, node):
        """Visit a node and track depth."""
        self.current_depth += 1
        self.max_depth = max(self.max_depth, self.current_depth)

        node_type = type(node).__name__
        self.node_counts[node_type] += 1

        # Track specific constructs
        if node_type == 'FunctionDef':
            self.function_count += 1
            self.nesting_depths.append(self.current_depth)
        elif node_type == 'ClassDef':
            self.class_count += 1
        elif node_type in ('For', 'While', 'AsyncFor'):
            self.loop_count += 1
            self.nesting_depths.append(self.current_depth)
        elif node_type == 'If':
            self.condition_count += 1
        elif node_type == 'Try':
            self.try_count += 1
        elif node_type == 'Return':
            self.return_count += 1
        elif node_type == 'Call':
            self.call_count += 1

        # Visit children
        for child in ast.iter_child_nodes(node):
            self.visit(child)

        self.current_depth -= 1


def extract_ast_features(code: str) -> Dict[str, float]:
    """Extract AST-based structural features from code."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        # Return zeros for invalid code
        return {f'ast_{name.lower()}': 0 for name in AST_NODE_TYPES}

    extractor = ASTFeatureExtractor()
    extractor.visit(tree)

    features = {
        'ast_max_depth': extractor.max_depth,
        'ast_total_nodes': sum(extractor.node_counts.values()),
        'ast_unique_node_types': len(extractor.node_counts),
        'ast_function_count': extractor.function_count,
        'ast_class_count': extractor.class_count,
        'ast_loop_count': extractor.loop_count,
        'ast_condition_count': extractor.condition_count,
        'ast_try_count': extractor.try_count,
        'ast_return_count': extractor.return_count,
        'ast_call_count': extractor.call_count,
        'ast_avg_nesting': np.mean(extractor.nesting_depths) if extractor.nesting_depths else 0,
    }

    # Add normalized counts for each node type
    total_nodes = max(sum(extractor.node_counts.values()), 1)
    for node_type in AST_NODE_TYPES:
        features[f'ast_{node_type.lower()}_ratio'] = extractor.node_counts.get(node_type, 0) / total_nodes

    return features


def get_ast_node_sequence(code: str) -> List[str]:
    """Get the sequence of AST node types (for sequence-based comparison)."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []

    sequence = []
    for node in ast.walk(tree):
        sequence.append(type(node).__name__)
    return sequence


def get_control_flow_pattern(code: str) -> str:
    """
    Extract a simplified control flow pattern string.
    Useful for comparing structural similarity.
    """
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return ""

    patterns = []

    class ControlFlowVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            patterns.append('F')  # Function
            self.generic_visit(node)

        def visit_For(self, node):
            patterns.append('[')  # Loop start
            self.generic_visit(node)
            patterns.append(']')  # Loop end

        def visit_While(self, node):
            patterns.append('(')  # While start
            self.generic_visit(node)
            patterns.append(')')  # While end

        def visit_If(self, node):
            patterns.append('?')  # Condition
            self.generic_visit(node)

        def visit_Return(self, node):
            patterns.append('R')  # Return
            self.generic_visit(node)

        def visit_Try(self, node):
            patterns.append('T')  # Try
            self.generic_visit(node)

    ControlFlowVisitor().visit(tree)
    return ''.join(patterns)


def compute_cyclomatic_complexity(code: str) -> int:
    """
    Compute cyclomatic complexity (simplified).
    CC = E - N + 2P where E=edges, N=nodes, P=connected components
    Simplified: CC = 1 + number of decision points
    """
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return 0

    complexity = 1  # Base complexity

    for node in ast.walk(tree):
        # Decision points add to complexity
        if isinstance(node, (ast.If, ast.While, ast.For, ast.AsyncFor)):
            complexity += 1
        elif isinstance(node, ast.BoolOp):
            # and/or add complexity
            complexity += len(node.values) - 1
        elif isinstance(node, ast.Try):
            # Each except handler adds complexity
            complexity += len(node.handlers)
        elif isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            # Comprehensions with conditions
            for generator in node.generators:
                complexity += len(generator.ifs)

    return complexity


def extract_function_signatures(code: str) -> List[Dict[str, Any]]:
    """Extract function signature information."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []

    signatures = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            sig = {
                'name': node.name,
                'num_args': len(node.args.args),
                'has_defaults': len(node.args.defaults) > 0,
                'has_vararg': node.args.vararg is not None,
                'has_kwargs': node.args.kwarg is not None,
                'has_return_annotation': node.returns is not None,
                'body_size': len(node.body),
            }
            signatures.append(sig)

    return signatures


def extract_structural_features_batch(df: pd.DataFrame, code_column: str = 'code_clean') -> pd.DataFrame:
    """Extract structural features for all code in a DataFrame."""
    feature_records = []

    for idx, row in df.iterrows():
        code = row[code_column]

        features = extract_ast_features(code)
        features['filepath'] = row['filepath']
        features['cyclomatic_complexity'] = compute_cyclomatic_complexity(code)
        features['control_flow_pattern'] = get_control_flow_pattern(code)
        features['control_flow_length'] = len(features['control_flow_pattern'])

        # Function-level features
        signatures = extract_function_signatures(code)
        features['num_functions'] = len(signatures)
        features['avg_function_args'] = np.mean([s['num_args'] for s in signatures]) if signatures else 0
        features['avg_function_body_size'] = np.mean([s['body_size'] for s in signatures]) if signatures else 0

        feature_records.append(features)

    return pd.DataFrame(feature_records)


if __name__ == "__main__":
    # Test on a sample
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from src.utils.preprocessing import load_all_generated_code

    df = load_all_generated_code()
    print(f"Loaded {len(df)} files")

    # Extract features for first file
    sample_code = df.iloc[0]['code_clean']
    features = extract_ast_features(sample_code)
    print(f"\nAST features for first file:")
    for k, v in sorted(features.items())[:20]:
        print(f"  {k}: {v:.3f}" if isinstance(v, float) else f"  {k}: {v}")

    print(f"\nControl flow pattern: {get_control_flow_pattern(sample_code)}")
    print(f"Cyclomatic complexity: {compute_cyclomatic_complexity(sample_code)}")
