"""" Módulo de la interfaz de línea de comandos para operaciones de lógica proposicional. """
# src/logic/logic_cli.py

import click
from sympy.parsing.sympy_parser import parse_expr
import sympy

from src.logic import (
    truth_table,
    parse_expression,
)
from src.utils import (
    normalize_expression,
    validate_expression,
    export_to_csv,
    export_to_md,
    visualize_truth_table,
    handle_boolean_expression,
    check_common_errors,
)


@click.group(name="logic")
def logic_cli():
    """Operaciones de Lógica Proposicional"""


# Comando para evaluar una expresión lógica
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

    # Normalizar la expresión antes de cualquier operación
    expression = normalize_expression(expression)
    click.echo(f"DEBUG: Expresión normalizada: {expression}")

    # Validación de la expresión antes de procesarla
    valid, feedback = validate_expression(expression)
    if not valid:
        click.echo("Errores encontrados en la expresión:")
        for suggestion in feedback:
            click.echo(f" - {suggestion}")
        return

    try:
        # Parsear la expresión con SymPy
        expr = parse_expr(expression)
        click.echo(f"DEBUG: Expresión parseada por SymPy: {expr}")

        assignments = {var: val for var, val in assign}
        click.echo(f"DEBUG: Asignaciones proporcionadas: {assignments}")

        # Evaluar la expresión con las asignaciones
        if isinstance(expr, bool):
            result = expr  # Si ya es booleana, no hace falta sustituir
            click.echo(f"DEBUG: Expresión evaluada como booleana: {result}")
        else:
            evaluated_expr = expr.subs(assignments)
            click.echo(f"DEBUG: Expresión después de aplicar subs(): {evaluated_expr}")

            # Si es una expresión booleana, manejarla con el módulo de booleanos
            result = handle_boolean_expression(evaluated_expr)

        click.echo(f"Resultado: {result}")

    except (sympy.SympifyError, ValueError) as e:
        click.echo(f"Error: {str(e)}")



# Comando para generar una tabla de verdad
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
    # Normalizar la expresión antes del parseo
    click.echo(f"Expresión original: {expression}")
    expression = normalize_expression(expression)
    click.echo(f"Expresión normalizada: {expression}")
    
    # Validación de la expresión antes de procesarla
    valid, feedback = validate_expression(expression)
    if not valid:
        click.echo("Errores encontrados en la expresión:")
        for suggestion in feedback:
            click.echo(f" - {suggestion}")
        return
    expression = normalize_expression(expression)
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
        export_to_csv(headers, table_data, f"{filename}.csv")
        click.echo(f"Tabla de verdad exportada como {filename}.csv en la carpeta 'exports'.")
    elif export == "md":
        export_to_md(headers, table_data, f"{filename}.md")
        click.echo(f"Tabla de verdad exportada como {filename}.md en la carpeta 'exports'.")

    # Visualización gráfica (opcional)
    if graph:
        visualize_truth_table(headers, table_data, filename)
        click.echo(f"Gráfico de la tabla de verdad guardado como {filename}.png en la carpeta 'exports'.")

@click.command()
@click.argument("expression")
@click.option("--form", "-f", type=click.Choice(["cnf", "dnf"]), help="Especificar la forma normal (CNF, DNF)")
def simplify(expression, form):
    """Simplifica una expresión lógica en CNF o DNF."""
    expression = normalize_expression(expression)
    expr = parse_expression(expression)
    
    if form == "cnf":
        simplified_expr = sympy.to_cnf(expr)
    elif form == "dnf":
        simplified_expr = sympy.to_dnf(expr)

    click.echo(f"Expresión simplificada ({form}): {simplified_expr}")

@click.command()
@click.argument("expression")
def classify(expression):
    """Clasifica una expresión lógica como tautología, contradicción o contingencia."""
    
    # Normalización y validación
    expression = normalize_expression(expression)
    valid, feedback = validate_expression(expression)
    
    if not valid:
        click.echo("Errores encontrados en la expresión:")
        for suggestion in feedback:
            click.echo(f" - {suggestion}")
        return
    
    try:
        # Parseo y simplificación
        expr = parse_expression(expression)
        simplified_expr = sympy.simplify_logic(expr)
        
        # Clasificación basada en el resultado simplificado
        if isinstance(simplified_expr, bool):
            if simplified_expr:
                result = "tautología"
            else:
                result = "contradicción"
        else:
            # Si no se simplifica a un booleano, lo tratamos como una contingencia
            result = "contingencia"
        
        click.echo(f"La expresión es una {result}.")
    
    except Exception as e:
        # Manejo de errores
        click.echo(f"Error al procesar la expresión: {str(e)}")
        check_common_errors(expression)

@click.command()
@click.argument("expression1")
@click.argument("expression2")
def equivalent(expression1, expression2):
    """Verifica si dos expresiones son equivalentes."""
    
    # Normalización y validación
    expression1 = normalize_expression(expression1)
    expression2 = normalize_expression(expression2)
    
    valid1, feedback1 = validate_expression(expression1)
    valid2, feedback2 = validate_expression(expression2)
    
    if not valid1 or not valid2:
        click.echo("Errores encontrados en las expresiones:")
        if not valid1:
            for suggestion in feedback1:
                click.echo(f" - {suggestion} en la primera expresión")
        if not valid2:
            for suggestion in feedback2:
                click.echo(f" - {suggestion} en la segunda expresión")
        return
    
    try:
        # Parseo y simplificación
        expr1 = parse_expression(expression1)
        expr2 = parse_expression(expression2)
        
        # Verificación de equivalencia
        if sympy.simplify_logic(expr1) == sympy.simplify_logic(expr2):
            click.echo("Las expresiones son equivalentes.")
        else:
            click.echo("Las expresiones no son equivalentes.")
    
    except Exception as e:
        # Manejo de errores
        click.echo(f"Error al procesar las expresiones: {str(e)}")
        check_common_errors(expression2)
        check_common_errors(expression1)


# Agregar los comandos al grupo `logic_cli`
logic_cli.add_command(evaluate)
logic_cli.add_command(table)
logic_cli.add_command(simplify)
logic_cli.add_command(classify)
logic_cli.add_command(equivalent)

