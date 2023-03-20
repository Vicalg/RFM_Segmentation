# Cargando todas las librerías necesarias
# Manipulación de la base de datos y lectura de credenciales
import sqlalchemy
from sqlalchemy import create_engine

# Librerías para ubicar paths y cargar información
import os
import json

# Manipulación de dataframes y cálculos
import pandas as pd

# Cargando la información para acceder a la base de datos
# Creando los paths relativos
path_parent = os.path.dirname(os.getcwd())
path_info = path_parent + '\\info.json'


def load_info(path_info=path_info) -> dict:
    """
    Carga la información de un archivo JSON en un diccionario.

    Args:
        path_info (str): Ruta del archivo JSON que contiene la información a cargar.

    Returns:
        dict: Diccionario con la información cargada desde el archivo JSON.
    """

    # Leyendo las credenciales para la conexión
    with open(path_info, 'rb') as file:
        info = json.load(file)
    
    return info


def engine_create(path_info=path_info) -> sqlalchemy.engine.base.Engine:
    """Crea un objeto engine para conectarse a una base de datos PostgreSQL.

    Utiliza la información de conexión almacenada en el archivo especificado por `path_info`.

    Args:
        path_info (str): Ruta al archivo que contiene la información de conexión a la base de datos.

    Returns:
        sqlalchemy.engine.Engine: Objeto engine para conectarse a la base de datos PostgreSQL.
    """

    # Loading information required for the connection
    info = load_info(path_info)

    # Creando engine con las credenciales
    # Crear un objeto engine para conectarse a la base de datos PostgreSQL
    engine = create_engine(f"postgresql+psycopg2://{info['usuario']}:{info['contraseña']}@{info['hostname']}/{info['database']}")

    # Borrar variable con las credenciales
    del info

    return engine