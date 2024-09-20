# src/logic/logic_cli.py

import click
import sympy
from sympy.parsing.sympy_parser import parse_expr
from src.logic.logic_solver import (
    evaluate_expression,
    truth_table,
    simplify_expression,
    classify_expression,
    are_equivalent,
    is_satisfiable,
    check_equivalence,
    analyze_complexity,
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
def logic():
    """Operaciones de Lógica Proposicional"""
    pass


@logic.command()
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

    # Validar la expresión antes de procesar
    valid, feedback = validate_expression(expression)
    if not valid:
        click.echo("Errores encontrados en la expresión:")
        for suggestion in feedback:
            click.echo(f" - {suggestion}")
        return

    expression = normalize_expression(expression)
    expression = replace_implication(expression)

    try:
        # Parsear la expresión con SymPy
        expr = parse_expr(expression)
        assignments = {var: val for var, val in assign}
        result = evaluate_expression(expr, assignments)

        click.echo(f"Expresión normalizada: {expression}")
        click.echo(f"Resultado: {result}")

    except (sympy.SympifyError, ValueError) as e:
        click.echo(f"Error: {str(e)}")


@logic.command()
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


@logic.command()
@click.argument("expression")
@click.option(
    "--form",
    "-f",
    type=click.Choice(["dnf", "cnf"]),
    default="dnf",
    help="Forma normal a simplificar (dnf o cnf)",
)
def simplify(expression, form):
    """Simplifica una expresión lógica a DNF o CNF."""

    valid, feedback = validate_expression(expression)
    if not valid:
        click.echo("Errores encontrados en la expresión:")
        for suggestion in feedback:
            click.echo(f" - {suggestion}")
        return

    expression = normalize_expression(expression)
    expression = replace_implication(expression)
    expr = parse_expression(expression)
    simplified = simplify_expression(expr, form=form)
    click.echo(f"Expresión simplificada ({form.upper()}): {simplified}")


@logic.command()
@click.argument("expression")
def classify(expression):
    """Clasifica una expresión lógica como tautología, contradicción o contingencia."""

    valid, feedback = validate_expression(expression)
    if not valid:
        click.echo("Errores encontrados en la expresión:")
        for suggestion in feedback:
            click.echo(f" - {suggestion}")
        return

    expr = parse_expression(expression)
    classification = classify_expression(expr)
    click.echo(f"La expresión es una: {classification}")


@logic.command()
@click.argument("expression1")
@click.argument("expression2")
def equivalent(expression1, expression2):
    """Verifica si dos expresiones lógicas son equivalentes."""

    valid1, feedback1 = validate_expression(expression1)
    valid2, feedback2 = validate_expression(expression2)

    if not valid1:
        click.echo("Errores en la primera expresión:")
        for suggestion in feedback1:
            click.echo(f" - {suggestion}")
        return

    if not valid2:
        click.echo("Errores en la segunda expresión:")
        for suggestion in feedback2:
            click.echo(f" - {suggestion}")
        return

    expr1 = parse_expression(expression1)
    expr2 = parse_expression(expression2)
    are_equiv = are_equivalent(expr1, expr2)
    
    if are_equiv:
        click.echo("Las expresiones son equivalentes.")
    else:
        click.echo("Las expresiones NO son equivalentes.")


@logic.command()
@click.argument("expression")
def sat(expression):
    """Verifica si una expresión lógica es satisfacible (SAT) o insatisfacible (UNSAT)."""

    valid, feedback = validate_expression(expression)
    if not valid:
        click.echo("Errores encontrados en la expresión:")
        for suggestion in feedback:
            click.echo(f" - {suggestion}")
        return

    expr = parse_expression(expression)
    result = is_satisfiable(expr)
    click.echo(f"La expresión {expression} es {result}")


@logic.command()
@click.argument("expression1")
@click.argument("expression2")
def equivalence(expression1, expression2):
    """Verifica si dos expresiones son equivalentes usando reglas de inferencia."""

    valid1, feedback1 = validate_expression(expression1)
    valid2, feedback2 = validate_expression(expression2)

    if not valid1:
        click.echo("Errores en la primera expresión:")
        for suggestion in feedback1:
            click.echo(f" - {suggestion}")
        return

    if not valid2:
        click.echo("Errores en la segunda expresión:")
        for suggestion in feedback2:
            click.echo(f" - {suggestion}")
        return

    equiv_result, steps = check_equivalence(expression1, expression2)
    if equiv_result:
        click.echo("Las expresiones son equivalentes.")
        for step, rule in steps:
            click.echo(f"{rule}: {step}")
    else:
        click.echo("Las expresiones NO son equivalentes.")


@logic.command()
@click.argument("expressions", nargs=-1)
def derive(expressions):
    """Aplica deducción natural paso a paso para las expresiones dadas."""
    steps = []
    for expr in expressions:
        expr = expr.replace("->", "Implies")
        try:
            steps.append(sympy.sympify(expr))
        except sympy.SympifyError:
            click.echo(f"Error al procesar la expresión: {expr}")
            return
    deductions = apply_inference_rules(steps)
    for deduction in deductions:
        click.echo(deduction)


@logic.command()
@click.argument("expression")
def complexity(expression):
    """Analiza la complejidad de una expresión lógica."""

    valid, feedback = validate_expression(expression)
    if not valid:
        click.echo("Errores encontrados en la expresión:")
        for suggestion in feedback:
            click.echo(f" - {suggestion}")
        return

    expression = replace_implication(expression)
    num_operations, num_variables = analyze_complexity(expression)
    click.echo(f"La expresión tiene {num_operations} operaciones lógicas y {num_variables} variables.")
