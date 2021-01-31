#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Archivo: predecir.py
Autor: Alejandro Manzanares Lemus

Script correspondiente al apartado 4.6
Utilizar el clasificador con datos nuevos a partir del simulador
'''
import vrep
import sys
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
import json
import os
import funciones as fn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import GridSearchCV
import pickle

def predecir(clientID, params):
	print("Ejecutando predecir...")
	###########################################################################
	'''
	LEYENDO DATOS DEL LASER
	'''
	print('LEYENDO DATOS DEL LASER...')

	_, robothandle = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx', vrep.simx_opmode_oneshot_wait)

	#Guardar la referencia de los motores
	_, left_motor_handle=vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', vrep.simx_opmode_oneshot_wait)
	_, right_motor_handle=vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', vrep.simx_opmode_oneshot_wait)

	#Guardar la referencia de la camara
	_, camhandle = vrep.simxGetObjectHandle(clientID, 'Vision_sensor', vrep.simx_opmode_oneshot_wait)

	#acceder a los datos del laser
	_, datosLaserComp = vrep.simxGetStringSignal(clientID,'LaserData',vrep.simx_opmode_streaming)

	velocidad = 0 #Variable para la velocidad de los motores, dejamos fijo el robot

	#Iniciar la camara y esperar un segundo para llenar el buffer
	_, resolution, image = vrep.simxGetVisionSensorImage(clientID, camhandle, 0, vrep.simx_opmode_streaming)
	time.sleep(1)

	plt.axis('equal')
	plt.axis([0, 4, -2, 2])

	# mostramos el directorio de trabajo y vemos si existe el dir para salvar los datos
	dir_p2 = os.getcwd()
	print("Directorio de trabajo es: ", os.getcwd())

	direc = dir_p2 + "/predecir"

	if not os.path.isdir(direc):
		print("Creando el directorio " + direc)
		os.mkdir(direc)

	os.chdir(direc)
	print("Cambiando el directorio de trabajo: ", os.getcwd())

	ficheroLaser=open("datosLaser.json", "w")

	puntosx=[] #listas para recibir las coordenadas x, y z de los puntos detectados por el laser
	puntosy=[]
	puntosz=[]
	returnCode, signalValue = vrep.simxGetStringSignal(clientID,'LaserData',vrep.simx_opmode_buffer)

	datosLaser=vrep.simxUnpackFloats(signalValue)
	for indice in range(0,len(datosLaser),3):
		puntosx.append(datosLaser[indice+1])
		puntosy.append(datosLaser[indice+2])
		puntosz.append(datosLaser[indice])

	#Se guarda una imagen de los puntos leidos en el plano
	plt.clf()
	plt.plot(puntosx, puntosy, 'r.')
	plt.savefig("lecturaLaser.jpg")

	#Guardamos los puntosx, puntosy en el fichero JSN
	lectura={"PuntosX":puntosx, "PuntosY":puntosy}
	ficheroLaser.write(json.dumps(lectura))
	ficheroLaser.close()
	###########################################################################
	'''
	CLUSTERIZACIÓN
	'''
	print('CLUSTERIZANDO...')

	file = "datosLaser.json"
	objetos=[]
	with open(file, 'r') as f:
		for line in f:
			objetos.append(json.loads(line))

	clusters = fn.clusterizacion(objetos[0]['PuntosX'], objetos[0]['PuntosY'], params)

	file = "clustersLaser.json"
	fichero = open(file, "w")

	puntosx = []
	puntosy = []

	for d in clusters.keys():
		cluster = {"numero_cluster":d, "numero_puntos":clusters[d][0], "puntosX":clusters[d][1], "puntosY":clusters[d][2]}
		fichero.write(json.dumps(cluster)+'\n')
		for px, py in zip(clusters[d][1], clusters[d][2]):
			puntosx.append(px)
			puntosy.append(py)

	#Se guarda una imagen de los puntos leídos despues de clusterizar
	plt.clf()
	plt.plot(puntosx, puntosy, 'r.')
	plt.savefig("lecturaClusters.jpg")

	fichero.close()
	###########################################################################
	'''
	CARACTERIZACION
	'''
	print('EXTRAYENDO CARACTERISTICAS...')

	file = "clustersLaser.json"
	objetos=[]
	with open(file, 'r') as f:
		for line in f:
			objetos.append(json.loads(line))

	file_w = "caracteristicasLaser.dat"
	fichero = open(file_w, "w")
	for dic in objetos:
		perimetro, profundidad, anchura = fn.caracterizacion(dic['numero_puntos'], dic['puntosX'], dic['puntosY'])
		caract = {"numero_cluster":dic['numero_cluster'], "numero_puntos":dic['numero_puntos'], "perimetro":perimetro, "profundidad":profundidad, "anchura":anchura}
		fichero.write(json.dumps(caract)+'\n')

	fichero.close()

	objetos=[]
	with open(file_w, 'r') as f:
		for line in f:
			objetos.append(json.loads(line))

	file = "caracteristicasLaser.csv"
	fichero = open(file, "w")

	for dic in objetos:
		linea = str(dic['perimetro']) + ','
		linea += str(dic['profundidad']) + ','
		linea += str(dic['anchura'])

		fichero.write(linea+'\n')

	fichero.close()
	###########################################################################
	'''
	PREDICCION
	'''
	print('PROPORCIONANDO PREDICCION...')

	colnames = ['perimetro', 'profundidad', 'anchura']

	# cargamos los datos
	# Read dataset to pandas dataframe
	laserdata = np.array(pd.read_csv("caracteristicasLaser.csv", names=colnames))

	# Leemos el clasificador

	if not os.path.isfile("clasificador.pkl"):
		print("No existe el clasificador entrenado")
	else:
		with open("clasificador.pkl", "rb") as archivo:
			clasificador=pickle.load(archivo)

		# lo pasamos a Dataframe

		carDataF=pd.DataFrame(laserdata)

		# hacemos la prediccion

		prediccion=clasificador.predict(carDataF)

		print("Prediccion:", prediccion)

		file_c = "clustersLaser.json"
		objetos=[]
		with open(file_c, 'r') as f:
			for line in f:
				objetos.append(json.loads(line))

		#Separamos los puntos según la predicción
		cont = 0
		puntosXpos = []
		puntosYpos = []
		puntosXneg = []
		puntosYneg = []
		for dic in objetos:
			if prediccion[cont] == 0:
				for px,py in zip(dic['puntosX'], dic['puntosY']):
					puntosXneg.append(px)
					puntosYneg.append(py)
			else:
				for px,py in zip(dic['puntosX'], dic['puntosY']):
					puntosXpos.append(px)
					puntosYpos.append(py)
			cont += 1

		#Guardamos una imagen de la predicción sin los centroides de los clusters
		plt.clf()
		plt.plot(puntosXpos, puntosYpos, 'r.')
		plt.plot(puntosXneg, puntosYneg, 'b.')
		plt.savefig("prediccion_sin_centro.jpg")

		#Calculamos los centroides de los clusters
		#como la media de los puntos de dicho clusters
		centroides = []
		for dic in objetos:
			centrox = 0
			centroy = 0
			for px,py in zip(dic['puntosX'],dic['puntosY']):
				centrox += px
				centroy += py
			centrox /= len(dic['puntosX'])
			centroy /= len(dic['puntosY'])
			centroide = {"numero_cluster": dic['numero_cluster'], "centroX":centrox, "centroY": centroy}
			centroides.append(centroide)

		distanciaCercana = 0.5 #Establecemos el valor de distancia cercana entre dos clusters

		 #Calculamos las parejas cercanas de clusters
		parejas = []

		#Mientras haya centroides
		while(len(centroides) > 0):
			centro = centroides[0]
			del centroides[0]
			cont = 0
			pos = -1
			#Se comprueba para cada centroide la distancia con centro
			for c in centroides:
				mind = 1000.0
				dist = fn.distancia_dos_puntos(centro['centroX'], centro['centroY'], c['centroX'], c['centroY'])
				if dist < mind and dist < distanciaCercana and prediccion[centro['numero_cluster']] == prediccion[c['numero_cluster']]:
					mind = dist
					pos = cont
				cont += 1
			if pos != -1:
				#Si se ha encontrado pareja para centro se añade
				parejas.append((centro,centroides[pos]))
				del centroides[pos]

		#Se separan los centros de las parejas
		#segun la predicción
		centrosXneg = []
		centrosXpos = []
		centrosYneg = []
		centrosYpos = []
		for pareja in parejas:
			x1 = pareja[0]['centroX']
			y1 = pareja[0]['centroY']
			x2 = pareja[1]['centroX']
			y2 = pareja[1]['centroY']
			xm, ym = fn.punto_medio(x1,y1,x2,y2)
			if prediccion[pareja[0]['numero_cluster']] == 0:
				centrosXneg.append(xm)
				centrosYneg.append(ym)
			else:
				centrosXpos.append(xm)
				centrosYpos.append(ym)

		#Se guarda la imagen con la predicción final
		plt.clf()
		plt.plot(puntosXpos, puntosYpos, 'r.')
		plt.plot(puntosXneg, puntosYneg, 'b.')
		plt.plot(centrosXpos, centrosYpos, 'ro')
		plt.plot(centrosXneg, centrosYneg, 'bo')
		plt.savefig("prediccion.jpg")



	###########################################################################
	os.chdir(dir_p2)

