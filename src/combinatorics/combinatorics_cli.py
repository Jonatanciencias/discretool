# src/combinatorics/combinatorics_cli.py

import click
from src.combinatorics.combinations import combinations
from src.combinatorics.permutations import permutations
from src.combinatorics.combinations_with_repetition import combinations_with_repetition
from src.utils import validate_non_negative_integers

@click.group()
def combinatorics_cli():
    """
    Operaciones de Combinatoria.
    
    Este comando contiene operaciones relacionadas con la combinatoria, como 
    combinaciones (nCk) y permutaciones (nPk).
    
    Utiliza --help para más información en cada comando.
    """

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
        validate_non_negative_integers(n, k)  # Validación de enteros no negativos
        result = combinations(n, k)
        click.echo(f"Combinaciones de {n} elementos tomados de {k} en {k}: {result}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}. Asegúrate de que n >= k y ambos sean no negativos.")

@combinatorics_cli.command(name="combinations_with_repetition")
@click.argument("n", type=int)
@click.argument("k", type=int)
def combinations_with_repetition_command(n, k):
    """
    Calcula combinaciones con repetición.
    
    Devuelve el número de formas en las que se pueden elegir k elementos de un 
    conjunto de n elementos permitiendo la repetición de elementos.
    
    Ejemplo de uso:
    python -m src.cli combinatorics combinations_with_repetition 5 3
    """
    try:
        validate_non_negative_integers(n, k)  # Validación de enteros no negativos
        result = combinations_with_repetition(n, k)
        click.echo(f"Combinaciones con repetición de {n} elementos tomados de {k}: {result}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}. Asegúrate de que ambos sean no negativos.")

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
        validate_non_negative_integers(n, k)  # Validación de enteros no negativos
        result = permutations(n, k)
        click.echo(f"Permutaciones de {n} elementos tomados de {k} en {k}: {result}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}. Asegúrate de que n >= k y ambos sean no negativos.")

if __name__ == "__main__":
    combinatorics_cli()