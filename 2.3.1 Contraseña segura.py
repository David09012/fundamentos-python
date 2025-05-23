'''
Clase:        Clase 2
Tema:         Bloque if, elif, else
Ejercicio:    Contraseña segura
Descripción:  Revisa la contraseña que el usuario crea, y a partir del numero de digitos que contenga, o de letras, reconoce si la contraseña es segura o no

Autor:        David Alejandro Aguilar Aguilar
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''
c="Ishish99"
if len(c)>=8:
    for i in c:
        if i.isdigit or i.isupper:
            pass
    print("Contraseña segura")
else:
    print("Contraseña no segura")
    