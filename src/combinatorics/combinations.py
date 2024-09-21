""" Módulo que contiene la función combinations(n, k). """
# src/combinatorics/combinations.py

from math import factorial
from src.utils.error_handling import validate_non_negative_integers

def combinations(n, k):
    """Calcula el número de combinaciones (nCk)."""
    validate_non_negative_integers(n, k)
    
    if k > n:
        raise ValueError(f"No se puede elegir {k} elementos de un conjunto de {n} elementos.")
    
    return factorial(n) // (factorial(k) * factorial(n - k))
