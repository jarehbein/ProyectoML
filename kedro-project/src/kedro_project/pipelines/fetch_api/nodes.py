"""
This is a boilerplate pipeline 'fetch_api'
generated using Kedro 0.19.8
"""

import os
import pandas as pd
import kaggle
import logging
import re

logger = logging.getLogger(__name__)

def download_dataset_from_kaggle() -> str:
    """
    Descarga el dataset desde Kaggle si no existe y devuelve la ruta del archivo.
    """
    logger.info("Iniciando la descarga del dataset desde Kaggle...")
    dataset_dir = 'data/01_raw/'
    dataset_file = os.path.join(dataset_dir, 'goodreads_data.csv')

    if not os.path.exists(dataset_file):
        kaggle.api.dataset_download_files(
            'ishikajohari/best-books-10k-multi-genre-data',
            path=dataset_dir,
            unzip=True
        )
        if not os.path.exists(dataset_file):
            raise FileNotFoundError(f"El archivo {dataset_file} no se encontró después de descargar el dataset.")
    logger.info(f"Dataset descargado y guardado en: {dataset_file}")

    return dataset_file

def preprocess_data(raw_dataset_path: pd.DataFrame) -> pd.DataFrame:
    print("Leyendo el archivo CSV para preprocesamiento...")
    df = pd.read_csv(raw_dataset_path, delimiter=',', on_bad_lines='skip')
    print(f"Columnas encontradas en el archivo CSV: {df.columns}")

    # Asegurar compatibilidad de caracteres
    df = df.applymap(
        lambda x: x.encode('utf-8', 'ignore').decode('utf-8') if isinstance(x, str) else x
    )

    # Eliminar la columna innecesaria 'Unnamed: 0'
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
        logger.info("Columna 'Unnamed: 0' eliminada.")

    # Remover caracteres no imprimibles
    df.replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)

    # Normalizar columna 'Genres'
    if 'Genres' in df.columns:
        df['Genres'] = df['Genres'].apply(lambda x: eval(x)[0] if isinstance(x, str) and eval(x) else 'Unknown')

    # Limpiar y convertir 'Num_Ratings'
    if 'Num_Ratings' in df.columns:
        df['Num_Ratings'] = df['Num_Ratings'].str.replace(',', '', regex=True).astype(float)
        logger.info("Columna 'Num_Ratings' convertida a numérico.")

    # Guardar con manejo de errores
    try:
        df.to_csv("data/02_intermediate/temp_cleaned_data.csv", index=False, encoding="utf-8", errors="replace")
        print("Archivo guardado correctamente.")
    except UnicodeEncodeError as e:
        print("Error de codificación:", e)

    # Retornar el DataFrame limpio
    return df