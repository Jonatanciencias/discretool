""" Módulo de la interfaz de línea de comandos para operaciones de lógica proposicional. """
# src/logic/logic_cli.py

import click
import sympy

from src.logic.logic_solver import (
    evaluate_expression,
    truth_table,
    parse_expression,
)
from src.utils import (
    normalize_expression,
    replace_implication,
    validate_expression,
    export_truth_table_csv,
    export_truth_table_md,
    visualize_truth_table,
)


@click.group(name="logic")
def logic_cli():
    """Operaciones de Lógica Proposicional"""


# Definir los comandos aquí antes de agregarlos al grupo
@click.command()
@click.argument("expression")
@click.option(
    "--assign",
    "-a",
    multiple=True,
    type=(str, bool),
    help="Asignaciones de variables, e.g., -a A True -a B False",
)
def evaluate(expression, assign):
    """Evalúa una expresión lógica con asignaciones dadas."""
    # Validación de la expresión antes de procesarla
    valid, feedback = validate_expression(expression)
    if not valid:
        click.echo("Errores encontrados en la expresión:")
        for suggestion in feedback:
            click.echo(f" - {suggestion}")
        return

    expression = normalize_expression(expression)
    expression = replace_implication(expression)

    try:
        expr = sympy.parse_expr(expression)
        assignments = {var: val for var, val in assign}
        result = evaluate_expression(expr, assignments)

        click.echo(f"Expresión normalizada: {expression}")
        click.echo(f"Resultado: {result}")

    except (sympy.SympifyError, ValueError) as e:
        click.echo(f"Error: {str(e)}")


@click.command()
@click.argument("expression")
@click.option(
    "--export",
    type=click.Choice(["csv", "md"]),
    default=None,
    help="Exportar la tabla de verdad a CSV o Markdown",
)
@click.option("--filename", default="truth_table", help="Nombre del archivo exportado")
@click.option("--graph", is_flag=True, help="Generar una visualización gráfica de la tabla")
def table(expression, export, filename, graph):
    """Genera la tabla de verdad para una expresión lógica."""
    # Validación de la expresión antes de procesarla
    valid, feedback = validate_expression(expression)
    if not valid:
        click.echo("Errores encontrados en la expresión:")
        for suggestion in feedback:
            click.echo(f" - {suggestion}")
        return

    expression = normalize_expression(expression)
    expression = replace_implication(expression)
    expr = parse_expression(expression)
    headers, table_data = truth_table(expr)

    # Mostrar la tabla en la terminal
    header_str = " | ".join(headers)
    separator = "-+-".join(["-" * len(h) for h in headers])
    click.echo(header_str)
    click.echo(separator)
    for row in table_data:
        row_str = " | ".join(["T" if row.get(h) else "F" for h in headers])
        click.echo(row_str)

    # Exportar a CSV o Markdown
    if export == "csv":
        export_truth_table_csv(headers, table_data, f"{filename}.csv")
        click.echo(f"Tabla de verdad exportada como {filename}.csv en la carpeta 'exports'.")
    elif export == "md":
        export_truth_table_md(headers, table_data, f"{filename}.md")
        click.echo(f"Tabla de verdad exportada como {filename}.md en la carpeta 'exports'.")

    # Visualización gráfica (opcional)
    if graph:
        visualize_truth_table(headers, table_data, filename)
        click.echo(f"Gráfico de la tabla de verdad guardado como {filename}.png en la carpeta 'exports'.")


# Agregar los comandos al grupo `logic_cli`
logic_cli.add_command(evaluate)
logic_cli.add_command(table)

# También puedes agregar otros comandos aquí como `simplify`, `equivalent`, etc.
