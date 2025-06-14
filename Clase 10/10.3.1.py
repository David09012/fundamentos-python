'''
Clase:        Clase 10
Tema:         Matríces
Ejercicio:    10.3.1 Matríz simétrica
Descripción:    El programa le pide al usuario que ingrese una matriz cuadrada, 
                una fila a la vez, con los números separados por comas. 
                Luego, compara los elementos de la matriz con su reflejo respecto a la diagonal principal. 
                Si todos los elementos coinciden en esa simetría, le dice al usuario que la matriz es simétrica. 
                Si no, le indica que no lo es.
Autor:        David Alejandro Aguilar Aguilar
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''
def es_matriz_simetrica(matriz):
    N = len(matriz)
    for i in range(N):
        for j in range(N):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True
matriz = []
print("Ingresa una matriz cuadrada fila por fila.")
print("Cada fila debe tener los números separados por comas (ej: 1,2,3).")
print("Ejemplo de una matriz 3x3:\n1,2,3\n2,5,0\n3,0,5\n")
while True:
    fila = input(f"Fila {len(matriz) + 1}: ")
    numeros = list(map(int, fila.split(',')))

    if len(matriz) == 0:
        N = len(numeros) 

    if len(numeros) != N:
        print(f"Error: Se esperaban {N} elementos. Intenta de nuevo.")
        continue

    matriz.append(numeros)

    if len(matriz) == N:
        break
if es_matriz_simetrica(matriz):
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")