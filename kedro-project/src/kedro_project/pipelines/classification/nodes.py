import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import logging

logger = logging.getLogger(__name__)

def prepare_data(cleaned_data: pd.DataFrame):
    """
    Prepara los datos para entrenamiento y prueba.
    """
    logger.info("Preparando datos para entrenamiento y prueba...")
    
    # Dividir características (X) y etiquetas (y)
    X = cleaned_data.drop(columns=["Genre"])
    y = cleaned_data["Genre"]
    
    # Dividir en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    return X_train, X_test, y_train, y_test

def train_random_forest(X_train, y_train):
    """
    Entrena un modelo Random Forest.
    """
    logger.info("Entrenando modelo Random Forest...")
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)
    return rf_model

def train_logistic_regression(X_train, y_train):
    """
    Entrena un modelo de Regresión Logística.
    """
    logger.info("Entrenando modelo de Regresión Logística...")
    lr_model = LogisticRegression(max_iter=1000, random_state=42)
    lr_model.fit(X_train, y_train)
    return lr_model

def train_svc(X_train, y_train):
    """
    Entrena un modelo Support Vector Classifier (SVC).
    """
    logger.info("Entrenando modelo SVC...")
    svc_model = SVC(random_state=42)
    svc_model.fit(X_train, y_train)
    return svc_model

def evaluate_model(model, X_test, y_test, model_name: str):
    """
    Evalúa un modelo con el conjunto de prueba.
    """
    logger.info(f"Evaluando el modelo {model_name}...")
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)
    
    logger.info(f"Precisión del modelo {model_name}: {accuracy:.2f}")
    return {
        "model_name": model_name,
        "accuracy": accuracy,
        "classification_report": report
    }

def select_best_model(evaluation_results):
    """
    Selecciona el mejor modelo basado en la precisión.
    """
    logger.info("Seleccionando el mejor modelo basado en precisión...")
    best_model = max(evaluation_results, key=lambda x: x["accuracy"])
    logger.info(f"El mejor modelo es {best_model['model_name']} con una precisión de {best_model['accuracy']:.2f}")
    return best_model

def combine_evaluations(rf_evaluation, lr_evaluation, svc_evaluation):
    return {
        "Random Forest": rf_evaluation,
        "Logistic Regression": lr_evaluation,
        "SVC": svc_evaluation,
    }
