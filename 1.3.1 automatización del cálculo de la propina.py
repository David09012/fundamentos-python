'''
Clase:        Clase 1
Tema:         Exploración de conceptos
Ejercicio:    Automatización del cálculo de una propina
Descripción:  Calcula el pago total de una cuenta, tomando en cuenta el porcentaje de propina que se debe pagar

Autor:        David Alejandro Aguilar Aguilar
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''
cuenta = 57
porcentaje_p= 10
propina = (porcentaje_p * cuenta) / 100
Total = cuenta+propina
print(f"Total de la cuenta: ${cuenta} \nPropina: ${propina} \nTotal de la cuenta con propina({porcentaje_p}%): ${Total}")
