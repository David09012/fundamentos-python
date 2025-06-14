"""
Sistema de emparejamiento:
- Algoritmo para asignar tutor a tutorado según materias y disponibilidad.
- Posibilidad de búsqueda manual por parte del tutorado.
- Recomendaciones automáticas.

Pseudocódigo:

"""
import json
with open("Tutores.json", "r") as file:
    Tutores=json.load(file)

print(f"{Tutores[0]["Tutor"]}\n{Tutores[0]["Materias"]}")

for algortimo in Tutores:
    print(algortimo)
    
