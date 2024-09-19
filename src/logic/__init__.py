# src/logic/__init__.py

from .logic_solver import (
    parse_expression,
    evaluate_expression,
    truth_table,
    simplify_expression,
    classify_expression,
    are_equivalent
)

from .derivation import (
    apply_inference_rules
)
from .inference import (
    modus_ponens,
    modus_tollens,
    disjunctive_syllogism,
    hypothetical_syllogism,
    double_negation
)

__all__ = [
    "parse_expression",
    "evaluate_expression",
    "truth_table",
    "simplify_expression",
    "classify_expression",
    "are_equivalent",
    "apply_inference_rules",
    "modus_ponens",
    "modus_tollens",
    "disjunctive_syllogism",
    "hypothetical_syllogism",
    "double_negation"
    
]
