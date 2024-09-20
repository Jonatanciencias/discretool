""" Módulo con funciones para manejar errores comunes en expresiones lógicas. """
# src/utils/error_handling.py

def check_common_errors(expression):
    """
    Revisa la expresión en busca de errores comunes y sugiere correcciones.
    """
    suggestions = []

    # Error común 1: Uso incorrecto de implicaciones o bicondicionales
    if "=>" in expression or "<=>" in expression:
        suggestions.append("Reemplaza '=>' con '->' para implicaciones.")
        suggestions.append("Reemplaza '<=>' con '<->' para bicondicionales.")

    # Error común 2: Uso de operadores lógicos no estándar
    if "AND" in expression or "OR" in expression:
        suggestions.append("Utiliza 'and' o '∧' para conjunción y 'or' o '∨' para disyunción.")

    # Error común 3: Uso incorrecto de negaciones
    if "NOT" in expression:
        suggestions.append("Reemplaza 'NOT' con '¬' o '~' para negación.")

    # Si hay errores, devolver sugerencias
    if suggestions:
        return False, suggestions
    else:
        return True, []
