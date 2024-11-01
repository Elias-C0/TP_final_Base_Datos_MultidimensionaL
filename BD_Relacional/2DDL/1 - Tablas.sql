-- Table: Usuarios
CREATE TABLE Usuarios (
	ID_Usuarios SERIAL PRIMARY KEY,
	Nombre CHAR(20) NOT NULL,
	Apellido CHAR(20),
	Email CHAR(25) UNIQUE NOT NULL,
	Telefono CHAR(20)
);

-- Table: Marca
CREATE TABLE Marca (
	ID_Marca SERIAL PRIMARY KEY,
	Marca CHAR(20),
	Modelo CHAR(20),
	Numero_serie CHAR(25)
);

-- Table: Ubicacion
CREATE TABLE Ubicacion(
	ID_Ubicacion SERIAL PRIMARY KEY,
	Pais CHAR(20),
	Provincia CHAR(20),
	Ciudad CHAR(20)
);

-- Table: Lavaropas
CREATE TABLE Lavaropas (
	ID_Lavaropas SERIAL PRIMARY KEY,
	Fecha_compra DATE,
	Estado CHAR(20),
	Ultima_revision DATE,
	ID_Marca INT,
	ID_Usuario INT,
	ID_Ubicacion INT,
	FOREIGN KEY (ID_Marca) REFERENCES Marca(ID_Marca),
	FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuarios),
	FOREIGN KEY (ID_Ubicacion) REFERENCES Ubicacion(ID_Ubicacion)
);
-- Table: Programa
CREATE TABLE Programa (
	ID_Programa SERIAL PRIMARY KEY,
	Nombre_programa CHAR(20) NOT NULL
);

-- Table: Fase
CREATE TABLE Fase (
	ID_Fase SERIAL PRIMARY KEY,
	Nombre_fase CHAR(20) NOT NULL
);

-- Table: Ciclo_lavado
CREATE TABLE Ciclo_lavado (
	ID_Ciclo SERIAL PRIMARY KEY,
	Fecha_inicio TIMESTAMP NOT NULL,
	Fecha_fin TIMESTAMP,
	Volumen_carga DECIMAL(10, 2),
	Tipo_ropa CHAR(20),
	ID_Lavaropas INT,
	ID_Programa INT,
	FOREIGN KEY (ID_Lavaropas) REFERENCES Lavaropas(ID_Lavaropas),
	FOREIGN KEY (ID_Programa) REFERENCES Programa(ID_Programa)
);

-- Table: Consumo_lavaropas
CREATE TABLE Consumo_lavaropas (
	ID_Consumo SERIAL PRIMARY KEY,
	Consumo_energia DECIMAL(10, 2) NOT NULL, -- kWh
	Consumo_agua DECIMAL(10, 2) NOT NULL, -- Liters
	ID_Ciclo INT,
	ID_Fase INT,
	FOREIGN KEY (ID_Ciclo) REFERENCES Ciclo_lavado(ID_Ciclo),
	FOREIGN KEY (ID_Fase) REFERENCES Fase(ID_Fase)
);