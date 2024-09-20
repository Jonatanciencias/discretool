"""CLI para las herramientas comunes de Matemáticas Discretas."""

# src/common_tools/common_tools_cli.py

import click
from src.common_tools import (
    gcd,
    lcm,
    generate_primes,
    is_congruent,
    solve_linear_congruence,
    solve_diophantine,
)


@click.group(invoke_without_command=True)
@click.pass_context
def common_tools_cli(ctx):
    """Herramientas comunes para Matemáticas Discretas"""
    if ctx.invoked_subcommand is None:
        click.echo(
            "Herramientas comunes disponibles: gcd, lcm, primes, congruence, solve-congruence, solve-diophantine."
        )


@common_tools_cli.command(name="gcd_command")
@click.argument("a", type=int)
@click.argument("b", type=int)
def gcd_command(a, b):
    """Calcula el MCD (Máximo Común Divisor) de dos números."""
    result = gcd(a, b)
    click.echo(f"El MCD de {a} y {b} es {result}")


@common_tools_cli.command(name="lcm_command")
@click.argument("a", type=int)
@click.argument("b", type=int)
def lcm_command(a, b):
    """Calcula el MCM (Mínimo Común Múltiplo) de dos números."""
    result = lcm(a, b)
    click.echo(f"El MCM de {a} y {b} es {result}")


@common_tools_cli.command(name="primes")
@click.argument("n", type=int)
def primes_command(n):
    """Genera todos los números primos menores o iguales a n."""
    prime_numbers = generate_primes(n)
    click.echo(f"Números primos menores o iguales a {n}: {prime_numbers}")


@common_tools_cli.command(name="congruence")
@click.argument("a", type=int)
@click.argument("b", type=int)
@click.argument("m", type=int)
def congruence(a, b, m):
    """Verifica si a es congruente con b módulo m."""
    if is_congruent(a, b, m):
        click.echo(f"{a} es congruente con {b} módulo {m}")
    else:
        click.echo(f"{a} NO es congruente con {b} módulo {m}")


@common_tools_cli.command(name="solve-congruence")
@click.argument("a", type=int)
@click.argument("b", type=int)
@click.argument("m", type=int)
def solve_congruence(a, b, m):
    """Resuelve la congruencia lineal ax ≡ b (mod m)."""
    solutions = solve_linear_congruence(a, b, m)
    click.echo(f"Soluciones de {a}x ≡ {b} (mod {m}): {solutions}")


@common_tools_cli.command(name="solve-diophantine")
@click.argument("a", type=int)
@click.argument("b", type=int)
@click.argument("c", type=int)
def solve_diophantine_command(a, b, c):
    """Resuelve la ecuación diofántica ax + by = c."""
    result = solve_diophantine(a, b, c)
    click.echo(f"Solución para la ecuación {a}x + {b}y = {c}: {result}")


if __name__ == "__main__":
    common_tools_cli()
