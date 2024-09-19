# src/__init__.py

"""
Paquete principal de DiscreTool.

Este paquete incluye:
- Módulo `logic` para operaciones de lógica proposicional.
- Módulo `common_tools` para herramientas comunes en matemáticas discretas.
- Utilidades adicionales en `utils`.
"""

from .logic import (
    parse_expression,
    evaluate_expression,
    truth_table,
    simplify_expression,
    classify_expression,
    are_equivalent,
)

from .common_tools import (
    gcd,
    lcm,
    generate_primes,
)

from .utils import (
    print_welcome_message,
    replace_implication
)

config = {
    "version": "1.0.0",
    "author": "Jonatan García"
}
