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

# Codigo para el cuestionario cuestionario
consumo_hogar5_viernes = consumo[4, 4]
print(f"Consumo del hogar 5 el viernes: {consumo_hogar5_viernes}")

consumo_ultimos3_domingo = consumo[-3:, 6]
print(f"Consumo de los últimos 3 hogares el domingo: {consumo_ultimos3_domingo}")

promedio_finde = np.mean(consumo[:, 5:7], axis=1)
print(f"Promedio de consumo en fines de semana por hogar: {promedio_finde}")

desviacion_dias = np.std(consumo, axis=0)
dia_mayor_desviacion = np.argmax(desviacion_dias)
print(f"Día con mayor desviación estándar: {dia_mayor_desviacion}")
print(f"Desviaciones por día: {desviacion_dias}")

consumo_total_hogar = np.sum(consumo, axis=1)
indices_menor_consumo = np.argsort(consumo_total_hogar)[:3]
valores_menor_consumo = consumo_total_hogar[indices_menor_consumo]
print(f"Índices de los 3 hogares con menor consumo: {indices_menor_consumo}")
print(f"Valores de consumo: {valores_menor_consumo}")

consumo_hogar3_incrementado = consumo[2] * 1.10
nuevo_consumo_total_hogar3 = np.sum(consumo_hogar3_incrementado)
print(f"Nuevo consumo total del hogar 3 con aumento del 10%: {nuevo_consumo_total_hogar3}")

'''
1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
El consumo del hogar 5 el viernes fue de 17.4 unidades.

2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
Los consumos del domingo para los últimos 3 hogares (hogares 8, 9 y 10) fueron:
[12.0, 16.7, 9.3] unidades respectivamente.

3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
El promedio de consumo en sábado y domingo por hogar fue:
[14.65, 11.9, 15.9, 9.85, 17.9, 12.65, 14.95, 12.1, 16.85, 9.4] unidades.

4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
El día con mayor desviación estándar fue el sábado (índice 5) con una desviación de aproximadamente 2.74 unidades.
Esto indica que el consumo de los hogares ese día varió más que en cualquier otro, es decir, hubo más desigualdad o variabilidad en el consumo entre los diferentes hogares durante el sábado.

5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
Los tres hogares con menor consumo total fueron:

Índice 9 con 62.6 unidades

Índice 3 con 66.1 unidades

Índice 1 con 77.1 unidades

6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
El nuevo consumo total del hogar 3 tras un aumento del 10% diario sería de aproximadamente 114.95 unidades.

'''