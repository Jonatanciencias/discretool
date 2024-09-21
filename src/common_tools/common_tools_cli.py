"""CLI para las herramientas comunes de Matemáticas Discretas."""
# src/common_tools/common_tools_cli.py

import click
from src.common_tools import (
    is_congruent,
    solve_linear_congruence,
    solve_diophantine,
    gcd,
    lcm,
    division_algorithm,
    generate_primes,
    sieve_of_eratosthenes,
    factorize,
    mod_exp,
    mod_inverse,
    extended_gcd
)


@click.group(invoke_without_command=True)
@click.pass_context
def common_tools_cli(ctx):
    """Herramientas comunes para Matemáticas Discretas"""
    if ctx.invoked_subcommand is None:
        click.echo(
            "Herramientas comunes disponibles: gcd, lcm, primes, congruence, solve-congruence, solve-diophantine."
        )

@common_tools_cli.command(name="gcd")
@click.argument("a", type=int)
@click.argument("b", type=int)
def gcd_command(a, b):
    """Calcula el MCD (Máximo Común Divisor) de dos números."""
    result = gcd(a, b)
    click.echo(f"El MCD de {a} y {b} es {result}")


@common_tools_cli.command(name="lcm")
@click.argument("a", type=int)
@click.argument("b", type=int)
def lcm_command(a, b):
    """Calcula el MCM (Mínimo Común Múltiplo) de dos números."""
    result = lcm(a, b)
    click.echo(f"El MCM de {a} y {b} es {result}")


# Comando para generar todos los primos menores o iguales a n usando el método básico
@common_tools_cli.command(name="primes")
@click.argument('n', type=int)
def primes(n):
    """
    Genera todos los números primos menores o iguales a n.
    """
    primes_list = generate_primes(n)
    click.echo(f"Números primos menores o iguales a {n}: {primes_list}")

# Comando para generar todos los primos usando la Criba de Eratóstenes
@common_tools_cli.command(name="sieve_primes")
@click.argument('limit', type=int)
def sieve_primes(limit):
    """
    Genera todos los primos menores o iguales a 'limit' usando la Criba de Eratóstenes.
    """
    primes_list = sieve_of_eratosthenes(limit)
    click.echo(f"Números primos hasta {limit} utilizando la Criba de Eratóstenes: {primes_list}")


@common_tools_cli.command(name="is_congruent")
@click.argument("a", type=int)
@click.argument("b", type=int)
@click.argument("m", type=int)
def congruence(a, b, m):
    """Verifica si a es congruente con b módulo m."""
    if is_congruent(a, b, m):
        click.echo(f"{a} es congruente con {b} módulo {m}")
    else:
        click.echo(f"{a} NO es congruente con {b} módulo {m}")


@common_tools_cli.command(name="solve_linear_congruence")
@click.argument("a", type=int)
@click.argument("b", type=int)
@click.argument("m", type=int)
def solve_congruence(a, b, m):
    """Resuelve la congruencia lineal ax ≡ b (mod m)."""
    solutions = solve_linear_congruence(a, b, m)
    click.echo(f"Soluciones de {a}x ≡ {b} (mod {m}): {solutions}")


@common_tools_cli.command(name="solve_diophantine")
@click.argument("a", type=int)
@click.argument("b", type=int)
@click.argument("c", type=int)
def solve_diophantine_command(a, b, c):
    """Resuelve la ecuación diofántica ax + by = c."""
    result = solve_diophantine(a, b, c)
    click.echo(f"Solución para la ecuación {a}x + {b}y = {c}: {result}")

@common_tools_cli.command(name="prime_factorization")
@click.argument('number', type=int)
def prime_factorization(number):
    """Descompone un número en sus factores primos."""
    factors = factorize(number)
    click.echo(f"Factorización prima de {number}: {factors}")


@common_tools_cli.command(name="mod_exp")
@click.argument('base', type=int)
@click.argument('exp', type=int)
@click.argument('mod', type=int)
def mod_exp_cli(base, exp, mod):
    """Calcula exponenciación modular."""
    result = mod_exp(base, exp, mod)
    click.echo(f"Resultado: {result}")

@common_tools_cli.command(name="extended_gcd")
@click.argument('a', type=int)
@click.argument('b', type=int)
def extended_gcd_cli(a, b):
    """Calcula el MCD usando el Algoritmo Extendido de Euclides."""
    g, x, y = extended_gcd(a, b)
    click.echo(f"MCD: {g}, Coeficientes de Bézout: {x}, {y}")


if __name__ == "__main__":
    common_tools_cli()
