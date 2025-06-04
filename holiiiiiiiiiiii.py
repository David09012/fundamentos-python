import numpy as np


consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

print("Dimensiones:", consumo.ndim)          # 2 (filas y columnas)
print("Forma:", consumo.shape)               # (10, 7) → 10 filas y 7 columnas
print("Tipo de datos:", consumo.dtype)       # float64 (números decimales)
print("Consumo primer hogar:", consumo[0])   # Todos los datos de la fila 0
print("Consumo el miércoles (día 3):", consumo[:, 2])  # Todos los datos de la columna 2

promedio_por_hogar = np.mean(consumo, axis=1)
promedio_por_dia = np.mean(consumo, axis=0)
total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

maximos = np.max(consumo, axis=1)
minimos = np.min(consumo, axis=0)
desviacion = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion)

consumo_total_hogar = np.sum(consumo, axis=1)
hogar_mayor_consumo = np.argmax(consumo_total_hogar)
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)

consumo_total_hogar = np.sum(consumo, axis=1)
print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")
altos = consumo_total_hogar > 100
consumo_mayor_100 = np.where(altos)[0]

print(f"IDs de hogares con consumo mayor a 100: {consumo_mayor_100}")

consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())

print(consumo_normalizado)