def normalize_expression(expression):
    """
    Normaliza la notación de la expresión para que SymPy pueda entenderla.
    Transforma notaciones alternativas de operadores lógicos (como ∧, ∨, and, or)
    en notación estándar (&, |), y maneja casos especiales como la presencia de rutas de archivo.
    Realiza hasta dos ciclos de verificación para corregir la expresión.
    """

    def clean_expression(expr):
        # Eliminar posibles rutas de Windows malinterpretadas
        expr = expr.replace("\\", "")

        # Reemplazar conjunciones (and, ∧) por &
        expr = expr.replace('∧', '&').replace('and', '&')

        # Reemplazar disyunciones (or, ∨) por |
        expr = expr.replace('∨', '|').replace('or', '|')

        # Reemplazar implicaciones por >>
        expr = expr.replace('→', '>>').replace('->', '>>')

        # Reemplazar bicondicional (↔, <->) por ==
        expr = expr.replace('↔', '==').replace('<->', '==')

        # Reemplazar negación (¬, not) por ~
        expr = expr.replace('¬', '~').replace('not', '~')

        # Eliminar cualquier referencia a rutas de archivo comunes
        expr = expr.replace('C:Users', '')

        # Eliminar posibles espacios innecesarios
        return expr.strip()

    # Ciclo 1 de normalización
    expression = clean_expression(expression)
    
    # Verificación de errores comunes después del primer ciclo
    if "C:\\" in expression or "C:Users" in expression:
        # Si encontramos errores relacionados con rutas, intentamos limpiarlo una vez más
        expression = clean_expression(expression)
        
        # Verificar después del segundo ciclo
        if "C:\\" in expression or "C:Users" in expression:
            print(f"Error: No se pudo corregir la expresión. Posible referencia a una ruta: {expression}")
            raise ValueError("Error: Se ha detectado una ruta de archivo en la expresión y no se pudo corregir automáticamente.")
        else:
            print("Advertencia: Se detectó una posible ruta de archivo pero se corrigió en el segundo ciclo.")
    else:
        print(f"Expresión normalizada correctamente: {expression}")

    return expression

