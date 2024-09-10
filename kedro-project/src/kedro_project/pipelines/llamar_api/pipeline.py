"""
This is a boilerplate pipeline 'llamar_api'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([])


import kaggle
import pandas as pd
from kedro.pipeline import Pipeline, node
from kedro.io import DataCatalog, MemoryDataSet
import os

def download_dataset_from_kaggle():
    # Verificar si el archivo ya está descargado
    csv_file_path = 'data/books.csv'  # Ajusta el nombre del archivo CSV
    if not os.path.exists(csv_file_path):
        # Si el archivo no existe, descarga el dataset desde Kaggle
        kaggle.api.dataset_download_files('jealousleopard/goodreadsbooks', path='data/', unzip=True)
    
    # Cargar el archivo CSV descargado
    df = pd.read_csv(csv_file_path)
    return df

def preprocess_data(df):
    # Realiza el preprocesamiento necesario
    df_cleaned = df.dropna()  # Ejemplo simple de eliminación de valores nulos
    return df_cleaned

# Crear el pipeline en Kedro
def create_pipeline(**kwargs):
    return Pipeline([
        node(download_dataset_from_kaggle, None, 'raw_data'),
        node(preprocess_data, 'raw_data', 'cleaned_data')
    ])

# Registro en el DataCatalog de Kedro
catalog = DataCatalog({'raw_data': MemoryDataSet(), 'cleaned_data': MemoryDataSet()})
