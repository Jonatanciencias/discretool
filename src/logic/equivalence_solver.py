"""Módulo para resolver equivalencias lógicas paso a paso."""
# src/logic/equivalence_solver.py

from sympy import simplify, Equivalent, sympify
from .inference_rules import de_morgan, idempotence, absorption, distribution

# Lista de reglas disponibles
RULES = [
    ("De Morgan", de_morgan),
    ("Idempotence", idempotence),
    ("Absorption", absorption),
    ("Distribution", distribution),
]

def apply_rules(expr):
    """Aplica reglas de inferencia lógicas paso a paso hasta que no haya más cambios."""
    steps = [(str(expr), "Original expression")]
    
    changed = True
    while changed:
        changed = False
        for rule_name, rule in RULES:
            new_expr = rule(expr)
            if new_expr != expr:
                steps.append((str(new_expr), rule_name))
                expr = new_expr
                changed = True
                break  # Aplicamos una regla a la vez
    return steps

def check_equivalence(expr1, expr2):
    """Aplica reglas de inferencia a expr1 hasta llegar a una equivalencia con expr2, si es posible."""
    # Convertir las expresiones de cadenas a expresiones simbólicas
    expr1 = sympify(expr1)
    expr2 = sympify(expr2)
    
    simplified_expr1 = simplify(expr1)
    simplified_expr2 = simplify(expr2)
    
    if Equivalent(simplified_expr1, simplified_expr2):
        return True, apply_rules(expr1)
    return False, []
