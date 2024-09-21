""" Módulo que contiene funciones para calcular los números de Stirling de primer y segundo tipo. """
# src/combinatorics/stirling_numbers.py


def stirling_first(n, k):
    """
    Calcula el número de Stirling de primer tipo (permutaciones de n elementos con k ciclos).

    Args:
        n (int): Número total de elementos.
        k (int): Número de ciclos.

    Returns:
        int: Números de Stirling de primer tipo.
    """
    if n == k == 0:
        return 1
    elif k == 0 or n == 0:
        return 0
    else:
        return (n - 1) * stirling_first(n - 1, k) + stirling_first(n - 1, k - 1)


def stirling_second(n, k):
    """
    Calcula el número de Stirling de segundo tipo (divisiones de n elementos en k subconjuntos).

    Args:
        n (int): Número total de elementos.
        k (int): Número de subconjuntos.

    Returns:
        int: Números de Stirling de segundo tipo.
    """
    if n == k == 0:
        return 1
    elif k == 0 or n == 0:
        return 0
    else:
        return k * stirling_second(n - 1, k) + stirling_second(n - 1, k - 1)
