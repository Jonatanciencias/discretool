""" Módulo que contiene la función permutations(n, k). """
# src/combinatorics/permutations.py

from math import factorial
from src.utils import validate_non_negative_integers

def permutations(n, k):
    """Calcula el número de permutaciones (nPk)."""
    validate_non_negative_integers(n, k)
    
    if k > n:
        raise ValueError(f"No se puede permutar {k} elementos de un conjunto de {n} elementos.")
    
    return factorial(n) // factorial(n - k)
