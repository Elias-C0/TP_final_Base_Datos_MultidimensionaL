import psycopg2
import random
import string
from modulos.update_dimensions_table import actualizarTablaDimension

#Base de datos relacional
conn = psycopg2.connect(
    host="localhost",
    database="Lavarropas",
    user="postgres",
    password="1234")

def insert_data(table, columnas, datos):
    columnas_str = ", ".join(columnas)
    placeholders = ", ".join(["%s"] * len(columnas))
    insert_query = f"INSERT INTO {table} ({columnas_str}) VALUES ({placeholders})"
    with conn.cursor() as cursor:
        cursor.executemany(insert_query, datos)
    conn.commit()

num_registros = 500 #cantidad de registors a generar

#======== base relacional | Marca | ================
marcas= ["Samsung", "LG", "Whirlpool", "Bosch", "Electrolux", "BGH", "Top_House", "Xiaomi"]
modelos = ["EcoBubble", "TWINWash", "SupremeCare", "Serie6", "SmartDrive", "Quicker", "PowerClean", "EcoSmart"]

#generar un numero de serie unico (para el numero de serie)
def generar_numero_serie():
    return random.choice(string.ascii_uppercase) + ''.join(random.choices(string.digits, k=10)) #con el K decidis la longitud

# Generar datos aleatorios para la tabla Marca
marcas_data = [(random.choice(marcas), random.choice(modelos), generar_numero_serie()) for x in range(num_registros)]

columnas= ["marca","modelo","numero_serie"]
insert_data("Marca",columnas,marcas_data) # Ejecutamos la insercion

#======== base relacional | Ubicacion | ================
#agrego mas paises
provincias = ["Buenos Aires", "Cordoba", "Santa Fe", "Mendoza", "Salta", "Entre Rios", "Tucuman"]
# Ciudades para cada provincia
ciudades_por_provincia = {
    "Buenos Aires": ["La Plata", "Mar del Plata", "Bahía Blanca"],
    "Cordoba": ["Cordoba Capital", "Río Cuarto"],
    "Santa Fe": ["Rosario", "Rafaela"],
    "Mendoza": ["Mendoza", "San Rafael", "Godoy Cruz"],
    "Salta": ["Salta Capital", "Tartagal", "Orán"],
    "Entre Rios": ["Paraná", "Concordia", "Gualeguaychú"],
    "Tucuman": ["San Miguel de Tucumán", "Tafí Viejo", "Concepción"]
}

ubicaciones = []
for x in range(num_registros):
    pais = "Argentina"
    provincia = random.choice(provincias)
    ciudad = random.choice(ciudades_por_provincia[provincia])
    ubicaciones.append((pais, provincia, ciudad))

# Ejecutar la inserción
columnas= ["Pais", "Provincia", "Ciudad"]
insert_data("Ubicacion", columnas, ubicaciones)

#======== | Usuario | ================
nombres = ["Juan", "Maria", "Carlos", "Ana", "Luis", "Sofia", "Pedro", "Laura", "Miguel", "Lucia", 
           "Jorge", "Valentina", "Fernando", "Camila", "Pablo", "Florencia", "Hernan", "Julieta", "Alberto", "Martina"]
apellidos = ["Perez", "Lopez", "Gomez", "Martinez", "Garcia", "Fernandez", "Escalante", "Rodriguez", "Diaz", "Silva",
             "Morales", "Ramirez", "Romero", "Suarez", "Herrera", "Gonzalez", "Rojas", "Castro", "Milessi", "Mendez"]

# Generar lista de usuarios
usuarios = []
dominio_email = ["example.com", "correo.com", "mail.com", "gmail.com","outlook.es","outlook.es","yahoo.ar"]
emails_generados = set()  # Set para almacenar emails únicos generados

for _ in range(num_registros):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    email = f"{nombre.lower()}.{apellido.lower()}@{random.choice(dominio_email)}"
    
    # Verificar si el email ya fue generado
    while email in emails_generados:
        # Si el email ya existe, genera uno nuevo
        email = f"{nombre.lower()}.{apellido.lower()}_{random.randint(1, 99)}@{random.choice(dominio_email)}"
    
    emails_generados.add(email)  # Añadir el email al set de únicos
    
    telefono = "".join([str(random.randint(0, 9)) for _ in range(10)])  # Número de 10 dígitos
    usuarios.append((nombre, apellido, email, telefono))

columnas= ["Nombre","Apellido","Email","Telefono"]
insert_data("Usuarios", columnas, usuarios)

#======== | programa | ================
programas = ["eco", "rapido", "delicado", "intensivo"]

programas_generados = []  # Lista para almacenar los programas generados

for x in range(num_registros):
    programa = random.choice(programas)
    programas_generados.append(programa)

columnas= ["nombre_programa"]
insert_data("programa", columnas, programas_generados)

#======== | fase | ================
programas = ["Prelavado", "Lavado", "Enjuague", "Centrifugado"]
Nombre_fase_generados = []

# Generación de datos aleatorios
for x in range(num_registros):
    programa = random.choice(programas)
    Nombre_fase_generados.append((programa,))  # Convertir cada valor en una tupla

# Definir las columnas
columnas = ["Nombre_fase"]
insert_data("Fase", columnas, Nombre_fase_generados)
conn.close()

#======== | Consumo_lavarropas | ================


#======== | Ciclo_lavado | ================



#======== | Lavarropas | ================
# import datetime

# # Variables de ejemplo
# estados = ['Activo', 'Revisado', 'Inactivo']

# # Función para generar una fecha aleatoria dentro de un rango
# def generar_fecha_aleatoria(fecha_inicio, fecha_fin):
#     delta = fecha_fin - fecha_inicio
#     rand_days = random.randint(0, delta.days)
#     return fecha_inicio + datetime.timedelta(days=rand_days)

# # Definir las fechas de inicio y fin para las compras
# fecha_inicio = datetime.datetime(2018, 1, 1)
# fecha_fin = datetime.datetime(2023, 12, 31)

# # Generar registros aleatorios para la tabla Lavarropas
# lavarropas = []
# for _ in range(num_registros):
#     fecha_compra = generar_fecha_aleatoria(fecha_inicio, fecha_fin).strftime('%Y-%m-%d')
#     estado = random.choice(estados)
#     ultima_revision = generar_fecha_aleatoria(fecha_inicio, fecha_fin).strftime('%Y-%m-%d')
#     id_marca = random.randint(1, 8)  # Asumimos que hay 4 marcas disponibles
#     id_usuario = random.randint(1, num_registros)  # Asumimos que hay 25 usuarios
#     id_ubicacion = random.randint(1, num_registros)  # Asumimos que hay 25 ubicaciones

#     lavarropas.append((fecha_compra, estado, ultima_revision, id_marca, id_usuario, id_ubicacion))

# # Ahora lavarropas contiene los datos aleatorios generados
# print(lavarropas)

# columnas= ["fecha_compra","estado", "ultima_revision", "id_marca", "id_usuario", "id_ubicacion"]
# #insert_data("Lavarropas", columnas, lavarropas)

# conn.close()

# #================================
# #para visualizar como queda
# import pandas as pd
# a= pd.DataFrame(marcas_data)
# print(a)
# #================================