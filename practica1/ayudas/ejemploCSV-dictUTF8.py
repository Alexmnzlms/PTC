# -*- coding: utf-8 -*-
"""

@author: Eugenio
Ejemplo de operaciones con ficheros .csv y diccionarios
En este ejemplo el separador es el ;

Leemos el fichero poblacionPrueba.csv como un fichero de texto
para quitar la información que no interesa y generar un nuevo
poblacionPruebaFinal.csv con los datos de provincias y población en columnas

Aviso: hay que tener cuidado con el valor de codificación si trabajamos con ficheros
procedentes de windows que suele usar windows-1250 o ISO-8859-1
en este caso hemos salvado el fichero poblacionPrueba.csv en utf8 usando el
bloc de notas de windows

Primero limpiar el archivo para quitar los datos no útiles
dejar cabecera y datos

"""
import csv

ficheroInicial=open("poblacionPrueba.csv","r", encoding="utf8")


cadenaPob=ficheroInicial.read()

ficheroInicial.close()

print("\nFichero leido inicial es\n",cadenaPob)

primero=cadenaPob.find("Total")
ultimo=cadenaPob.find("Notas")

cadenaFinal=cadenaPob[primero:ultimo]

print("\nFichero leido final es\n",cadenaFinal)

cabecera="Provincia;H2017;H2016;H2015;M2017;M2016;M2015"

ficheroFinal=open("poblacionPruebaFinal.csv", "w",encoding="utf8")

ficheroFinal.write(cabecera+'\n'+cadenaFinal)

ficheroFinal.close()

print("\n------------------------------------------------------------\n")
# Leer el archivo 'poblacionPruebaFinal.csv' con reader() y 
# mostrar todos los registros, uno a uno:
print("Primer caso: se muestra cada linea como una lista de valores")
with open('poblacionPruebaFinal.csv', encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo, delimiter=';')
    for reg in entrada:
        print(reg)  # Cada línea se muestra como una lista de valores


print("\n------------------------------------------------------------\n")
# en este segundo caso se lee como una serie de diccionarios
print("Segundo caso: se muestra cada linea como un diccionario")
with open('poblacionPruebaFinal.csv', encoding="utf8") as csvarchivo:
    poblacionDict = csv.DictReader(csvarchivo, delimiter=';')     
    for regD in poblacionDict:
        print(regD)
        
      

  
 
