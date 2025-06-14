'''
Clase:        Clase 10
Tema:         Matríces
Ejercicio:    Diagonal principal y secundaria
Descripción:  El usuario ingresa una matriz cuadrada fila por fila (números separados por comas).
                El programa valida que cada fila tenga el mismo número de elementos.
                Una vez completada la matriz, se calculan las diagonales:
                Principal: de arriba a la izquierda a abajo a la derecha (matriz[i][i]).
                Secundaria: de arriba a la derecha a abajo a la izquierda (matriz[i][N - i - 1]).
                Se imprimen ambas diagonales.
Autor:        David Alejandro Aguilar Aguilar y apoyo de chatgpt en la parte de como debería de ingresar los inputs.
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''
def obtener_diagonales(matriz):
    N = len(matriz)
    diagonal_principal = [matriz[i][i] for i in range(N)]
    diagonal_secundaria = [matriz[i][N - i - 1] for i in range(N)]
    return diagonal_principal, diagonal_secundaria

matriz = []
print("Ingrese cada fila, dependiendo cuantos numeros tenga tu fila, será el numero de columnas (separa cada numero con una coma).")
print("Cuando termines de ingresar N filas con N elementos cada una, se calcularán las diagonales.")

while True:
    fila = input(f"Fila {len(matriz) + 1}: ")
    numeros = list(map(int, fila.split(',')))
    if len(matriz) == 0:
        N = len(numeros)
    if len(numeros) != N:
        print(f"Error: esta fila tiene {len(numeros)} elementos, pero se esperaban {N}. Intenta de nuevo.")
        continue
    matriz.append(numeros)

    if len(matriz) == N:
        break

principal, secundaria = obtener_diagonales(matriz)
print("Diagonal principal:", principal)
print("Diagonal secundaria:", secundaria)