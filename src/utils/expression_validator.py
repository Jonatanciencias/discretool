from sympy import sympify
from .error_handling import check_common_errors

def validate_expression(expression):
    """
    Valida la expresión lógica, verificando errores comunes.
    """

    # Verificar errores comunes antes de la normalización
    valid, suggestions = check_common_errors(expression)
    if not valid:
        return False, suggestions

    try:
        # Intentar parsear con SymPy
        expr = sympify(expression)
        return True, expr
    except Exception as e:
        return False, [f"Error al procesar la expresión con SymPy: {str(e)}"]