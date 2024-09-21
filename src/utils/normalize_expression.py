import re

def normalize_expression(expression):
    """
    Normaliza la notación de la expresión para que SymPy pueda entenderla.
    Solo transforma los operadores y limpia la sintaxis, sin hacer cambios a la lógica de la expresión.
    """

    def clean_expression(expr):
        # Transformaciones de operadores
        expr = re.sub(r'\b(and|∧)\b', ' & ', expr)
        expr = re.sub(r'\b(or|∨)\b', ' | ', expr)
        expr = re.sub(r'(→|->)', ' >> ', expr)
        expr = re.sub(r'(↔|<->)', ' == ', expr)
        expr = re.sub(r'\b(not|¬)\b', ' ~ ', expr)

        # Limpieza de dobles espacios y caracteres no válidos
        expr = re.sub(r'\s+', ' ', expr)
        expr = re.sub(r'[^A-Za-z0-9~&|!=><() ]', '', expr)

        # Corrección de variables consecutivas sin operadores
        expr = re.sub(r'([A-Za-z0-9])\s+([A-Za-z0-9])', r'\1 & \2', expr)
        
        return expr.strip()

    expression = clean_expression(expression)

    # Si se detectan rutas de archivo o errores comunes, se intenta limpiar
    if re.search(r"C:\\|C:Users", expression):
        expression = clean_expression(expression)
        if re.search(r"C:\\|C:Users", expression):
            raise ValueError("Error: Se ha detectado una ruta de archivo en la expresión.")
    else:
        print(f"Expresión normalizada correctamente: {expression}")

    return expression
