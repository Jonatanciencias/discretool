""" Módulo para generar tablas de verdad de expresiones lógicas. """
# src/logic/truth_table.py

from sympy.logic.boolalg import truth_table as sympy_truth_table
from src.utils.export_tools import export_to_csv, export_to_md
from src.utils.visualize import visualize_truth_table

def truth_table(expr):
    """
    Genera una tabla de verdad para una expresión lógica.
    Retorna los encabezados y los datos de la tabla de verdad.
    """
    symbols_in_expr = sorted(expr.free_symbols, key=str)
    headers = [str(sym) for sym in symbols_in_expr] + [str(expr)]
    table_data = []

    for row in sympy_truth_table(expr, symbols_in_expr):
        truth_values = [bool(val) for val in row]  # Asegurarse de que los valores sean booleanos
        evaluated_expr = expr.subs(zip(symbols_in_expr, truth_values))  # Evaluar la expresión
        truth_row = {str(sym): val for sym, val in zip(symbols_in_expr, truth_values)}
        truth_row[str(expr)] = bool(evaluated_expr)  # Convertir el resultado a booleano
        table_data.append(truth_row)

    return headers, table_data

def export_truth_table_csv(headers, table_data, filename="truth_table"):
    """
    Exporta la tabla de verdad a un archivo CSV usando la función export_to_csv del módulo export_tools.
    """
    export_to_csv(headers, table_data, filename)

def export_truth_table_md(headers, table_data, filename="truth_table"):
    """
    Exporta la tabla de verdad a un archivo Markdown usando la función export_to_md del módulo export_tools.
    """
    export_to_md(headers, table_data, filename)

def export_truth_table_graph(headers, table_data, filename="truth_table"):
    """
    Exporta una representación gráfica de la tabla de verdad usando la función visualize_truth_table.
    """
    visualize_truth_table(headers, table_data, filename)
