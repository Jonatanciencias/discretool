def is_prime(n):
    """Verifica si un número es primo."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(n):
    """
    Genera todos los números primos menores o iguales a n.

    Args:
        n (int): Límite superior.

    Returns:
        list: Lista de números primos.
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes
