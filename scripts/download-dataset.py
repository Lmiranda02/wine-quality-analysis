import os
import requests
import pandas as pd
from zipfile import ZipFile
from io import BytesIO

# Definir URLs y rutas de almacenamiento
dataset_url = "https://archive.ics.uci.edu/static/public/186/wine+quality.zip"
data_dir = "data/raw/"
zip_path = os.path.join(data_dir, "wine_quality.zip")

# Crear directorio si no existe
os.makedirs(data_dir, exist_ok=True)

# Descargar el dataset
print("Descargando dataset...")
response = requests.get(dataset_url)
if response.status_code == 200:
    with open(zip_path, "wb") as f:
        f.write(response.content)
    print("Descarga completa. Extrayendo archivos...")

    # Extraer archivos
    with ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(data_dir)

    os.remove(zip_path)
    print("Extracción completa. Archivos guardados en:", data_dir)
else:
    print("Error al descargar el dataset:", response.status_code)

# Cargar y mostrar los archivos disponibles
files = os.listdir(data_dir)
print("Archivos descargados:", files)

csv_files = [f for f in files if f.endswith(".csv")]
if csv_files:
    df = pd.read_csv(os.path.join(data_dir, csv_files[0]), sep=";")
    print("Primeras filas del dataset:")
    print(df.head())
else:
    print("No se encontraron archivos CSV en la carpeta descargada.")
