'''
Clase:        Clase 10
Tema:         Matríces
Ejercicio:    10.3.2 Juego del entorno
Descripción:  
Autor:        David Alejandro Aguilar Aguilar y sugerencia de chatgpt para usar el for anidado 4 veces.
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''


n = int(input("Ingresa el número de filas (N): "))
m = int(input("Ingresa el número de columnas (M): "))
matriz = []
print("Ahora ingresa la matriz binaria (solo 0 o 1), separados por comas:")
for i in range(n):
    fila_texto = input(f"Fila {i+1}: ")
    fila = list(map(int, fila_texto.split(','))) 
    matriz.append(fila)
resultado = []
for i in range(n):
    fila_resultado = []
    for j in range(m):
        suma_vecinos = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue 
                ni = i + dx
                nj = j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    suma_vecinos += matriz[ni][nj]
        fila_resultado.append(suma_vecinos)
    resultado.append(fila_resultado)
print("\nMatriz resultado:")
for fila in resultado:
    print(fila)