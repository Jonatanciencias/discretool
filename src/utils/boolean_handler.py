def handle_boolean_expression(expr):
    """
    Procesa una expresión lógica que resulta en un valor booleano.
    
    Args:
        expr: Expresión lógica evaluada.
    
    Returns:
        El valor booleano directamente si es True o False.
    """
    if isinstance(expr, bool):
        return expr
    elif expr == True:
        return True
    elif expr == False:
        return False
    else:
        raise ValueError("Expresión no es booleano o no puede ser procesada")
