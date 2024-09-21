# src/combinatorics/lexicographic_combinations.py

from itertools import combinations

def generate_lexicographic_combinations(n, k):
    """
    Genera todas las combinaciones posibles de n elementos tomados de k en k, en orden lexicográfico.

    Args:
        n (int): El número total de elementos.
        k (int): El tamaño de cada combinación.

    Returns:
        list: Lista de combinaciones en orden lexicográfico.
    """
    if k > n:
        raise ValueError(f"No se puede elegir {k} elementos de un conjunto de {n} elementos.")
    return list(combinations(range(1, n + 1), k))
