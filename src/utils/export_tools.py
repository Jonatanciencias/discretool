""" Módulo con funciones para exportar tablas de verdad a CSV y Markdown. """
# src/utils/export_tools.py

import csv

def export_truth_table_csv(headers, table_data, filename):
    """Exporta una tabla de verdad a un archivo CSV."""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(table_data)
    print(f"Tabla de verdad exportada a {filename}.")

def export_truth_table_md(headers, table_data, filename):
    """Exporta una tabla de verdad a un archivo Markdown."""
    with open(filename, 'w') as mdfile:
        mdfile.write("| " + " | ".join(headers) + " |\n")
        mdfile.write("| " + " | ".join(["---"] * len(headers)) + " |\n")
        for row in table_data:
            row_str = " | ".join(["T" if row.get(h) else "F" for h in headers])
            mdfile.write(f"| {row_str} |\n")
    print(f"Tabla de verdad exportada a {filename}.")
