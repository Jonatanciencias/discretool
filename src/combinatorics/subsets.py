""" Módulo que contiene funciones para generar todos 
los subconjuntos posibles de un conjunto de tamaño n. 
"""
# src/combinatorics/subsets.py

from itertools import chain, combinations
from src.utils import validate_non_negative_integers

def generate_subsets(n):
    """
    Genera todos los subconjuntos posibles de un conjunto de tamaño n.
    
    Args:
        n (int): Tamaño del conjunto.

    Returns:
        list: Lista de subconjuntos.
    """
    validate_non_negative_integers(n)
    
    # Generamos el conjunto {0, 1, ..., n-1}
    elements = list(range(n))
    
    # Usamos itertools para generar todas las combinaciones de distintos tamaños
    subsets = list(chain.from_iterable(combinations(elements, r) for r in range(n + 1)))
    
    return subsets
