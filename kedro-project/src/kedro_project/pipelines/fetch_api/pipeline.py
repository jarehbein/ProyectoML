"""
This is a boilerplate pipeline 'fetch_api'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, node
from .nodes import download_dataset_from_kaggle, preprocess_data

def create_pipeline(**kwargs) -> Pipeline:
    """
    Define y retorna el pipeline de la API fetch.

    Returns:
        Pipeline: Un pipeline con nodos para descargar y preprocesar los datos.
    """
    return Pipeline([
        node(
            func=download_dataset_from_kaggle,
            inputs=None,
            outputs="raw_dataset_path",
            name="download_dataset_node"
        ),
        node(
            func=preprocess_data,
            inputs="raw_dataset_path",
            outputs="cleaned_data",
            name="preprocess_data_node"
        )
    ])
