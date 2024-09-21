"""Combinatorics: Calcula combinaciones y permutaciones."""
# src/combinatorics/combinatorics_cli.py

import click
from src.combinatorics.combinations import combinations
from src.combinatorics.permutations import permutations

@click.group()
def combinatorics_cli():
    """Combinatorics: Calcula combinaciones y permutaciones."""
    pass

@combinatorics_cli.command(name="combinations")
@click.argument("n", type=int)
@click.argument("k", type=int)
def combinations_command(n, k):
    """Calcula combinaciones (nCk)."""
    try:
        result = combinations(n, k)
        click.echo(f"Combinaciones de {n} elementos tomados de {k} en {k} es: {result}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")

@combinatorics_cli.command(name="permutations")
@click.argument("n", type=int)
@click.argument("k", type=int)
def permutations_command(n, k):
    """Calcula permutaciones (nPk)."""
    try:
        result = permutations(n, k)
        click.echo(f"Permutaciones de {n} elementos tomados de {k} en {k} es: {result}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")

if __name__ == "__main__":
    combinatorics_cli()
