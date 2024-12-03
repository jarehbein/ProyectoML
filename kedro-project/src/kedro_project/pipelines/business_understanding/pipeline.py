"""
This is a boilerplate pipeline 'business_understanding'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, node
from .nodes import analyze_data, generate_insights

def create_pipeline(**kwargs) -> Pipeline:
    """
    Define y retorna el pipeline de análisis de negocio.

    Returns:
        Pipeline: Un pipeline con nodos para análisis de datos y generación de insights.
    """
    return Pipeline([
        node(
            func=analyze_data,
            inputs="cleaned_data",
            outputs="analysis_results",
            name="analyze_data_node"
        ),
        node(
            func=generate_insights,
            inputs="analysis_results",
            outputs="business_insights",
            name="generate_insights_node"
        ),
    ])
