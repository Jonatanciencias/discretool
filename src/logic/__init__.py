""" logic module """
# src/logic/__init__.py

from .logic_solver import (
    parse_expression,
    evaluate_expression,
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
    is_satisfiable  # Solo importar desde sat_solver
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

from .truth_table import truth_table, export_truth_table_csv, export_truth_table_md

__all__ = [
    "parse_expression",
    "evaluate_expression",
    "truth_table",
    "apply_inference_rules",
    "modus_ponens",
    "modus_tollens",
    "disjunctive_syllogism",
    "hypothetical_syllogism",
    "double_negation",
    "is_satisfiable", 
    "de_morgan",
    "idempotence",
    "absorption",
    "distribution",
    "analyze_complexity",
]
