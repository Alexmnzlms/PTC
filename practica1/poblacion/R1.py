# -*- coding: utf-8 -*-

import csv
import numpy as np

datos = open("entradas/poblacionProvinciasHM2010-17.csv", "r", encoding="utf-8")

tabla = datos.read()

datos.close()

primero = tabla.find("Total")
ultimo = tabla.find("Notas")

print(primero)
print(ultimo)

tabla = tabla[primero:ultimo]

print(tabla)

data = tabla.split("\n")

data = np.array(data)

print(data)

matrix = np.array([])
for i in data:
    aux = np.array(i.split(";"))
    print(aux)
    matrix = np.append(matrix, aux)

print(matrix)
print(np.shape(matrix))

matrix = np.delete(matrix,0,0)




#print("\nFichero leido final es\n",cadenaFinal)
