""" logic module"""
# src/logic/__init__.py

from .logic_solver import (
    parse_expression,
    evaluate_expression,
    truth_table,
    simplify_expression,
    classify_expression,
    are_equivalent,
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

from .sat_solver import (
    is_satisfiable
)

from .equivalence_solver import (
    check_equivalence
)

from .inference_rules import (
    de_morgan,
    idempotence,
    absorption,
    distribution
)

from .complexity_analysis import (
    analyze_complexity
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
    "double_negation",
    "is_satisfiable",
    "check_equivalence",
    "de_morgan",
    "idempotence",
    "absorption",
    "distribution",
    "analyze_complexity"
]
