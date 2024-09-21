def check_common_errors(expression):
    """
    Revisa la expresión en busca de errores comunes y sugiere correcciones.
    
    Esta función devuelve un booleano indicando si la expresión es válida 
    y una lista de sugerencias de correcciones si se detectan errores comunes.
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
    invalid_chars = set(expression) - set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789¬~&|∨∧()=><-> ")
    if invalid_chars:
        suggestions.append(f"Elimina o corrige caracteres no válidos: {', '.join(invalid_chars)}")

    # Si hay errores, devolver sugerencias
    if suggestions:
        return False, suggestions
    else:
        return True, []

def validate_expression(expression):
    """
    Valida una expresión completa llamando a múltiples verificaciones.
    
    Combina la verificación de errores comunes y otras comprobaciones necesarias
    para garantizar que la expresión sea válida antes de su procesamiento.
    """
    # Realizar las verificaciones de errores comunes
    valid, feedback = check_common_errors(expression)
    if not valid:
        return False, feedback

    # Agregar más validaciones si es necesario, como reglas de dominio específicas
    return True, feedback