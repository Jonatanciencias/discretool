""" Módulo que contiene la implementación del Algoritmo de Heap para generar permutaciones. """
# src/combinatorics/heap_permutations.py

def heap_permutations(n):
    """
    Genera todas las permutaciones de un conjunto de tamaño n utilizando el Algoritmo de Heap.

    Args:
        n (int): El número de elementos en el conjunto.

    Returns:
        list: Lista de permutaciones de n elementos.
    """
    # Crear una lista con los números 1 hasta n
    elements = list(range(1, n + 1))
    result = []

    def generate(k, elements):
        if k == 1:
            result.append(tuple(elements))
        else:
            generate(k - 1, elements)
            for i in range(k - 1):
                if k % 2 == 0:
                    elements[i], elements[k - 1] = elements[k - 1], elements[i]
                else:
                    elements[0], elements[k - 1] = elements[k - 1], elements[0]
                generate(k - 1, elements)

    generate(n, elements)
    return result
