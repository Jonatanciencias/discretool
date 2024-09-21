""" Módulo que se encarga de validar la expresión lógica ingresada por el usuario. """
# src/utils/expression_validator.py

from sympy import sympify
from sympy.core.sympify import SympifyError
from .error_handling import check_common_errors

def validate_expression(expression):
    """
    Valida la expresión lógica y devuelve errores amigables si algo falla.
    """
    # Paso 1: Verificar errores comunes
    valid, suggestions = check_common_errors(expression)
    
    if not valid:
        return False, suggestions

    # Paso 2: Intentar parsear la expresión con SymPy
    try:
        expr = sympify(expression)
        return True, expr
    except SympifyError as e:
        return False, [f"Error al procesar la expresión: {str(e)}"]
