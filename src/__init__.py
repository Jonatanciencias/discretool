"""
Paquete principal de DiscreTool.

Este paquete contiene los módulos necesarios para realizar 
cálculos y operaciones relacionados con matemáticas discretas.
Incluye módulos para lógica proposicional, herramientas comunes, 
combinatoria, grafos, y utilidades adicionales.
"""
# src/__init__.py

# Importar módulos de lógica proposicional
from .logic import (
    parse_expression,
    evaluate_expression,
    truth_table,
    apply_inference_rules,
    is_satisfiable,
    check_equivalence,
)

# Importar reglas de inferencia y equivalencia lógica
from .logic.inference_rules import de_morgan, idempotence, absorption, distribution

# Importar herramientas comunes para cálculos matemáticos
from .common_tools import (
    gcd,
    lcm,
    generate_primes,
    is_congruent,
    solve_linear_congruence,
    solve_diophantine,
)

# Importar utilidades
from .utils import (
    print_welcome_message,
    normalize_expression,
    validate_expression,
    export_to_csv,   # Función actualizada
    export_to_md,    # Función actualizada
    visualize_truth_table,
    check_common_errors,
    handle_boolean_expression
)


# Futuras expansiones para combinatoria, grafos y recursión
# from .combinatorics import (
#     combinations,
#     permutations,
# )
#
# from .graphs import (
#     find_shortest_path,
#     detect_cycle,
# )
#
# from .recursion import (
#     factorial_recursive,
#     fibonacci_recursive,
# )

__all__ = [
    # Lógica proposicional
    "parse_expression",
    "evaluate_expression",
    "truth_table",
    "apply_inference_rules",
    "is_satisfiable",
    "check_equivalence",
    # Reglas de inferencia
    "de_morgan",
    "idempotence",
    "absorption",
    "distribution",
    # Herramientas comunes
    "gcd",
    "lcm",
    "generate_primes",
    "is_congruent",
    "solve_linear_congruence",
    "solve_diophantine",
    # Utilidades
    "print_welcome_message",
    "normalize_expression",
    "validate_expression",
    "export_to_csv",   # Función actualizada
    "export_to_md",    # Función actualizada
    "visualize_truth_table",
    "check_common_errors",
    "handle_boolean_expression",
]
