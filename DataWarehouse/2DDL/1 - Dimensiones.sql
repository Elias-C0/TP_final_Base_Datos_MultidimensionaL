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
Anio INT,
Mes INT,
Dia INT,
Hora INT,
Fecha_inicio TIMESTAMP,
PRIMARY KEY (Anio, Mes, Dia, Hora)
);

--Tabla de hechos

CREATE TABLE registro_Lavado (
id_registro SERIAL PRIMARY KEY,
ID_ubicacion INT NOT NULL,
ID_marca INT NOT NULL,
Numero_lavados INT,
Anio INT,
Mes INT,
Dia INT,
Hora INT,
Consumo_total_energia_kWh DECIMAL(10, 2),
Consumo_total_agua_L DECIMAL(10, 2),
FOREIGN KEY (ID_ubicacion) REFERENCES Ubicacion(ID_ubicacion),
FOREIGN KEY (ID_marca) REFERENCES Marca(ID_marca),
FOREIGN KEY (Anio, Mes, Dia, Hora) REFERENCES Tiempo(Anio, Mes, Dia, Hora)
);