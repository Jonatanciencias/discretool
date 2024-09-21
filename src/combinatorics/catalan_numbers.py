""" Módulo que contiene la implementación de la función que calcula el número de Catalan. """
# src/combinatorics/catalan_numbers.py

from math import factorial

def catalan_number(n):
    """
    Calcula el número de Catalan.
    
    Args:
        n (int): Índice del número de Catalan.
    
    Returns:
        int: El número de Catalan.
    """
    return factorial(2 * n) // (factorial(n + 1) * factorial(n))
