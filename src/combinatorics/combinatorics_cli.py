# src/combinatorics/combinatorics_cli.py

import click
from src.combinatorics.combinations import combinations
from src.combinatorics.permutations import permutations
from src.utils.error_handling import validate_non_negative_integers

@click.group()
def combinatorics_cli():
    """
    Operaciones de Combinatoria.

    Este comando contiene operaciones relacionadas con la combinatoria, como 
    combinaciones (nCk) y permutaciones (nPk).

    Uso:
    - Combinaciones: Calcula cuántas formas diferentes se pueden elegir k elementos de un conjunto de n elementos.
    - Permutaciones: Calcula cuántas formas diferentes se pueden ordenar k elementos de un conjunto de n elementos.

    Utiliza --help para más información en cada comando.
    """
    pass

@combinatorics_cli.command(name="combinations")
@click.argument("n", type=int)
@click.argument("k", type=int)
def combinations_command(n, k):
    """
    Calcula combinaciones (nCk).
    
    Devuelve el número de formas en las que se pueden elegir k elementos de un 
    conjunto de n elementos sin importar el orden.

    Ejemplo de uso:
    python -m src.cli combinatorics combinations 5 3
    """
    try:
        # Validar que n y k sean enteros no negativos
        validate_non_negative_integers(n, k)

        # Calcular combinaciones
        result = combinations(n, k)
        click.echo(f"Combinaciones de {n} elementos tomados de {k} en {k}: {result}")

    except ValueError as e:
        click.echo(f"Error: {str(e)}. Asegúrate de que n >= k y ambos sean no negativos.")

@combinatorics_cli.command(name="permutations")
@click.argument("n", type=int)
@click.argument("k", type=int)
def permutations_command(n, k):
    """
    Calcula permutaciones (nPk).
    
    Devuelve el número de formas en las que se pueden ordenar k elementos de 
    un conjunto de n elementos, considerando el orden.

    Ejemplo de uso:
    python -m src.cli combinatorics permutations 5 3
    """
    try:
        # Validar que n y k sean enteros no negativos
        validate_non_negative_integers(n, k)

        # Calcular permutaciones
        result = permutations(n, k)
        click.echo(f"Permutaciones de {n} elementos tomados de {k} en {k}: {result}")

    except ValueError as e:
        click.echo(f"Error: {str(e)}. Asegúrate de que n >= k y ambos sean no negativos.")

if __name__ == "__main__":
    combinatorics_cli()
