SELECT AVG(temperatura) AS media_temperatura
FROM telemetry;

SELECT MAX(vibracao) AS maior_vibracao
FROM telemetry;

SELECT *
FROM telemetry
WHERE temperatura > 100
OR vibracao > 4;