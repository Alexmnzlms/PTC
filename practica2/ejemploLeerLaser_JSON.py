#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:12:23 2019

@author: eaguirre
Leemos el fichero de datos del laser y lo mostramos con matplot


"""
import matplotlib.pyplot as plt
import json
import os
import glob
import sys


# mostramos el directorio de trabajo y leemeos los datos del primero
print("Directorio de trabajo es: ", os.getcwd())

listaDir=sorted(glob.glob("dirLectura*"))
numDirLecturas=len(listaDir)

if(numDirLecturas>0):
    print("Numero de directorios con lecturas: ", numDirLecturas)
    print("Leemos solo el primero: ", listaDir[0])
else:
    sys.exit("Error, no hay directorios con lecturas")

os.chdir(listaDir[0])
print("Cambiando el directorio de trabajo a: ", os.getcwd())


objetos=[]

with open('datosLaser.json', 'r') as f:
     for line in f:
        objetos.append(json.loads(line))


cabecera=objetos[0]
segundos=cabecera['TiempoSleep']
maxIter=cabecera['MaxIteraciones']

iterTotalesDict=objetos[len(objetos)-1]

iterTotales=iterTotalesDict['Iteraciones totales']

plt.axis('equal')
plt.axis([0, 4, -2, 2])




for i in range(iterTotales):
    iteracion=objetos[i+1]['Iteracion']
    puntosX=objetos[i+1]['PuntosX']
    puntosY=objetos[i+1]['PuntosY']
    
    print("Iteración: ", iteracion)
    plt.clf()    
    plt.plot(puntosX, puntosY, 'r.')
    plt.show()
    

    
    






    

