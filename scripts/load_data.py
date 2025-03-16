import pandas as pd

def load_wine_data(red_wine_path="../data/raw/winequality-red.csv",
                   white_wine_path="../data/raw/winequality-white.csv"):
    """
    Carga los datasets de vinos tintos y blancos, agrega una columna 'wine_type' y los combina en un solo DataFrame.

    Parámetros:
        red_wine_path (str): Ruta del archivo CSV de vinos tintos.
        white_wine_path (str): Ruta del archivo CSV de vinos blancos.

    Retorna:
        pd.DataFrame: DataFrame combinado con los datos de vino tinto y blanco.
    """
    # Cargar datasets
    df_red = pd.read_csv(red_wine_path, sep=";")
    df_white = pd.read_csv(white_wine_path, sep=";")

    # Agregar una columna "wine_type" para identificar el tipo de vino
    df_red["wine_type"] = "red"
    df_white["wine_type"] = "white"

    # Combinar ambos datasets en uno solo
    df_wine = pd.concat([df_red, df_white], ignore_index=True)
    
    return df_wine, df_red, df_white
