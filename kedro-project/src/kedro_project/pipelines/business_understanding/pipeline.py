from kedro.pipeline import Pipeline, node
import pandas as pd

# Nodo: Análisis inicial de variables clave
def analyze_key_variables(df: pd.DataFrame):
    """
    Analiza las variables clave para entender el negocio.
    
    Args:
        df: DataFrame de libros.
    
    Returns:
        dict: Resumen con conteo de géneros, autores más populares y promedio de calificaciones.
    """
    # Conteo de géneros
    genres_count = df["Genres"].value_counts().to_dict()
    
    # Autores con más libros
    popular_authors = df["Author"].value_counts().head(5).to_dict()
    
    # Promedio de calificaciones
    avg_rating = df["Avg_Rating"].mean()

    # Resumen
    summary = {
        "genres_count": genres_count,
        "popular_authors": popular_authors,
        "avg_rating": avg_rating,
    }

    return summary


# Pipeline
def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=analyze_key_variables,
                inputs="cleaned_data",  # Viene del pipeline `fetch_api`
                outputs="business_summary",  # Salida del análisis inicial
                name="analyze_key_variables_node",
            )
        ]
    )
