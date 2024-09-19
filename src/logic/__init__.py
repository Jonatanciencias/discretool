# src/logic/__init__.py
from .logic_solver import (
    parse_expression,
    evaluate_expression,
    truth_table,
    simplify_expression,
    classify_expression,
    are_equivalent
)

__all__ = [
    "parse_expression",
    "evaluate_expression",
    "truth_table",
    "simplify_expression",
    "classify_expression",
    "are_equivalent"
]
