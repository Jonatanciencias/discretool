"""Módulo para analizar la complejidad de expresiones lógicas."""
# src/logic/complexity_analysis.py

import sympy
from sympy.logic.boolalg import BooleanFunction

def count_operations(expr):
    """Cuenta el número de operaciones lógicas en la expresión."""
    if not isinstance(expr, BooleanFunction):
        return 0
    return 1 + sum(count_operations(arg) for arg in expr.args)

def count_variables(expr):
    """Cuenta el número de variables únicas en la expresión."""
    return len(expr.free_symbols)

def analyze_complexity(expr):
    """
    Analiza la complejidad de la expresión lógica.
    
    Retorna:
    - Número de operaciones lógicas.
    - Número de variables.
    """
    # Convierte la cadena a una expresión de SymPy
    expr = sympy.sympify(expr)
    
    num_operations = count_operations(expr)
    num_variables = count_variables(expr)
    
    return num_operations, num_variables
