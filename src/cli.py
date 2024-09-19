#/src/cli.py

import click
import sympy
#from sympy import symbols, Implies, Not
from sympy.parsing.sympy_parser import parse_expr

from src.common_tools import (
    is_congruent,
    solve_linear_congruence,
    solve_diophantine,
    gcd,
    lcm,
    generate_primes
)
from src.logic import (
    parse_expression,
    evaluate_expression,
    truth_table,
    simplify_expression,
    classify_expression,
    are_equivalent,
    apply_inference_rules,
    is_satisfiable
)

from src.utils import (
    replace_implication,
    print_welcome_message
)

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Aplicación para Matemáticas Discretas 2"""
    if ctx.invoked_subcommand is None:
        print_welcome_message()  # Mostrar el mensaje de bienvenida

@cli.group()
def logic():
    """Operaciones de Lógica Proposicional"""

@cli.group(name="common_tools")
def common_tools():
    """Herramientas comunes de Matemáticas Discretas"""


# COMMON COMMANDS
@common_tools.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def gcd_command(a, b):
    """Calcula el MCD (Máximo Común Divisor) de dos números."""
    result = gcd(a, b)
    click.echo(f"El MCD de {a} y {b} es {result}")


@common_tools.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def lcm_command(a, b):
    """Calcula el MCM (Mínimo Común Múltiplo) de dos números."""
    result = lcm(a, b)
    click.echo(f"El MCM de {a} y {b} es {result}")


@common_tools.command()
@click.argument('n', type=int)
def primes(n):
    """Genera todos los números primos menores o iguales a n."""
    primes = generate_primes(n)
    click.echo(f"Números primos menores o iguales a {n}: {primes}")


@common_tools.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
@click.argument('m', type=int)
def congruence(a, b, m):
    """Verifica si a es congruente con b módulo m."""
    if is_congruent(a, b, m):
        click.echo(f"{a} es congruente con {b} módulo {m}")
    else:
        click.echo(f"{a} NO es congruente con {b} módulo {m}")


@common_tools.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
@click.argument('m', type=int)
def solve_congruence(a, b, m):
    """Resuelve la congruencia lineal ax ≡ b (mod m)."""
    solutions = solve_linear_congruence(a, b, m)
    click.echo(f"Soluciones de {a}x ≡ {b} (mod {m}): {solutions}")


@common_tools.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
@click.argument('c', type=int)
def solve_diophantine_command(a, b, c):
    """Resuelve la ecuación diofántica ax + by = c."""
    result = solve_diophantine(a, b, c)
    click.echo(f"Solución para la ecuación {a}x + {b}y = {c}: {result}")


# LOGIC COMMANDS
@logic.command()
@click.argument('expression')
@click.option('--assign', '-a', multiple=True, type=(str, bool),
              help="Asignaciones de variables, e.g., -a A True -a B False")
def evaluate(expression, assign):
    """Evalúa una expresión lógica con asignaciones dadas."""
    # Reemplazar '->' por '>>'
    expression = replace_implication(expression)
    try:
        expr = parse_expr(expression)  # Usar parse_expr para entender '>>' como Implies
        assignments = {var: val for var, val in assign}
        result = evaluate_expression(expr, assignments)
        click.echo(f"Resultado: {result}")
    except (sympy.SympifyError, ValueError) as e:
        click.echo(f"Error al procesar la expresión: {e}")


@logic.command()
@click.argument('expression')
def table(expression):
    """Genera la tabla de verdad para una expresión lógica."""
    # Reemplazar '->' por 'Implies'
    expression = replace_implication(expression)
    expr = parse_expression(expression)
    headers, table_data = truth_table(expr)

    # Formatear la tabla para mostrarla
    header_str = ' | '.join(headers)
    separator = '-+-'.join(['-' * len(h) for h in headers])
    click.echo(header_str)
    click.echo(separator)
    for row in table_data:
        row_str = ' | '.join(['T' if row[h] else 'F' for h in headers])
        click.echo(row_str)


@logic.command()
@click.argument('expression')
@click.option('--form', '-f', type=click.Choice(['dnf', 'cnf']), default='dnf',
              help="Forma normal a simplificar (dnf o cnf)")
def simplify(expression, form):
    """Simplifica una expresión lógica a DNF o CNF."""
    # Reemplazar '->' por 'Implies'
    expression = replace_implication(expression)
    expr = parse_expression(expression)
    simplified = simplify_expression(expr, form=form)
    click.echo(f"Expresión simplificada ({form.upper()}): {simplified}")


@logic.command()
@click.argument('expression')
def classify(expression):
    """Clasifica una expresión lógica como tautología, contradicción o contingencia."""
    expr = parse_expression(expression)
    classification = classify_expression(expr)
    click.echo(f"La expresión es una: {classification}")


@logic.command()
@click.argument('expression1')
@click.argument('expression2')
def equivalent(expression1, expression2):
    """Verifica si dos expresiones lógicas son equivalentes."""
    # Reemplazar '->' por 'Implies'
    expression1 = replace_implication(expression1)
    expression2 = replace_implication(expression2)
    expr1 = parse_expression(expression1)
    expr2 = parse_expression(expression2)
    equivalence = are_equivalent(expr1, expr2)
    if equivalence:
        click.echo("Las expresiones son equivalentes.")
    else:
        click.echo("Las expresiones NO son equivalentes.")


@logic.command()
@click.argument('expression')
def sat(expression):
    """
    Verifica si una expresión lógica es satisfacible (SAT) o insatisfacible (UNSAT).
    
    Ejemplo:
        python cli.py logic sat "(A | ~B) & (B | ~C)"
    """
    expr = parse_expression(expression)

    # Verificar satisfacibilidad
    result = is_satisfiable(expr)
    click.echo(f"La expresión {expression} es {result}")


@logic.command()
@click.argument('expressions', nargs=-1)
def derive(expressions):
    """
    Aplica deducción natural paso a paso para las expresiones dadas.
    
    Ejemplo:
        python cli.py logic derive "(A -> B)" "A"
    """
    steps = []
    for expr in expressions:
        # Reemplazar '->' por 'Implies' para manejar implicaciones
        expr = expr.replace("->", "Implies")
        try:
            steps.append(sympy.sympify(expr))  # Convierte la cadena en una expresión simbólica de manera segura
        except sympy.SympifyError:
            click.echo(f"Error al procesar la expresión: {expr}")
            return
    
    # Aplica las reglas de inferencia paso a paso
    deductions = apply_inference_rules(steps)

    # Mostrar los pasos deducidos
    for deduction in deductions:
        click.echo(deduction)


if __name__ == '__main__':
    cli()
