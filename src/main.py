"""
Punto de entrada principal para el Generador de Gráficos 2D.

Este módulo ejecuta la aplicación principal que genera gráficos de barras
con datos de municipios de Antioquia.
"""

import sys
from pathlib import Path

# Agregar el directorio raíz al path para importar módulos
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from src.utils import crear_dataframe_municipios, crear_grafico_barras, mostrar_datos


def main():
    """
    Función principal que ejecuta el generador de gráficos.
    """
    # Crear DataFrame con datos de municipios
    df = crear_dataframe_municipios()
    
    # Mostrar los datos en consola
    mostrar_datos(df)
    
    # Crear y mostrar gráfico de barras
    crear_grafico_barras(
        df=df,
        columna_x="Municipio",
        columna_y="Ventas_promedio",
        titulo="Ventas promedio por municipio - Antioquia",
        color="teal"
    )


if __name__ == "__main__":
    main()

