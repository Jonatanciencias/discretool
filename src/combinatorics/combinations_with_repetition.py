""" Módulo que contiene la función combinations_with_repetition. """
# src/combinatorics/combinations_with_repetition.py

import math

def combinations_with_repetition(n, k):
    """
    Calcula las combinaciones con repetición (n+k-1)Ck.
    
    Args:
        n (int): El número de elementos en el conjunto.
        k (int): El número de elementos a elegir.
        
    Returns:
        int: El número de combinaciones con repetición.
    """
    if n < 1 or k < 0:
        raise ValueError("n debe ser mayor o igual a 1 y k no puede ser negativo.")
    
    # Usamos la fórmula: (n+k-1)Ck = (n+k-1)! / (k! * (n-1)!)
    return math.comb(n + k - 1, k)
