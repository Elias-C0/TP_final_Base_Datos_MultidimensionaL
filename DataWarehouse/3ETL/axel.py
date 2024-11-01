#Relizaremos las conecion de la base de datos Lavarropas de postgresql con python y tambien cargaremos el datawarehouse 
#para realizar el ETL

import psycopg2
import pandas as pd
from sqlalchemy import create_engine # Importante para la conexion con la base de datos
import os

# Conexion con la base de datos
conn = psycopg2.connect(
    host="localhost",
    database="Lavarropas",
    user="postgres",
    password="1234"
)

# realizamos una consulta para ver los datos de la tabla
cur = conn.cursor()
cur.execute("""SELECT 
    ID_Ciclo,
    SUM(Consumo_energia) AS Consumo_total_energia,
    SUM(Consumo_agua) AS Consumo_total_agua
FROM 
    Consumo_lavaropas
GROUP BY 
    ID_Ciclo;""")
rows = cur.fetchall()
print(rows)

# conexion con el datawarehouse
engine = create_engine('postgresql://postgres:1234@localhost:5432/Lavarropas_DW')

#guardamos las tablas de la base de datos relacional que utilizaremos en dataframes
listas_tablas = ['Consumo_lavaropas', 'Ciclo_lavado', 'Lavaropas','fase','marca','programa', 'ubicacion', 'usuarios' ]

tablas = {}
for tabla in listas_tablas:
    query = f'SELECT * FROM {tabla}'
    tablas[tabla] = pd.read_sql(query, conn)

#conn.close()


#generamos consulta sql de la base de datos relacional de la tabla ubicaion para luego cargarla en el datawarehouse
# Consulta sql para obtener los datos de la tabla Ubicacion



def actualizarTablaDimension(engine, table, data, pk="id"):
    """
    Esta función actualiza una tabla de dimensión de un DW con los datos nuevos. Si los datos
    ya existen en la tabla, no se agregan. Devuelve la tabla actualizada con los pk tal cual esta
    en la base de datos.

    La tabla de dimensión debe estar creada y las columnas deben llamarse igual que en el df.

    Parametros:
        engine: engine de la base de datos
        table: nombre de la tabla
        data: datafarme de datos nuevos a agregar, sin incluir la PK
        pk: nombre de la PK. Por defecto es "ID"

    Retorno:
        dimension_df: datafarme con la tabla según está en la DB con los datos nuevos agregados.

    """
    with engine.connect() as conn, conn.begin():
        old_data = pd.read_sql_table(table, conn)

        # Borro la columna pk
        old_data.drop(pk, axis=1, inplace=True)

        # new_data es el datafarme de datos diferencia de conjunto con old_data
        new_data = data[~data.stack().isin(old_data.stack().values).unstack().astype(bool)].dropna()

        # insertar new_data
        new_data.to_sql(table, conn, if_exists='append', index=False)

        # buscar como quedó la tabla
        dimension_df = pd.read_sql_table(table, conn)

    return dimension_df

#dimension ubicaion
query= 'SELECT * FROM ubicacion'

ubicacion = pd.read_sql(query, conn)
print(ubicacion)

#actualizamos la tabla de ubicacion
ubicacion = actualizarTablaDimension(engine, 'ubicacion', ubicacion, pk='id_ubicacion')

#dimension marca
query2= 'SELECT id_marca, marca, modelo FROM  marca'
marca = pd.read_sql(query2, conn)
print(marca)

marca = actualizarTablaDimension(engine, 'marca', marca, pk='id_marca')

#dimension fecha

