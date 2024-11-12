from datetime import datetime, timedelta
import psycopg2
import random
import string

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

#======== | programa | ================
programas = ["eco", "rapido", "delicado", "intensivo"]

programas_generados = []
for _ in range(num_registros):
    programa = random.choice(programas)
    programas_generados.append((programa,))  # Cada programa debe ser una tupla con un solo valor

# Insertar datos en la tabla 'programa'
columnas = ["nombre_programa"]
insert_data("programa", columnas, programas_generados)

#======== | Marca | ================
marcas= ["Samsung", "LG", "Whirlpool", "Bosch", "Electrolux", "BGH", "Top_House", "Xiaomi"]
modelos = ["EcoBubble", "TWINWash", "SupremeCare", "Serie6", "SmartDrive", "Quicker", "PowerClean", "EcoSmart"]

#generar un numero de serie unico (para el numero de serie)
def generar_numero_serie():
    return random.choice(string.ascii_uppercase) + ''.join(random.choices(string.digits, k=10)) #con el K decidis la longitud

# Generar datos aleatorios para la tabla Marca
marcas_data = [(random.choice(marcas), random.choice(modelos), generar_numero_serie()) for x in range(num_registros)]

columnas= ["marca","modelo","numero_serie"]
insert_data("Marca",columnas,marcas_data) # Ejecutamos la insercion

#======== | Ubicacion | ================
paises = ["Argentina", "Uruguay", "Paraguay"]

# Provincias asignadas a cada país
provincias_por_pais = {
    "Argentina": ["Buenos Aires", "Cordoba", "Santa Fe", "Mendoza", "Salta", "Entre Rios", "Tucuman"],
    "Uruguay": ["Montevideo", "Canelones", "Maldonado"],
    "Paraguay": ["Asunción", "Central", "Alto Paraná"]
}

# Ciudades para las provincias de Argentina
ciudades_por_provincia = {
    "Buenos Aires": ["La Plata", "Mar del Plata", "Bahía Blanca"],
    "Cordoba": ["Cordoba Capital", "Villa Carlos Paz", "Río Cuarto"],
    "Santa Fe": ["Rosario", "Santa Fe Capital", "Rafaela"],
    "Mendoza": ["Mendoza", "San Rafael", "Godoy Cruz"],
    "Salta": ["Salta Capital", "Tartagal", "Orán"],
    "Entre Rios": ["Paraná", "Concordia", "Gualeguaychú"],
    "Tucuman": ["San Miguel de Tucumán", "Tafí Viejo", "Concepción"],
    # Ciudades para las provincias de Uruguay
    "Montevideo": ["Montevideo", "La Paz", "Ciudad de la Costa"],
    "Canelones": ["Canelones", "Pando", "Santa Lucia"],
    "Maldonado": ["Maldonado", "Punta del Este", "San Carlos"],
    # Ciudades para las provincias de Paraguay
    "Asunción": ["Asunción", "Lambaré", "San Lorenzo"],
    "Central": ["Areguá", "Luque", "Fernando de la Mora"],
    "Alto Paraná": ["Ciudad del Este", "Hernandarias", "Presidente Franco"]
}

#Generamos los datos aleatorios
ubicaciones = []
for _ in range(num_registros):
    pais = random.choice(paises)
    provincia = random.choice(provincias_por_pais[pais])
    ciudad = random.choice(ciudades_por_provincia[provincia])# Asigna una ciudad segun el pais y provincia seleccionada
    ubicaciones.append((pais, provincia, ciudad))

# Ejecutar la inserción
columnas = ["Pais","Provincia","Ciudad"]
insert_data("Ubicacion", columnas, ubicaciones)

#======== | Usuario | ================
nombres = ["Juan", "Maria", "Carlos", "Ana", "Luis", "Sofia", "Pedro", "Laura", "Miguel", "Lucia", 
           "Jorge", "Valentina", "Fernando", "Camila", "Pablo", "Florencia", "Hernan", "Julieta", "Alberto", "Martina"]
apellidos = ["Perez", "Lopez", "Gomez", "Martinez", "Garcia", "Fernandez", "Escalante", "Rodriguez", "Diaz", "Silva",
             "Morales", "Ramirez", "Romero", "Suarez", "Herrera", "Gonzalez", "Rojas", "Castro", "Milessi", "Mendez"]

# Generar lista de usuarios
usuarios = []
dominio_email = ["example.com", "correo.com", "mail.com", "gmail.com", "outlook.es", "outlook.es", "yahoo.ar", "hotmail.com", "hotmail.com.ar"]
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

#======== | Consumo_lavarropas | ================


#======== | Ciclo_lavado | ================



#======== | Lavarropas | ================
#Generamos fechas aleatorias en un rango
def random_date(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Listas de posibles estados
estados = ["Activo", "Inactivo", "Revisado"]

id_marcas = list(range(0,num_registros+1))
id_usuarios = list(range(0, num_registros+1))
id_ubicaciones = list(range(0, num_registros+1))

lavarropas_data = []
# Generar datos aleatorios para la tabla Lavarropas
for _ in range(num_registros):
    fecha_compra = random_date(2018, 2024).strftime('%Y-%m-%d')
    estado = random.choice(estados)  # Estado aleatorio
    ultima_revision = random_date(2022, 2024).strftime('%Y-%m-%d')
    id_marca = random.choice(id_marcas)
    id_usuario = random.choice(id_usuarios)
    id_ubicacion = random.choice(id_ubicaciones)

    # Añadir tupla a la lista de datos
    lavarropas_data.append((fecha_compra, estado, ultima_revision, id_marca, id_usuario, id_ubicacion))

columnas = ["Fecha_compra", "Estado", "Ultima_revision", "ID_Marca", "ID_Usuario", "ID_Ubicacion"]
insert_data("Lavarropas", columnas, lavarropas_data)
conn.close()

# #================================
# #para visualizar como queda
# import pandas as pd
# a= pd.DataFrame(marcas_data)
# print(a)
# #================================