'''
Clase:        Clase 6
Tema:         Manejo de lista
Ejercicio:    Eliminando valores duplicados
Descripción:  Le pido un conjunto de numeros al usuario, lo convierto en lista con espacios, creo una lista vacia, y comparo los la lista vacia con la lista del usuario, si el numero no esta en la lista vacia, lo agregra, y si esta, no hace nada.

Autor:        David Alejandro Aguilar Aguilar
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''
x=input("Dame una lista de numeros: ")
lista= x.split()
z=[]
for i in x:
    if i not in z:
        z.append(i)
for i in z:
    print(i,end=" ")
