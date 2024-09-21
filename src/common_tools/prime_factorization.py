"""Descompone un número en sus factores primos."""
# src/common_tools/prime_factorization.py

def factorize(n):
    """Descompone un número en sus factores primos."""
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

