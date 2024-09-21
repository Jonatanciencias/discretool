""" Comandos de la línea de comandos para operaciones de combinatoria. """
# src/combinatorics/combinatorics_cli.py

import click

from src.combinatorics import(
    combinations,
    permutations,
    circular_permutations,
    generalized_binomial,
    combinations_with_repetition,
    generate_subsets,
    multinomial,
    stirling_first,
    stirling_second,
    catalan_number,
    generate_partitions,
    generate_lexicographic_combinations,
    heap_permutations
)

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

@combinatorics_cli.command(name="circular_permutations")
@click.argument("n", type=int)
def circular_permutations_command(n):
    """Calcula permutaciones circulares de n elementos."""
    try:
        result = circular_permutations(n)
        click.echo(f"Permutaciones circulares de {n} elementos: {result}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}. Asegúrate de que el número de elementos sea válido.")

@combinatorics_cli.command(name="generalized_binomial")
@click.argument("x", type=float)
@click.argument("k", type=int)
def generalized_binomial_command(x, k):
    """Calcula el coeficiente binomial generalizado."""
    try:
        result = generalized_binomial(x, k)
        click.echo(f"Coeficiente binomial generalizado de {x} sobre {k}: {result}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}. Asegúrate de que k sea un entero no negativo.")

@combinatorics_cli.command(name="subsets")
@click.argument("n", type=int)
def subsets_command(n):
    """
    Genera todos los subconjuntos de un conjunto de tamaño n.
    
    Ejemplo de uso:
    python -m src.cli combinatorics subsets 3
    """
    try:
        subsets = generate_subsets(n)
        click.echo(f"Subconjuntos de un conjunto de tamaño {n}:")
        for subset in subsets:
            click.echo(f"{subset}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")

@combinatorics_cli.command(name="multinomial")
@click.argument("n", type=int)
@click.argument("groups", nargs=-1, type=int)
def multinomial_command(n, groups):
    """
    Calcula el coeficiente multinomial.
    
    Ejemplo de uso:
    python -m src.cli combinatorics multinomial 10 3 2 5
    """
    try:
        result = multinomial(n, *groups)
        click.echo(f"Coeficiente multinomial para n={n} y grupos {groups}: {result}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")

# Comando para Números de Stirling de Primer Tipo
@combinatorics_cli.command(name="stirling_first")
@click.argument("n", type=int)
@click.argument("k", type=int)
def stirling_first_command(n, k):
    """Calcula los números de Stirling de primer tipo."""
    try:
        result = stirling_first(n, k)
        click.echo(f"Números de Stirling de primer tipo para n={n}, k={k}: {result}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")

# Comando para Números de Stirling de Segundo Tipo
@combinatorics_cli.command(name="stirling_second")
@click.argument("n", type=int)
@click.argument("k", type=int)
def stirling_second_command(n, k):
    """Calcula los números de Stirling de segundo tipo."""
    try:
        result = stirling_second(n, k)
        click.echo(f"Números de Stirling de segundo tipo para n={n}, k={k}: {result}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")

# Comando para Números de Catalan
@combinatorics_cli.command(name="catalan_number")
@click.argument("n", type=int)
def catalan_number_command(n):
    """Calcula los números de Catalan."""
    try:
        result = catalan_number(n)
        click.echo(f"Número de Catalan para n={n}: {result}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")


# Comando para generar particiones de un número entero
@combinatorics_cli.command(name="partitions")
@click.argument("n", type=int)
def partitions_command(n):
    """Genera todas las particiones de un número entero."""
    try:
        partitions = generate_partitions(n)
        click.echo(f"Particiones de {n}:")
        for partition in partitions:
            click.echo(f"{partition}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")

# Comando para generar combinaciones lexicográficas
@combinatorics_cli.command(name="lexicographic_combinations")
@click.argument("n", type=int)
@click.argument("k", type=int)
def lexicographic_combinations_command(n, k):
    """
    Genera combinaciones de k elementos de un conjunto de tamaño n en orden lexicográfico.
    
    Ejemplo de uso:
    python -m src.cli combinatorics lexicographic_combinations 5 3
    """
    try:
        lexicographic_combinations = generate_lexicographic_combinations(n, k)
        click.echo(f"Combinaciones lexicográficas de {n} elementos tomados de {k} en {k}:")
        for combination in lexicographic_combinations:
            click.echo(f"{combination}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")

# Comando para generar permutaciones usando el Algoritmo de Heap
@combinatorics_cli.command(name="heap_permutations")
@click.argument("n", type=int)
def heap_permutations_command(n):
    """
    Genera todas las permutaciones de un conjunto de tamaño n utilizando el Algoritmo de Heap.
    
    Ejemplo de uso:
    python -m src.cli combinatorics heap_permutations 4
    """
    try:
        heap_perms = heap_permutations(n)
        click.echo(f"Permutaciones de {n} elementos usando el Algoritmo de Heap:")
        for perm in heap_perms:
            click.echo(f"{perm}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")



if __name__ == "__main__":
    combinatorics_cli()