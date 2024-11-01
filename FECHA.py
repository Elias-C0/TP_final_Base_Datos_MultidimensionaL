import psycopg2
import pandas as pd

# Conexión al sistema transaccional
Base_de_datos = psycopg2.connect(
    dbname="Lavarropas TP final BDM",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

# Conexión al data warehouse
DataWhareHouse = psycopg2.connect(
    dbname="datawharehouse",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

try:
    # Conexión a la base de datos transaccional
    Base_de_datos.autocommit = True
    trans_cursor = Base_de_datos.cursor()

    # Consulta para extraer datos del sistema transaccional
    query = "SELECT Fecha_inicio FROM ciclo_lavado;"
    trans_cursor.execute(query)
    fechas = trans_cursor.fetchall()

    # Convertir los resultados a un DataFrame
    df = pd.DataFrame(fechas, columns=["Fecha_inicio"])

    # Extraer componentes de tiempo
    df['anio'] = df['Fecha_inicio'].dt.year
    df['mes'] = df['Fecha_inicio'].dt.month
    df['dia'] = df['Fecha_inicio'].dt.day
    df['hora'] = df['Fecha_inicio'].dt.hour

    # Conexión al data warehouse
    dw_cursor = DataWhareHouse.cursor()

    # Obtener el último ID de la tabla Tiempo
    dw_cursor.execute("SELECT COALESCE(MAX(id_fecha), 0) FROM Tiempo;")
    contador = dw_cursor.fetchone()[0] + 1

    # Insertar datos en la tabla del data warehouse
    for _, row in df.iterrows():
        insert_query = """
        INSERT INTO Tiempo (id_fecha, anio, mes, dia, hora)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
        """
        dw_cursor.execute(insert_query, (contador, row['anio'], row['mes'], row['dia'], row['hora']))
        contador += 1

    
    DataWhareHouse.commit() # Commit de la transacción en el data warehouse

except Exception as e:
    print(f"Error: {e}")

finally:
    # Cerrar cursores y conexiones
    trans_cursor.close()
    Base_de_datos.close()
    dw_cursor.close()
    DataWhareHouse.close()
