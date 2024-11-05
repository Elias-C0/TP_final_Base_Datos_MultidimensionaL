#Relizaremos las conecion de la base de datos Lavarropas de postgresql con python y tambien cargaremos el datawarehouse 
#para realizar el ETL

import psycopg2
import pandas as pd
from sqlalchemy import create_engine # Importante para la conexion con la base de datos
import os
from actualizar import actualizarTablaDimension

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

conn.close()


#generamos consulta sql de la base de datos relacional de la tabla ubicaion para luego cargarla en el datawarehouse
# Consulta sql para obtener los datos de la tabla Ubicacion




#---------------------
#dimension ubicaion
#---------------------
ubicacion = tablas['ubicacion']
print(ubicacion)

#actualizamos la tabla de ubicacion
ubicacion = actualizarTablaDimension(engine, 'ubicacion', ubicacion, pk='id_ubicacion')

#---------------------
#dimension marca
#---------------------
marca = tablas['marca']
marca = marca[['id_marca', 'marca', 'modelo']]
print(marca)
marca = actualizarTablaDimension(engine, 'marca', marca, pk='id_marca')

# -----------------------------
# Dimension fecha
# -----------------------------
tiempo = tablas['Ciclo_lavado']
tiempo = tiempo[['fecha_inicio']]

# Extraer componentes de tiempo
tiempo['anio'] = tiempo['fecha_inicio'].dt.year
tiempo['mes'] = tiempo['fecha_inicio'].dt.month
tiempo['dia'] = tiempo['fecha_inicio'].dt.day
tiempo['hora'] = tiempo['fecha_inicio'].dt.hour



# Generar id_fecha único

print(tiempo)

#cargo la tabla en el datawarehouse
tiempo = actualizarTablaDimension(engine,'tiempo', tiempo, pk='id_fecha')

#JOIN entre las tablas de la base de datos relacional 

#--------------------
#Tabla de hecho
#--------------------
fact_table = pd.DataFrame({
    #Dimensiones
    'id_tiempo': tablas['Ciclo_lavado']['id_ciclo'].astype(int), #tiempo['fecha_inicio'].map(tiempo.set_index('fecha_inicio')['id_fecha'])
    'id_ubicacion': tablas['ubicacion']['id_ubicacion'].astype(int),
    'id_marca': tablas['marca']['id_marca'].astype(int),

    #Medidas
    'numero_lavados' : tablas['Ciclo_lavado']['id_ciclo'].groupby(tablas['Ciclo_lavado']['id_ciclo']).count(),
    'consumo_total_energia_kwh': tablas['Consumo_lavaropas'].groupby('id_ciclo')['consumo_energia'].sum(),
    'consumo_total_agua_l': tablas['Consumo_lavaropas'].groupby('id_ciclo')['consumo_agua'].sum()


})
print(fact_table)

fact_table = actualizarTablaDimension(engine, 'registro_lavado', fact_table, pk='id_registro')

#dimension fecha

