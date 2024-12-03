import os
import pandas as pd
import logging

def download_dataset_from_kaggle():
    # Define la ruta del directorio y del archivo CSV
    dataset_dir = "data/01_raw/"
    dataset_file = os.path.join(dataset_dir, "goodreads_data.csv")

    # Verificar si el directorio existe, y si no, crearlo
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)
        logging.info(f"Directorio {dataset_dir} creado.")

    # Verificar si el archivo ya existe
    if not os.path.exists(dataset_file):
        raise FileNotFoundError(
            f"El archivo {dataset_file} no fue encontrado. Por favor, asegúrate de que esté en la ubicación correcta o descárgalo."
        )

    logging.info(f"El archivo {dataset_file} fue encontrado. Cargando datos...")

    # Leer el archivo CSV con encoding seguro
    return pd.read_csv(dataset_file, encoding="utf-8", on_bad_lines="skip")
