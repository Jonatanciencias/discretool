""" Módulo que contiene funciones para generar particiones de un número entero. """
# src/combinatorics/partitions.py

def generate_partitions(n):
    """
    Genera todas las particiones de un número entero n.

    Args:
        n (int): El número entero a particionar.

    Returns:
        list: Una lista de listas, donde cada lista interna es una partición de n.
    """
    def partitions_helper(n, max_value):
        if n == 0:
            return [[]]
        if n < 0:
            return []
        result = []
        for i in range(min(n, max_value), 0, -1):
            for partition in partitions_helper(n - i, i):
                result.append([i] + partition)
        return result

    return partitions_helper(n, n)
