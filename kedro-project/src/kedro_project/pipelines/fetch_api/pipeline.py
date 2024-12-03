"""
This is a boilerplate pipeline 'fetch_api'
generated using Kedro 0.19.8
"""

import kaggle
import os
from kedro.pipeline import Pipeline, node

def download_dataset_from_kaggle():
    # Define el directorio de destino
    dataset_dir = 'data/01_raw/'
    dataset_file = os.path.join(dataset_dir, 'goodreads_data.csv')

    # Verificar si el archivo ya existe
    if not os.path.exists(dataset_file):
        # Descarga y descomprime el dataset desde Kaggle
        kaggle.api.dataset_download_files(
            'ishikajohari/best-books-10k-multi-genre-data', 
            path=dataset_dir, 
            unzip=True
        )

        # Verifica si el archivo CSV existe después de la descarga
        if not os.path.exists(dataset_file):
            raise FileNotFoundError(f"El archivo {dataset_file} no se encontró después de descargar el dataset.")

    return dataset_file  # Devuelve la ruta al archivo descargado

# Crear el pipeline en Kedro
def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=download_dataset_from_kaggle,
            inputs=None,
            outputs="raw_dataset_path",
            name="download_dataset_node"
        )
    ])
