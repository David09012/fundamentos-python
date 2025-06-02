'''
Clase:        Clase 6
Tema:         Manejo de lista
Ejercicio:    Numero líder
Descripción:  Primero definí una función que conviertiera valores x en integer, para luego usar esa función en toda la lista.
              Luego solo cree una lista vacía para agregar los numeros líderes. Y por último, iteré cada índice de la lista del usuario para compararlo con el maximo numero a partir del indice siguiente, y si era mayor y no estaba en la lista vacía, se agregaba.
Autor:        David Alejandro Aguilar Aguilar
Fecha:        2025-06-2
Estado:       [ Terminado ]
'''

usuario=input()
lista_usuario1=usuario.split()
def integer(x):
    return int(x)

lista_usuario= list(map(integer,lista_usuario1))


n=1
numeros_lider=[]
for i in lista_usuario:
    if n<len(lista_usuario):
        j=max(lista_usuario[n:])
        if i > j and i not in numeros_lider:
            numeros_lider.append(i)
    n+=1
print(numeros_lider)
