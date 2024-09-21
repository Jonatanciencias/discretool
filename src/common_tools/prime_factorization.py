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

# src/common_tools/common_tools_cli.py
@click.command()
@click.argument('number', type=int)
def prime_factorization(number):
    """Descompone un número en sus factores primos."""
    factors = factorize(number)
    click.echo(f"Factorización prima de {number}: {factors}")
