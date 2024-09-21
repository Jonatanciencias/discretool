
""" Inference rules for logical expressions. """
import sympy

def de_morgan(expr):
    """Aplica la ley de De Morgan si es posible."""
    if isinstance(expr, sympy.Not):
        sub_expr = expr.args[0]
        if isinstance(sub_expr, sympy.And):
            return sympy.Or(sympy.Not(sub_expr.args[0]), sympy.Not(sub_expr.args[1]))
        elif isinstance(sub_expr, sympy.Or):
            return sympy.And(sympy.Not(sub_expr.args[0]), sympy.Not(sub_expr.args[1]))
    return expr

def idempotence(expr):
    """Aplica la ley de idempotencia: A & A -> A, A | A -> A"""
    if isinstance(expr, sympy.And) and expr.args[0] == expr.args[1]:
        return expr.args[0]
    elif isinstance(expr, sympy.Or) and expr.args[0] == expr.args[1]:
        return expr.args[0]
    return expr

def absorption(expr):
    """Aplica la ley de absorción: A & (A | B) -> A"""
    if isinstance(expr, sympy.And):
        if isinstance(expr.args[1], sympy.Or) and expr.args[0] == expr.args[1].args[0]:
            return expr.args[0]
        elif isinstance(expr.args[0], sympy.Or) and expr.args[1] == expr.args[0].args[0]:
            return expr.args[1]
    return expr

def distribution(expr):
    """Aplica la ley de distribución: A & (B | C) -> (A & B) | (A & C)"""
    if isinstance(expr, sympy.And):
        if isinstance(expr.args[1], sympy.Or):
            return sympy.Or(sympy.And(expr.args[0], expr.args[1].args[0]), sympy.And(expr.args[0], expr.args[1].args[1]))
    elif isinstance(expr, sympy.Or):
        if isinstance(expr.args[1], sympy.And):
            return sympy.And(sympy.Or(expr.args[0], expr.args[1].args[0]), sympy.Or(expr.args[0], expr.args[1].args[1]))
    return expr