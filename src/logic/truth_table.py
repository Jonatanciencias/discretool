""" Módulo para generar y exportar tablas de verdad de expresiones lógicas. """

# src/logic/truth_table.py

import csv
import os
from sympy.logic.boolalg import truth_table as sympy_truth_table

# Obtener la ruta absoluta de la raíz del proyecto
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORT_FOLDER = os.path.join(ROOT_DIR, "exports")


def create_export_folder():
    """
    Crea la carpeta de exportación en la raíz del proyecto si no existe.
    """
    if not os.path.exists(EXPORT_FOLDER):
        os.makedirs(EXPORT_FOLDER)


def truth_table(expr):
    """
    Genera una tabla de verdad para una expresión lógica.
    Retorna los encabezados y los datos de la tabla de verdad.
    """
    symbols_in_expr = sorted(expr.free_symbols, key=str)
    headers = [str(sym) for sym in symbols_in_expr] + [str(expr)]
    table_data = []

    for row in sympy_truth_table(expr, symbols_in_expr):
        truth_values = [
            bool(val) for val in row
        ]  # Asegurarse de que los valores sean booleanos
        evaluated_expr = expr.subs(
            zip(symbols_in_expr, truth_values)
        )  # Evaluar la expresión con los valores de verdad
        truth_row = {str(sym): val for sym, val in zip(symbols_in_expr, truth_values)}
        truth_row[str(expr)] = bool(evaluated_expr)  # Convertir el resultado a booleano
        table_data.append(truth_row)

    return headers, table_data


def export_truth_table_csv(headers, table_data, filename="truth_table.csv"):
    """
    Exporta la tabla de verdad a un archivo CSV en la carpeta 'exports' en la raíz del proyecto.
    """
    create_export_folder()
    filepath = os.path.join(EXPORT_FOLDER, filename)

    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(table_data)


def export_truth_table_md(headers, table_data, filename="truth_table.md"):
    """
    Exporta la tabla de verdad a un archivo Markdown en 
    la carpeta 'exports' en la raíz del proyecto.
    """
    create_export_folder()
    filepath = os.path.join(EXPORT_FOLDER, filename)

    md_content = f"| {' | '.join(headers)} |\n"
    md_content += f"| {' | '.join(['---' for _ in headers])} |\n"
    for row in table_data:
        row_str = (
            " | ".join(["T" if row.get(h) else "F" for h in headers[:-1]])
            + f" | {row[headers[-1]]}"
        )
        md_content += f"| {row_str} |\n"

    with open(filepath, mode="w", encoding="utf-8") as file:
        file.write(md_content)

    print(f"Tabla de verdad exportada a {filename}.")
