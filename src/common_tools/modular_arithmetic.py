""" Módulo con funciones de aritmética modular. """
# src/common_tools/modular_arithmetic.py

def mod_exp(base, exp, mod):
    """Exponenciación modular."""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

def mod_inverse(a, mod):
    """Inverso modular usando el Algoritmo Extendido de Euclides."""
    g, x, _ = extended_gcd(a, mod)
    if g != 1:
        raise ValueError("No existe inverso modular")
    else:
        return x % mod

# src/common_tools/common_tools_cli.py

