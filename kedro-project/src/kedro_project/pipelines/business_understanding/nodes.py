"""
This is a boilerplate pipeline 'business_understanding'
generated using Kedro 0.19.8
"""

import pandas as pd
import logging
import seaborn as sb
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

def analyze_data(cleaned_data: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza un análisis exploratorio del dataset limpio.

    Args:
        cleaned_data (pd.DataFrame): El dataset limpio.

    Returns:
        pd.DataFrame: Un resumen del análisis exploratorio.
    """
    logger.info("Iniciando el análisis exploratorio del dataset limpio...")
    # Descripción básica del dataset
    analysis_summary = cleaned_data.describe(include="all").T
    logger.info(f"Resumen del dataset:\n{analysis_summary}")

    # Identificar valores faltantes
    missing_data = cleaned_data.isnull().sum()
    logger.info(f"Valores faltantes por columna:\n{missing_data}")

    # Visualización de valores faltantes
    plt.figure(figsize=(10, 6))
    sb.heatmap(cleaned_data.isnull(), cbar=False, cmap="viridis")
    plt.title("Mapa de calor de valores faltantes")
    plt.savefig("data/08_reporting/missing_data_heatmap.png")
    logger.info("Mapa de calor de valores faltantes guardado en data/08_reporting/missing_data_heatmap.png")

    return analysis_summary

def generate_insights(analysis_results: pd.DataFrame) -> dict:
    """
    Genera insights basados en el análisis exploratorio.
    """
    logger.info("Generando insights a partir del análisis...")
    
    if analysis_results.empty:
        raise ValueError("El DataFrame analysis_results está vacío.")

    total_rows = len(analysis_results)
    columns_with_missing_data = analysis_results.isnull().sum().to_dict()
    numeric_columns = analysis_results.select_dtypes(include=["number"]).columns.tolist()

    insights = {
        "total_rows": total_rows,
        "columns_with_missing_data": columns_with_missing_data,
        "numeric_columns": numeric_columns,
    }

    logger.info("Insights generados correctamente.")
    return insights
