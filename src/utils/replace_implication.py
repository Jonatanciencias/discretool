"""Reemplaza '->' por '>>' en las expresiones lógicas, que SymPy reconoce como Implies."""
# src/utils.py

def replace_implication(expression):
    """Reemplaza '->' por '>>' en las expresiones lógicas, que SymPy reconoce como Implies."""
    return expression.replace('->', '>>')
