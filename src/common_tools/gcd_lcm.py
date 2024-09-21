""" Módulo con funciones para calcular el máximo común divisor (GCD) 
y el mínimo común múltiplo (LCM). """
# src/common_tools/gcd_lcm.py

import math

def gcd(a, b):
    """Calcula el máximo común divisor (GCD) usando el algoritmo de Euclides."""
    return math.gcd(a, b)

def lcm(a, b):
    """Calcula el mínimo común múltiplo (LCM)."""
    return abs(a * b) // gcd(a, b)

def division_algorithm(a, b):
    """
    Realiza la división y devuelve el cociente y el residuo.

    Args:
        a (int): El dividendo.
        b (int): El divisor.

    Returns:
        tuple: (cociente, residuo)
    """
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return divmod(a, b)

def extended_gcd(a, b):
    """Algoritmo de Euclides Extendido."""
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y

