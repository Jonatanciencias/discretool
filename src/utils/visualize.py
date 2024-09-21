# src/utils/visualize.py

import os
import matplotlib.pyplot as plt
from datetime import datetime

EXPORT_FOLDER = "exports"

def create_export_folder():
    """Crea la carpeta 'exports' si no existe."""
    if not os.path.exists(EXPORT_FOLDER):
        os.makedirs(EXPORT_FOLDER)

def generate_filename(base_name="truth_table", extension="png"):
    """Genera un nombre de archivo con la sigla 'TT' (Truth Table) y la fecha de creación."""
    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_TT_{date_str}.{extension}"

def ask_user_for_table_settings():
    """
    Solicita al usuario que ingrese ciertos parámetros de visualización para personalizar la tabla.
    """
    print("Configura las opciones de la tabla:")
    font_size = input("Tamaño de fuente (predeterminado 10): ") or "10"
    scale_x = input("Escala horizontal (predeterminado 1.2): ") or "1.2"
    scale_y = input("Escala vertical (predeterminado 1.2): ") or "1.2"
    
    return int(font_size), float(scale_x), float(scale_y)

def visualize_truth_table(headers, table_data, base_filename="truth_table"):
    """
    Genera una visualización gráfica de la tabla de verdad usando matplotlib.
    Permite al usuario ajustar configuraciones antes de exportar el gráfico.
    """
    create_export_folder()  # Crear la carpeta 'exports' si no existe
    filename = generate_filename(base_filename, "png")
    filepath = os.path.join(EXPORT_FOLDER, filename)

    # Preguntar al usuario por ajustes antes de generar el gráfico
    font_size, scale_x, scale_y = ask_user_for_table_settings()

    # Preparar los datos para el gráfico
    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')

    # Convertir la tabla de verdad en formato adecuado para matplotlib
    data = [[str(row.get(h)) for h in headers] for row in table_data]
    
    # Crear la tabla en el gráfico
    table = ax.table(cellText=data, colLabels=headers, loc='center', cellLoc='center')

    # Ajustar el tamaño de la tabla según la configuración del usuario
    table.auto_set_font_size(False)
    table.set_fontsize(font_size)
    table.scale(scale_x, scale_y)

    # Guardar la figura en la carpeta 'exports'
    plt.savefig(filepath, bbox_inches='tight')
    plt.close()

    print(f"Gráfico de la tabla de verdad guardado en {filepath}")
