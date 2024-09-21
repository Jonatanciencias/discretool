""" Módulo con funciones para manejar errores comunes en expresiones lógicas. """
# src/utils/error_handling.py

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
