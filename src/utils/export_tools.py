""" Módulo con funciones para exportar la tabla de verdad a CSV o Markdown. """
# src/utils/export_tools.py

import csv
import os
from datetime import datetime

# Obtener la ruta de la carpeta 'exports' en la raíz del proyecto
EXPORT_FOLDER = "exports"

def create_export_folder():
    """Crea la carpeta 'exports' en la raíz del proyecto si no existe."""
    if not os.path.exists(EXPORT_FOLDER):
        os.makedirs(EXPORT_FOLDER)
        print(f"Created export folder at: {EXPORT_FOLDER}")
    else:
        print(f"Using existing export folder at: {EXPORT_FOLDER}")

def get_timestamped_filename(base_name, extension):
    """
    Genera un nombre de archivo con el formato:
    truth_table_YYYYMMDD_HHMMSS.csv o truth_table_YYYYMMDD_HHMMSS.md.
    """
    # Verificar si el nombre base ya incluye la extensión, y eliminarla si es necesario
    if base_name.endswith(f".{extension}"):
        base_name = base_name[:-len(extension)-1]
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}.{extension}"

def export_to_csv(headers, table_data, base_name="truth_table"):
    """
    Exporta los datos de la tabla de verdad a un archivo CSV.
    """
    create_export_folder()
    filename = get_timestamped_filename(base_name, "csv")
    filepath = os.path.join(EXPORT_FOLDER, filename)

    print(f"Exporting to CSV at: {filepath}")
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

    print(f"Exporting to Markdown at: {filepath}")
    md_content = f"| {' | '.join(headers)} |\n"
    md_content += f"| {' | '.join(['---' for _ in headers])} |\n"
    for row in table_data:
        row_str = " | ".join(["T" if row.get(h) else "F" for h in headers[:-1]]) + f" | {row[headers[-1]]}"
        md_content += f"| {row_str} |\n"

    with open(filepath, mode="w", encoding="utf-8") as file:
        file.write(md_content)

    print(f"Tabla de verdad exportada a {filepath}")
