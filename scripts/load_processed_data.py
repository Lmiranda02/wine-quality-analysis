import pandas as pd
import os

def load_processed_data(data_path="../data/processed/"):
    """
    Carga los datasets preprocesados de entrenamiento y prueba.

    Parámetros:
        data_path (str): Ruta de la carpeta donde están los archivos preprocesados.

    Retorna:
        tuple: (X_train, X_test, y_train, y_test) como DataFrames y Series de pandas.
    """
    # Definir rutas de los archivos
    X_train_path = os.path.join(data_path, "X_train.csv")
    X_test_path = os.path.join(data_path, "X_test.csv")
    y_train_path = os.path.join(data_path, "y_train.csv")
    y_test_path = os.path.join(data_path, "y_test.csv")

    # Cargar los datos
    X_train = pd.read_csv(X_train_path)
    X_test = pd.read_csv(X_test_path)
    y_train = pd.read_csv(y_train_path).squeeze()  # Convertir a Serie
    y_test = pd.read_csv(y_test_path).squeeze()  # Convertir a Serie

    print("✅ Datos preprocesados cargados correctamente.")
    
    return X_train, X_test, y_train, y_test
