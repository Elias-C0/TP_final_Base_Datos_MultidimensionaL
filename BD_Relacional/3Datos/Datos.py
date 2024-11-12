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

def random_datetime_combinado(start, end, include_time=False):
    """
    Genera una fecha aleatoria en un rango de fechas.
    :param start: Fecha de inicio (datetime).
    :param end: Fecha de fin (datetime).
    :param include_time: Si es True, incluye horas, minutos y segundos. Si es False, solo devuelve una fecha.
    :return: Fecha aleatoria generada dentro del rango.
    """
    if include_time:
        return start + timedelta(
            seconds=random.randint(0, int((end - start).total_seconds()))
        )
    else:
        # Genera solo la fecha sin hora
        return start + timedelta(
            days=random.randint(0, (end - start).days)
        )

num_registros = 500 #cantidad de registors a generar
IDs= list(range(1, num_registros + 1))

#======== | programa | ================
programas = ["eco", "rapido", "delicado", "intensivo"]

programas_generados = []
for _ in range(num_registros):
    programa = random.choice(programas)
    programas_generados.append((programa,))  # Cada programa debe ser una tupla con un solo valor

# Insertar datos en la tabla "programa"
columnas = ["nombre_programa"]
insert_data("programa", columnas, programas_generados)

#======== | Marca | ================
marcas= ["Samsung", "LG", "Whirlpool", "Drean", "Electrolux", "BGH", "Top_House", "Xiaomi", "Gafa"]
modelos = ["EcoBubble", "TWINWash", "SupremeCare", "Serie6", "SmartDrive", "Quicker", "PowerClean", "EcoSmart"]

#generar un numero de serie unico (para el numero de serie)
def generar_numero_serie():
    return random.choice(string.ascii_uppercase) + "".join(random.choices(string.digits, k=10)) #con el K decidis la longitud

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
           "Jorge", "Valentina", "Fernando", "Camila", "Pablo", "Florencia", "Hernan", "Julieta", "Alberto", "Martina", "Axel", "Adriel"]
apellidos = ["Perez", "Lopez", "Gomez", "Martinez", "Garcia", "Fernandez", "Escalante", "Rodriguez", "Diaz", "Silva",
             "Morales", "Ramirez", "Romero", "Suarez", "Herrera", "Gonzalez", "Rojas", "Castro", "Milessi", "Mendez", "Gallegos", "Gareis"]

# Generar lista de usuarios
usuarios = []
dominio_email = ["example.com", "correo.com", "mail.com", "gmail.com", "outlook.es", "outlook.com", "yahoo.ar", "hotmail.com", "hotmail.com.ar"]
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
fases = ["Prelavado", "Lavado", "Enjuague", "Centrifugado"]
Nombre_fase_generados = []

# Generación de datos aleatorios
for x in range(num_registros):
    Fase_aux = random.choice(fases)
    Nombre_fase_generados.append((Fase_aux,))  # Convertir cada valor en una tupla

# Definir las columnas
columnas = ["Nombre_fase"]
insert_data("Fase", columnas, Nombre_fase_generados)

#======== | Lavarropas | ================
estados = ["Activo", "Inactivo", "Revisado"]

lavarropas_data = []
# Generar datos aleatorios para la tabla Lavarropas
for _ in range(num_registros):
    #generar fecha de compra y ultima revision con o sin hora
    fecha_compra = random_datetime_combinado(datetime(2018, 1, 1), datetime(2024, 12, 31), include_time=True).strftime("%Y-%m-%d %H:%M:%S")
    estado = random.choice(estados)  # Estado aleatorio
    ultima_revision = random_datetime_combinado(datetime(2022, 1, 1), datetime(2024, 12, 31), include_time=True).strftime("%Y-%m-%d %H:%M:%S")
    id_marca = random.choice(IDs)
    id_usuario = random.choice(IDs)
    id_ubicacion = random.choice(IDs)

    # Añadir tupla a la lista de datos
    lavarropas_data.append((fecha_compra, estado, ultima_revision, id_marca, id_usuario, id_ubicacion))

columnas = ["Fecha_compra", "Estado", "Ultima_revision", "ID_Marca", "ID_Usuario", "ID_Ubicacion"]
insert_data("Lavarropas", columnas, lavarropas_data)

#======== | Ciclo_lavado | ================
volumen_rango = (1.0, 10.0)  #entre 1 a 10kg
tipos_ropa = ["Algodón", "Sintético", "Lana", "Mixto"]
id_programas = list(range(1, len(programas)))

ciclos_lavado_data = []
# Rango de fechas para el ciclo de lavado (por ejemplo entre 2024-01-01 y 2024-12-31)
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

for _ in range(num_registros):
    #Generamos una fecha de inicio aleatoria
    fecha_inicio = random_datetime_combinado(start_date, end_date, include_time=True).strftime("%Y-%m-%d %H:%M:%S")

    #Se elije un programa random y si es eco o rapido se ponen 30 o 45 minutos
    programa = random.choice(programas)
    if programa in ["eco", "rapido"]:
        duracion_minutos = random.randint(30, 45)
    else:
        duracion_minutos = random.randint(60, 120)
    
    # Calcular la fecha de fin sumando la duración al inicio
    fecha_fin = (datetime.strptime(fecha_inicio, "%Y-%m-%d %H:%M:%S") + timedelta(minutes=duracion_minutos)).strftime("%Y-%m-%d %H:%M:%S")
    
    volumen_carga = round(random.uniform(*volumen_rango), 1) #genera un volumen de carga aleatorio dentro del rango
    tipo_ropa = random.choice(tipos_ropa)

    #Seleccionamos un ID de forma aleatoria
    id_lavarropas_selected = random.choice(IDs) 
    id_programa_selected = random.choice(id_programas)

    # Añadir la tupla de datos al listado
    ciclos_lavado_data.append((fecha_inicio, fecha_fin, volumen_carga, tipo_ropa, id_lavarropas_selected, id_programa_selected))

columnas = ["Fecha_inicio", "Fecha_fin", "Volumen_carga", "Tipo_ropa", "ID_Lavarropas", "ID_Programa"]
insert_data("Ciclo_lavado", columnas, ciclos_lavado_data)

#======== | Consumo_Lavarropas | ================
# Rango de consumo de energía y agua por fase
consumo_energia_rango = {
    1: (0.6, 0.8),
    2: (0.5, 0.7),
    3: (0.4, 0.6),
    4: (0.5, 0.7)
}
consumo_agua_rango = {
    1: (40.0, 50.0),
    2: (30.0, 45.0),
    3: (25.0, 35.0),
    4: (30.0, 45.0)
}

consumo_lavado_data = []
for id_ciclo in IDs:
    for fase in range(1, 5):  # Las fases van de 1 a 4
        consumo_energia = round(random.uniform(*consumo_energia_rango[fase]), 2)  # Genera consumo de energía dentro del rango
        consumo_agua = round(random.uniform(*consumo_agua_rango[fase]), 1)  # Genera consumo de agua dentro del rango
        
        # Añadir los datos de consumo para cada fase
        consumo_lavado_data.append((consumo_energia, consumo_agua, id_ciclo, fase))

# Definir las columnas y ejecutar la inserción de datos
columnas = ["Consumo_energia", "Consumo_agua", "ID_Ciclo", "ID_Fase"]
insert_data("Consumo_Lavarropas", columnas, consumo_lavado_data)

conn.close()
print("Datos generados correctamente")