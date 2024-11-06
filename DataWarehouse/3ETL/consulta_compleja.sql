SELECT 
    EXTRACT(YEAR FROM cl.fecha_inicio) AS Anio,
    EXTRACT(MONTH FROM cl.fecha_inicio) AS Mes,
    EXTRACT(DAY FROM cl.fecha_inicio) AS Dia,
    u.ID_ubicacion,
    l.ID_Lavarropas,
    COUNT(cl.ID_ciclo) AS Numero_lavados,
    SUM(clv.Consumo_energia) AS Consumo_total_energia_kwh,
    SUM(clv.Consumo_agua) AS Consumo_total_agua_l
FROM 
    Ciclo_lavado cl
JOIN 
    Consumo_Lavarropas clv ON cl.ID_ciclo = clv.ID_ciclo
JOIN 
    Lavarropas l ON cl.ID_Lavarropas = l.ID_Lavarropas
JOIN 
    Ubicacion u ON l.ID_ubicacion = u.ID_ubicacion
JOIN 
	Marca m ON l.id_marca = m.id_marca
GROUP BY 
    Anio, Mes, Dia, u.ID_ubicacion, l.ID_Lavarropas, m.id_marca;

