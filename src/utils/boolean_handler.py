from sympy import Basic

def handle_boolean_expression(expr):
    """
    Procesa una expresión lógica que resulta en un valor booleano o simbólico.
    
    Args:
        expr: Expresión lógica evaluada.
    
    Returns:
        El valor booleano directamente si es True o False,
        o la expresión simbólica si no es booleana.
    """
    if isinstance(expr, bool):
        print("DEBUG: Expresión evaluada como booleana:", expr)
        return expr
    elif isinstance(expr, Basic):  # Verifica si es simbólica
        print("DEBUG: Expresión simbólica detectada:", expr)
        return expr
    else:
        print("DEBUG: Error, expresión inválida:", expr)
        raise ValueError("Expresión no es ni booleana ni simbólica válida")
