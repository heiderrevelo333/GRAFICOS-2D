"""
Módulo de utilidades para el generador de gráficos 2D.

Este módulo contiene funciones auxiliares para la creación y visualización
de gráficos de datos de municipios.
"""

import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Optional


def crear_dataframe_municipios() -> pd.DataFrame:
    """
    Crea un DataFrame con datos ficticios de municipios de Antioquia.
    
    Returns:
        pd.DataFrame: DataFrame con columnas 'Municipio', 'Ventas_promedio' y 'Poblacion_aprox'
    """
    data = {
        "Municipio": [
            "Medellín", "Envigado", "Bello", "Itagüí", 
            "Rionegro", "La Ceja", "Santa Fe de Antioquia"
        ],
        "Ventas_promedio": [150000, 80000, 60000, 70000, 50000, 30000, 25000],
        "Poblacion_aprox": [2500000, 250000, 500000, 280000, 160000, 60000, 25000]
    }
    return pd.DataFrame(data)


def crear_grafico_barras(
    df: pd.DataFrame,
    columna_x: str,
    columna_y: str,
    titulo: str,
    color: str = "teal",
    figsize: tuple = (10, 6)
) -> None:
    """
    Crea y muestra un gráfico de barras a partir de un DataFrame.
    
    Args:
        df: DataFrame con los datos a graficar
        columna_x: Nombre de la columna para el eje X
        columna_y: Nombre de la columna para el eje Y
        titulo: Título del gráfico
        color: Color de las barras (por defecto "teal")
        figsize: Tamaño de la figura (ancho, alto)
    """
    plt.figure(figsize=figsize)
    plt.bar(df[columna_x], df[columna_y], color=color)
    
    # Personalizar el gráfico
    plt.title(titulo, fontsize=14)
    plt.xlabel(columna_x, fontsize=12)
    plt.ylabel(columna_y, fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()


def mostrar_datos(df: pd.DataFrame) -> None:
    """
    Muestra los datos del DataFrame en la consola.
    
    Args:
        df: DataFrame a mostrar
    """
    print("\n" + "="*50)
    print("Datos de Municipios de Antioquia")
    print("="*50)
    print(df)
    print("="*50 + "\n")

