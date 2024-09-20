""" Módulo para generar y exportar tablas de verdad. """
import csv
import os
from sympy.logic.boolalg import truth_table as sympy_truth_table

EXPORT_FOLDER = "exports"

def create_export_folder():
    """
    Crea la carpeta de exportación si no existe.
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
        truth_values = [val for val in row]
        table_data.append({str(sym): val for sym, val in zip(headers, truth_values)})

    return headers, table_data

def export_truth_table_csv(headers, table_data, filename="truth_table.csv"):
    """
    Exporta la tabla de verdad a un archivo CSV.
    """
    create_export_folder()
    filepath = os.path.join(EXPORT_FOLDER, filename)
    
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(table_data)

def export_truth_table_md(headers, table_data, filename="truth_table.md"):
    """
    Exporta la tabla de verdad a un archivo Markdown.
    """
    create_export_folder()
    filepath = os.path.join(EXPORT_FOLDER, filename)
    
    md_content = f"| {' | '.join(headers)} |\n"
    md_content += f"| {' | '.join(['---' for _ in headers])} |\n"
    for row in table_data:
        row_str = ' | '.join(['T' if row.get(h) else 'F' for h in headers])
        md_content += f"| {row_str} |\n"
    
    with open(filepath, mode='w', encoding='utf-8') as file:
        file.write(md_content)
