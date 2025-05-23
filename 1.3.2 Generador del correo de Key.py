'''
Clase:        Clase 1
Tema:         Exploración de conceptos
Ejercicio:    Generador del correo Key
Descripción:  Genera el correo institucional usando el nombre completo del usuario

Autor:        David Alejandro Aguilar Aguilar
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''
n=input("Dime tu nombre completo: ")
m= n.split()
P_Nombre,P_Apellido= m[0],m[2]
p_nombre,p_apellido=P_Nombre.lower(),P_Apellido.lower()
print(f"{p_nombre}.{p_apellido}@keyinstitute.edu.sv")