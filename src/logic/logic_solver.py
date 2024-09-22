""" Módulo con funciones para resolver problemas de lógica proposicional. """
# src/logic/logic_solver.py

from itertools import product
import sympy
from sympy import simplify_logic, to_dnf, to_cnf
from sympy.core.sympify import SympifyError
from src.utils.normalize_expression import normalize_expression


def parse_expression(expr_str):
    """
    Toma una cadena de expresión lógica y la convierte en una expresión SymPy.
    Normaliza los operadores lógicos y procesa la implicación para SymPy.
    """
    try:
        # Paso 1: Normalizar la expresión antes de cualquier procesamiento
        expr_str = normalize_expression(expr_str)
        print(f"Expresión normalizada: {expr_str}")

        # Paso 2: Intentar convertir la expresión en un objeto de SymPy
        expr = sympy.sympify(expr_str)
        print(f"Expresión parseada por SymPy: {expr}")
        return expr

    except SympifyError as e:
        raise ValueError(f"Error al parsear la expresión: {e}") from e

    except Exception as e:
        raise ValueError(f"Error inesperado al procesar la expresión: {e}") from e

def evaluate_expression(expr, assignments):
    """
    Evalúa una expresión lógica con una asignación específica de valores.
    
    Args:
        expr (sympy.Expr): La expresión lógica.
        assignments (dict): Diccionario con asignaciones de variables, e.g., {'A': True, 'B': False}.
        
    Returns:
        bool: El resultado de la evaluación.
    """
    try:
        return bool(expr.subs(assignments))
    except Exception as e:
        raise ValueError(f"Error al evaluar la expresión: {e}") from e

def truth_table(expr):
    """
    Genera la tabla de verdad para una expresión lógica.
    
    Args:
        expr (sympy.Expr): La expresión lógica.
        
    Returns:
        list: Lista de diccionarios con asignaciones y resultados.
    """
    variables = sorted(expr.free_symbols, key=lambda x: x.name)
    headers = [str(var) for var in variables] + [str(expr)]
    table = []
    
    for values in product([False, True], repeat=len(variables)):
        assignment = dict(zip(variables, values))
        result = evaluate_expression(expr, assignment)
        row = {str(var): val for var, val in assignment.items()}
        row[str(expr)] = result
        table.append(row)
    
    return headers, table

