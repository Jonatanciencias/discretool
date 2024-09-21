"""Módulo que contiene las funciones permutations(n, k), circular_permutations(n), y generalized_binomial(x, k)."""
# src/combinatorics/permutations.py

from math import factorial
from src.utils.validate_non_negative_integers import validate_non_negative_integers

def permutations(n, k):
    """
    Calcula el número de permutaciones (nPk).

    Args:
        n (int): Número total de elementos.
        k (int): Número de elementos a permutar.

    Returns:
        int: El número de permutaciones posibles.

    Raises:
        ValueError: Si k es mayor que n o si alguno de los argumentos no es un entero no negativo.
    """
    validate_non_negative_integers(n, k)
    
    if k > n:
        raise ValueError(f"No se puede permutar {k} elementos de un conjunto de {n} elementos.")
    
    return factorial(n) // factorial(n - k)

def circular_permutations(n):
    """
    Calcula el número de permutaciones circulares de un conjunto de n elementos.

    Args:
        n (int): Número total de elementos.

    Returns:
        int: El número de permutaciones circulares posibles.

    Raises:
        ValueError: Si n es menor que 1.
    """
    validate_non_negative_integers(n)
    
    if n < 1:
        raise ValueError("El número de elementos para una permutación circular debe ser mayor o igual a 1.")
    
    # En permutaciones circulares, el número de formas de organizar n elementos en un círculo es (n-1)!
    return factorial(n - 1)

def generalized_binomial(x, k):
    """
    Calcula el coeficiente binomial generalizado (xCk), donde x puede ser un número real o fraccionario.

    Args:
        x (float): Un número real.
        k (int): Número de elementos a elegir.

    Returns:
        float: El coeficiente binomial generalizado.

    Raises:
        ValueError: Si k no es un entero no negativo.
    """
    validate_non_negative_integers(k)
    
    # El coeficiente binomial generalizado: x(x-1)...(x-k+1) / k!
    result = 1
    for i in range(k):
        result *= (x - i)
    
    return result / factorial(k)
