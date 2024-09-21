""" Valida que todos los argumentos sean enteros no negativos. """
# src/utils/vlidate_non_negative_integers.py

def validate_non_negative_integers(*args):
    """
    Valida que todos los argumentos sean enteros no negativos.
    
    Si algún argumento no es un entero no negativo, lanza un ValueError.
    """
    for arg in args:
        if not isinstance(arg, int) or arg < 0:
            raise ValueError(f"{arg} debe ser un entero no negativo.")
