# src/utils/export_tools.py

import csv
import os
from datetime import datetime

# Obtener la ruta de la carpeta 'exports' en la raíz del proyecto
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORT_FOLDER = os.path.join(ROOT_DIR, "exports")

def create_export_folder():
    """Crea la carpeta 'exports' si no existe."""
    if not os.path.exists(EXPORT_FOLDER):
        os.makedirs(EXPORT_FOLDER)

def get_timestamped_filename(base_name, extension):
    """
    Genera un nombre de archivo con una marca de tiempo.
    Ejemplo: base_name_20230915.csv
    """
    timestamp = datetime.now().strftime("%Y%m%d")
    return f"{base_name}_{timestamp}.{extension}"

def export_to_csv(headers, table_data, base_name="truth_table"):
    """
    Exporta los datos de la tabla de verdad a un archivo CSV.
    """
    create_export_folder()
    filename = get_timestamped_filename(base_name, "csv")
    filepath = os.path.join(EXPORT_FOLDER, filename)

    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(table_data)

    print(f"Tabla de verdad exportada a {filepath}")

def export_to_md(headers, table_data, base_name="truth_table"):
    """
    Exporta los datos de la tabla de verdad a un archivo Markdown (MD).
    """
    create_export_folder()
    filename = get_timestamped_filename(base_name, "md")
    filepath = os.path.join(EXPORT_FOLDER, filename)

    md_content = f"| {' | '.join(headers)} |\n"
    md_content += f"| {' | '.join(['---' for _ in headers])} |\n"
    for row in table_data:
        row_str = " | ".join(["T" if row.get(h) else "F" for h in headers[:-1]]) + f" | {row[headers[-1]]}"
        md_content += f"| {row_str} |\n"

    with open(filepath, mode="w", encoding="utf-8") as file:
        file.write(md_content)

    print(f"Tabla de verdad exportada a {filepath}")
