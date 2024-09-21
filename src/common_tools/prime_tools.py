""" Módulo con funciones relacionadas a los números primos. """
# src/common_tools/prime_tools.py

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

def sieve_of_eratosthenes(limit):
    """Genera todos los primos menores o iguales a 'limit' usando la Criba de Eratóstenes."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for i in range(start * start, limit + 1, start):
                sieve[i] = False
    return [num for num, prime in enumerate(sieve) if prime]

# src/common_tools/common_tools_cli.py
@click.command()
@click.argument('limit', type=int)
def primes_cli(limit):
    """Genera todos los números primos hasta 'limit'."""
    primes = sieve_of_eratosthenes(limit)
    click.echo(f"Primos hasta {limit}: {primes}")