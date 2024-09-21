import re

def check_common_errors(expression):
    """
    Revisa la expresión en busca de errores comunes y sugiere correcciones.
    
    Devuelve:
    - (bool, list): Si la expresión es válida o no y una lista de sugerencias de correcciones si se detectan errores comunes.
    """
    suggestions = []

    # Error común 1: Uso incorrecto de implicaciones o bicondicionales
    if "=>" in expression or "<=>" in expression:
        suggestions.append("Reemplaza '=>' con '->' para implicaciones.")
        suggestions.append("Reemplaza '<=>' con '<->' para bicondicionales.")

    # Error común 2: Uso de operadores lógicos no estándar
    if "&&" in expression or "||" in expression:
        suggestions.append("Utiliza 'and' o '∧' para conjunción y 'or' o '∨' para disyunción.")

    if "AND" in expression or "OR" in expression:
        suggestions.append("Utiliza 'and' o '∧' para conjunción y 'or' o '∨' para disyunción.")

    # Error común 3: Uso incorrecto de negaciones
    if "NOT" in expression:
        suggestions.append("Reemplaza 'NOT' con '¬' o '~' para negación.")

    if "!" in expression:
        suggestions.append("Utiliza '¬' o '~' para negación en lugar de '!'.")

    # Error común 4: Paréntesis desbalanceados
    open_parentheses = expression.count("(")
    close_parentheses = expression.count(")")
    if open_parentheses != close_parentheses:
        suggestions.append("Verifica los paréntesis, parecen estar desbalanceados.")

    # Error común 5: Caracteres no válidos o símbolos extraños
    valid_chars_pattern = r"^[A-Za-z0-9¬~&|∨∧()=><-> ]+$"
    if not re.match(valid_chars_pattern, expression):
        invalid_chars = set(expression) - set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789¬~&|∨∧()=><-> ")
        suggestions.append(f"Elimina o corrige caracteres no válidos: {', '.join(invalid_chars)}")

    # Si hay errores, devolver sugerencias
    if suggestions:
        return False, suggestions
    else:
        return True, []


def handle_sympy_error(expression, attempt_normalization=True):
    """
    Maneja los errores provenientes de SymPy al procesar la expresión.
    
    - Realiza un reintento de normalización y validación si se habilita `attempt_normalization`.
    - Si después de los reintentos no se resuelve, devuelve un mensaje de error claro.
    
    Args:
    expression (str): La expresión original que causó el error.
    attempt_normalization (bool): Si se debe intentar normalizar la expresión nuevamente.
    
    Devuelve:
    - Un mensaje de error detallado.
    """
    try:
        if attempt_normalization:
            # Intentar normalización y validación nuevamente
            print("Intentando normalizar y validar la expresión nuevamente...")
            from src.utils.normalize_expression import normalize_expression
            from src.utils.expression_validator import validate_expression
            
            normalized_expression = normalize_expression(expression)
            valid, feedback = validate_expression(normalized_expression)
            
            if not valid:
                return (False, f"Errores encontrados después de la normalización: {feedback}")
            else:
                return (True, f"Expresión normalizada y validada correctamente: {normalized_expression}")
        else:
            return (False, "Error al procesar la expresión con SymPy.")
    
    except Exception as e:
        return (False, f"Error inesperado durante la normalización: {str(e)}")


def validate_expression(expression):
    """
    Valida una expresión lógica llamando a múltiples verificaciones, incluyendo la corrección de errores comunes.
    
    Devuelve:
    - (bool, list): Si la expresión es válida o no y los mensajes de error o la expresión corregida.
    """
    # Paso 1: Verificar errores comunes en la notación
    valid, suggestions = check_common_errors(expression)
    
    if not valid:
        return False, suggestions

    # Paso 2: Verificaciones adicionales si es necesario, como paréntesis o símbolos de operadores
    return True, []


def raise_sympy_exception(error):
    """
    Maneja excepciones específicas relacionadas con el uso de SymPy para que los errores sean más comprensibles.
    
    Args:
    - error: La excepción levantada por SymPy.
    
    Devuelve:
    - Un mensaje de error más claro relacionado con el problema específico.
    """
    if "could not parse" in str(error):
        return "Error de sintaxis en la expresión. Verifica la estructura de la misma."
    return f"Error inesperado: {str(error)}"
