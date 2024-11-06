-- Dimension ubicacion

CREATE TABLE Ubicacion (
ID_ubicacion INT PRIMARY KEY,
Pais CHAR(20),
Provincia CHAR(20),
Ciudad CHAR(20)
);

-- Dimension marca

CREATE TABLE Marca (
ID_marca INT PRIMARY KEY,
Marca CHAR(20),
Modelo CHAR(20)
);

--Dimension tiempo

CREATE TABLE Tiempo (
ID_fecha serial PRIMARY KEY,
Fecha_inicio TIMESTAMP,
Anio INT,
Mes INT,
Dia INT,
Hora INT
);

--Tabla de hechos

CREATE TABLE Registro_Lavado (
id_registro SERIAL PRIMARY KEY,
ID_tiempo INT NOT NULL,
ID_ubicacion INT NOT NULL,
ID_marca INT NOT NULL,
Numero_lavados INT,
Consumo_total_energia_kWh DECIMAL(10, 2),
Consumo_total_agua_L DECIMAL(10, 2),
FOREIGN KEY (ID_tiempo) REFERENCES Tiempo(ID_fecha),
FOREIGN KEY (ID_ubicacion) REFERENCES Ubicacion(ID_ubicacion),
FOREIGN KEY (ID_marca) REFERENCES marca(ID_marca)
);