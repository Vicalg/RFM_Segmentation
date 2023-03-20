# Importando las librerías y módulos necesarios
# Importar el módulo os para interactuar con el sistema operativo.
import os

# Importar el módulo pandas para manipular y analizar datos.
import pandas as pd

# Importar la clase text del módulo sqlalchemy para crear consultas SQL.
from sqlalchemy import text

# Importar la función engine_create del módulo db_engine para crear un objeto engine para conectarse a la base de datos.
from db_engine import engine_create


# Definiendo variables globales
nombre_archivo = "rfm.pkl"                      # Asignar el nombre del archivo donde se guardará el DataFrame.


def create_datafile(nombre_archivo=nombre_archivo) -> None:
    """Función para crear un archivo de datos a partir de una consulta SQL.

    Args:
        nombre_archivo (str): Nombre del archivo a crear.

    Returns:
        None
    """
    # Crear el objeto engine para conectarse a la base de datos utilizando la función engine_create del módulo db_engine.
    engine = engine_create()

    with engine.connect() as connection:
        # Definir una consulta SQL para obtener la tabla con la información necesaria para calcular el RFM utilizando la clase text del módulo sqlalchemy.
        query = text("""
            WITH cte_time AS(
                SELECT order_id, customer_id, order_purchase_timestamp
                FROM orders
            ),
            cte_payments AS(
                SELECT order_id, payment_value
                FROM order_payments
            ),
            cte_timepay AS(
                SELECT t.customer_id AS customer_id,
                       t.order_purchase_timestamp AS purchase_date,
                       p.payment_value AS amount
                FROM cte_time AS t
                JOIN cte_payments AS p ON t.order_id = p.order_id
            )
            SELECT *
            FROM cte_timepay""")
        
        # Ejecutar la consulta y almacenar el resultado en un DataFrame de Pandas utilizando la función read_sql_query del módulo pandas.
        df = pd.read_sql_query(query, connection)

        # Liberar los recursos utilizados por el objeto engine utilizando su método dispose.
        engine.dispose()

    # Construir la ruta del archivo donde se guardará el DataFrame utilizando las funciones dirname y join del módulo os.
    path_parent = os.path.dirname(os.getcwd())
    path_archivo = os.path.join(path_parent, "data", nombre_archivo)

    # Guardar el DataFrame en un archivo pickle utilizando su método to_pickle.
    df.to_pickle(path_archivo)

    return None