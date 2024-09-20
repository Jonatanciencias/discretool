""" Normaliza la notación de la expresión para que SymPy pueda entenderla. """
# src/utils/normalize_expression.py

def normalize_expression(expression):
    """
    Normaliza la notación de la expresión para que SymPy pueda entenderla.
    
    Transforma notaciones alternativas de operadores lógicos (como ∧, ∨, and, or) 
    en notación estándar (&, |).
    """
     # Agregar logs o prints si es necesario para verificar la normalización
    expression = expression.replace('∧', '&').replace('and', '&')
    expression = expression.replace('∨', '|').replace('or', '|')
    expression = expression.replace('→', '>>').replace('->', '>>')
    expression = expression.replace('↔', '==').replace('<->', '==')
    expression = expression.replace('¬', '~').replace('not', '~') 
    return expression
