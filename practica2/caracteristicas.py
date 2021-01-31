#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Archivo: caracteristicas.py
Autor: Alejandro Manzanares Lemus

Script correspondiente al apartado 4.4
Convertir los clústeres en características geométricas
'''
import json
import funciones as fn

def caracteristicas():
	print("Ejecutando caracteristicas...")

	#Para cada archivo de clusters
	for file in ["clustersPiernas.json", "clustersNoPiernas.json"]:

		objetos=[]
		with open(file, 'r') as f:
			for line in f:
				objetos.append(json.loads(line))

		#Establecemos el fichero de salida en función de la entrada
		if file == "clustersPiernas.json":
			espierna = 1
			file_w = "caracteristicasPiernas.dat"
		elif file == "clustersNoPiernas.json":
			espierna = 0
			file_w = "caracteristicasNoPiernas.dat"

		fichero = open(file_w, "w")

		#Obtenemos las caracteristicas de todos los clusters
		for dic in objetos:
			perimetro, profundidad, anchura = fn.caracterizacion(dic['numero_puntos'], dic['puntosX'], dic['puntosY'])

			caract = {"numero_cluster":dic['numero_cluster'], "numero_puntos":dic['numero_puntos'], "perimetro":perimetro, "profundidad":profundidad, "anchura":anchura, "esPierna":espierna}

			fichero.write(json.dumps(caract)+'\n')

	file_w = "piernasDataset.csv"
	fichero = open(file_w, "w")

	#Creamos el dataset
	for file in ["caracteristicasNoPiernas.dat", "caracteristicasPiernas.dat"]:
		objetos=[]
		with open(file, 'r') as f:
			for line in f:
				objetos.append(json.loads(line))

		for dic in objetos:
			linea = str(dic['perimetro']) + ','
			linea += str(dic['profundidad']) + ','
			linea += str(dic['anchura']) + ','
			linea += str(dic['esPierna'])

			fichero.write(linea+'\n')



