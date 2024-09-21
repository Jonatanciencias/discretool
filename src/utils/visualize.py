""""Módulo con funciones para visualizar tablas de verdad."""
# src/utils/visualize.py

import os
import matplotlib.pyplot as plt
from datetime import datetime

EXPORT_FOLDER = "exports"

def create_export_folder():
    """Crea la carpeta 'exports' si no existe."""
    if not os.path.exists(EXPORT_FOLDER):
        os.makedirs(EXPORT_FOLDER)

def generate_filename(base_name="truth_table"):
    """Genera un nombre de archivo con siglas y la fecha de creación."""
    date_str = datetime.now().strftime("%Y%m%d")
    return f"{base_name}_TT_{date_str}.png"

def visualize_truth_table(headers, table_data, base_filename="truth_table"):
    """
    Genera una visualización gráfica de la tabla de verdad usando matplotlib.
    Guarda el gráfico en formato PNG dentro de la carpeta de exportación.
    """
    create_export_folder()  # Crear la carpeta 'exports' si no existe
    filename = generate_filename(base_filename)
    filepath = os.path.join(EXPORT_FOLDER, filename)
    
    # Preparar los datos para el gráfico
    _, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')

    # Convertir la tabla de verdad en formato adecuado para matplotlib
    data = [[str(row.get(h)) for h in headers] for row in table_data]
    headers = [header for header in headers]
    
    table = ax.table(cellText=data, colLabels=headers, loc='center', cellLoc='center')

    # Ajustar el tamaño de la tabla
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    # Guardar la figura en la carpeta 'exports'
    plt.savefig(filepath, bbox_inches='tight')
    plt.close()

    print(f"Gráfico de la tabla de verdad guardado en {filepath}")
