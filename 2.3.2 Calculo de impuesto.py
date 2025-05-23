'''
Clase:        Clase 2
Tema:         Bloque if, elif, else
Ejercicio:    Cálculo de impuestos
Descripción:  A partir del numero de unidades contenidas, se calcula el impuesto a pagar por unidad

Autor:        David Alejandro Aguilar Aguilar
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''
UC=250
if UC<=100:
    print("Sin impuestos")
elif 101<=UC<=200:
    x=UC*0.5
    print(f"$0.5 por cada unidad: ${x}")
elif UC>=201:
    x=UC*0.7
    print(f"$0.7 por cada unidad: ${x}")
