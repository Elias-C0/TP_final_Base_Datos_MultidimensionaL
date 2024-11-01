# Importamos las librerias
import psycopg2
import pandas as pd

# Conexión a la base de datos transaccional
#=========================================================================================================

# Conexión Elias
# Base_de_datos = psycopg2.connect(
#     dbname="Lavarropas TP final BDM",
#     user="postgres",
#     password="1234",
#     host="localhost",
#     port="5432"
# )

# Conexión Axel
# Base_de_datos = psycopg2.connect(
#     host="localhost",
#     database="Lavarropas",
#     user="postgres",
#     password="1234"
# )

# Conexión Ayrton
Base_de_datos = psycopg2.connect(
    dbname="TP Final Relacional",
    user="postgres",
    password="carrera-12345",
    host="localhost",
    port="5432"
)
#=========================================================================================================

# Conexión al data warehouse
#=========================================================================================================

# Conexión Elias
# DataWhareHouse = psycopg2.connect(
#     dbname="datawharehouse",
#     user="postgres",
#     password="1234",
#     host="localhost",
#     port="5432"
# )

# Conexión Axel
# DataWhareHouse = psycopg2.connect(
#     dbname="Lavarropas_DW",
#     user="postgres",
#     password="1234",
#     host="localhost",
#     port="5432"
# )

# Conexión Ayrton
DataWhareHouse = psycopg2.connect(
    dbname="TP Final DW",
    user="postgres",
    password="carrera-12345",
    host="localhost",
    port="5432"
)
#=========================================================================================================

# 