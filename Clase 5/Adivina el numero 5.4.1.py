'''
Clase:        Clase 5
Tema:         Loops for y while
Ejercicio:    Adivina el numero
Descripción:  

Autor:        David Alejandro Aguilar Aguilar
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''
import random
num=random.randrange(1,100)
i=int(input("Ingrese un numero entero entre 1 y 100: "))
if num ==i:
    print(f"¡Felicidades: Has adivinado el numero secreto: {i}\n Fin del juego " )
elif num !=i:
    while num!=i:
        if i<num:
            print("El numero secreto es mayor que tu numero")
            i=int(input("Ingrese un numero entero entre 1 y 100: "))
        elif i>num:
            print("El numero secreto es menor que tu numero")
            i=int(input("Ingrese un numero entero entre 1 y 100: "))
    print(f"¡Felicidades: Has adivinado el numero secreto: {i}\n Fin del juego " )
        