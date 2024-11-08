-- Datos para la tabla Usuarios
INSERT INTO Usuarios (Nombre, Apellido, Email, Telefono) VALUES
('Juan', 'Perez', 'juan.perez@mail.com', '1234567890'),
('Maria', 'Lopez', 'maria.lopez@mail.com', '0987654321'),
('Carlos', 'Gomez', 'carlos.gomez@mail.com', '5678901234'),
('Ana', 'Martinez', 'ana.martinez@mail.com', '4321098765');

-- Datos para la tabla Marca
INSERT INTO Marca (Marca, Modelo, Numero_serie) VALUES
('Samsung', 'EcoBubble', 'S1234567890123'),
('LG', 'TWINWash', 'L9876543210123'),
('Whirlpool', 'SupremeCare', 'W4567890123012'),
('Bosch', 'Serie6', 'B3210987654321');

-- Datos para la tabla Ubicacion
INSERT INTO Ubicacion (Pais, Provincia, Ciudad) VALUES
('Argentina', 'Buenos Aires', 'La Plata'),
('Argentina', 'Cordoba', 'Cordoba Capital'),
('Argentina', 'Santa Fe', 'Rosario'),
('Argentina', 'Mendoza', 'Mendoza');

-- Datos para la tabla Lavarropas
INSERT INTO Lavarropas (Fecha_compra, Estado, Ultima_revision, ID_Marca, ID_Usuario, ID_Ubicacion) VALUES
('2021-05-15', 'Activo', '2023-10-10', 1, 1, 1),
('2020-07-23', 'Revisado', '2023-09-12', 2, 2, 2),
('2022-01-05', 'Activo', '2023-11-01', 3, 3, 3),
('2019-11-18', 'Inactivo', '2022-10-15', 4, 4, 4);

-- Datos para la tabla Programa
INSERT INTO Programa (Nombre_programa) VALUES
('Eco'),
('Rápido'),
('Delicado'),
('Intensivo');

-- Datos para la tabla Fase
INSERT INTO Fase (Nombre_fase) VALUES
('Prelavado'),
('Lavado'),
('Enjuague'),
('Centrifugado');

-- Datos para la tabla Ciclo_lavado con hora y minutos
INSERT INTO Ciclo_lavado (Fecha_inicio, Fecha_fin, Volumen_carga, Tipo_ropa, ID_Lavarropas, ID_Programa) VALUES
('2024-01-10 08:30:00', '2024-01-10 10:15:00', 5.5, 'Algodón', 1, 1),
('2024-02-15 14:45:00', '2024-02-15 16:00:00', 3.0, 'Sintético', 2, 2),
('2024-03-20 09:20:00', '2024-03-20 11:05:00', 4.2, 'Lana', 3, 3),
('2024-04-25 18:10:00', '2024-04-25 20:40:00', 6.8, 'Mixto', 4, 4),
('2024-10-01 08:00:00', '2024-10-01 10:00:00', 7.5, 'Algodón', 1, 1),
('2024-10-02 09:00:00', '2024-10-02 11:00:00', 6.0, 'Sintético', 2, 2),
('2024-10-03 10:00:00', '2024-10-03 12:00:00', 5.5, 'Lana', 3, 3),
('2024-10-04 11:00:00', '2024-10-04 13:00:00', 8.0, 'Mixto', 4, 4);
-- Datos para la tabla Consumo_Lavarropas
INSERT INTO Consumo_Lavarropas (Consumo_energia, Consumo_agua, ID_Ciclo, ID_Fase) VALUES
(0.75, 45.0, 1, 1),
(0.70, 40.0, 1, 2),
(0.65, 30.0, 1, 3),
(0.70, 40.0, 1, 4),
(1.20, 55.5, 2, 2),
(0.90, 40.0, 3, 3),
(1.50, 60.2, 4, 4),
(1.00, 50.0, 5, 1),  -- Ciclo 5: Algodón, Prelavado
(0.85, 45.0, 5, 2),  -- Ciclo 5: Algodón, Lavado
(0.80, 35.0, 5, 3),  -- Ciclo 5: Algodón, Enjuague
(0.90, 50.0, 5, 4),  -- Ciclo 5: Algodón, Centrifugado
(0.75, 40.0, 6, 1),  -- Ciclo 6: Sintético, Prelavado
(0.60, 30.0, 6, 2),  -- Ciclo 6: Sintético, Lavado
(0.70, 40.0, 6, 3),  -- Ciclo 6: Sintético, Enjuague
(0.80, 45.0, 6, 4),  -- Ciclo 6: Sintético, Centrifugado
(1.10, 55.0, 7, 1),  -- Ciclo 7: Lana, Prelavado
(0.90, 50.0, 7, 2),  -- Ciclo 7: Lana, Lavado
(0.85, 30.0, 7, 3),  -- Ciclo 7: Lana, Enjuague
(1.20, 60.0, 7, 4),  -- Ciclo 7: Lana, Centrifugado
(1.30, 70.0, 8, 1),  -- Ciclo 8: Mixto, Prelavado
(1.00, 65.0, 8, 2),  -- Ciclo 8: Mixto, Lavado
(0.95, 55.0, 8, 3),  -- Ciclo 8: Mixto, Enjuague
(1.10, 75.0, 8, 4);  -- Ciclo 8: Mixto, Centrifugado
