""" Módulo con funciones para trabajar con congruencias. """
# src/common_tools/congruences.py

def is_congruent(a, b, m):
    """
    Verifica si a es congruente con b módulo m (a ≡ b (mod m)).

    Args:
        a (int): Primer número.
        b (int): Segundo número.
        m (int): Módulo.

    Returns:
        bool: True si a ≡ b (mod m), False en caso contrario.
    """
    return (a - b) % m == 0


def solve_linear_congruence(a, b, m):
    """
    Resuelve la congruencia lineal ax ≡ b (mod m).

    Args:
        a (int): Coeficiente de la incógnita.
        b (int): Segundo término.
        m (int): Módulo.

    Returns:
        list: Lista de soluciones o mensaje de error si no hay soluciones.
    """

    # Usa el algoritmo extendido de Euclides para resolver la congruencia
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        else:
            gcd, x, y = extended_gcd(b, a % b)
            return gcd, y, x - (a // b) * y

    gcd, x, _ = extended_gcd(a, m)

    if b % gcd != 0:
        return "No tiene solución"

    x0 = (x * (b // gcd)) % m
    return [(x0 + i * (m // gcd)) % m for i in range(gcd)]


def solve_diophantine(a, b, c):
    """
    Resuelve ecuaciones diofánticas ax + by = c usando el algoritmo extendido de Euclides.

    Args:
        a (int): Coeficiente de x.
        b (int): Coeficiente de y.
        c (int): Término constante.

    Returns:
        tuple: (x, y) que resuelve la ecuación o un mensaje de error si no tiene solución.
    """

    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        else:
            gcd, x, y = extended_gcd(b, a % b)
            return gcd, y, x - (a // b) * y

    gcd, x0, y0 = extended_gcd(a, b)

    if c % gcd != 0:
        return "No tiene solución"

    x = x0 * (c // gcd)
    y = y0 * (c // gcd)

    return (x, y)
