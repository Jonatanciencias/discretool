""" Módulo que contiene la función multinomial. """
# src/combinatorics/multinomial.py

from math import factorial
from src.utils import validate_non_negative_integers

def multinomial(n, *groups):
    """
    Calcula el coeficiente multinomial para n objetos distribuidos en grupos.
    
    Args:
        n (int): Número total de objetos.
        groups (int): Tamaño de cada grupo.
    
    Returns:
        int: El coeficiente multinomial.
    """
    # Validamos que todos los argumentos sean enteros no negativos
    validate_non_negative_integers(n, *groups)
    
    if sum(groups) != n:
        raise ValueError(f"La suma de los grupos {groups} debe ser igual a {n}")
    
    numerator = factorial(n)
    denominator = 1
    for group_size in groups:
        denominator *= factorial(group_size)
    
    return numerator // denominator
