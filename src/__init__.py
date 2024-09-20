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
    simplify_expression,
    classify_expression,
    are_equivalent,
    apply_inference_rules,
    is_satisfiable
)

# Importar reglas de inferencia y equivalencia lógica
from .logic.inference_rules import (
    de_morgan,
    idempotence,
    absorption,
    distribution
)

from .logic.equivalence_solver import (
    check_equivalence,
    apply_rules
)

# Importar herramientas comunes para cálculos matemáticos
from .common_tools import (
    gcd,
    lcm,
    generate_primes,
    is_congruent,
    solve_linear_congruence,
    solve_diophantine
)

# Importar utilidades
from .utils import (
    print_welcome_message,
    replace_implication,
    normalize_expression
    )
