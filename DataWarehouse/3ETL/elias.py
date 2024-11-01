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

try: #Se intentna ejecutar este bloque, en caso de error se ejecuta el except
    # Conexión a la base de datos transaccional
    Base_de_datos.autocommit = True
    trans_cursor = Base_de_datos.cursor()
    
    query = "SELECT Fecha_inicio FROM ciclo_lavado;" #creamos la consulta SQL
    trans_cursor.execute(query) #ejecutamos la consulta de arriba

    fechas = trans_cursor.fetchall() #Recupera todos los resultados de la consulta ejecutada

    df = pd.DataFrame(fechas, columns=["Fecha_inicio"])

    # Extraer componentes de tiempo
    df['anio'] = df['Fecha_inicio'].dt.year
    df['mes'] = df['Fecha_inicio'].dt.month
    df['dia'] = df['Fecha_inicio'].dt.day
    df['hora'] = df['Fecha_inicio'].dt.hour

    # Conexión al data warehouse
    dw_cursor = DataWhareHouse.cursor()

    dw_cursor.execute("SELECT COALESCE(MAX(id_fecha), 0) FROM Tiempo;") #sacamos el ultimo ID de la tabla Tiempo para que no haya duplicados
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

    DataWhareHouse.commit() #Commit de la transacción en el data warehouse

except Exception as e: #en caso de error imprimos el error
    print(f"Error: {e}")

finally: #cerramos los cursores y las conexiones
    trans_cursor.close()
    Base_de_datos.close()
    dw_cursor.close()
    DataWhareHouse.close()
