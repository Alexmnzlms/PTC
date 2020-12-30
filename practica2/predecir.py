'''
Archivo: predecir.py
Autor: Alejandro Manzanares Lemus

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
		for p in clusters[d][1]:
			puntosx.append(p)
		for p in clusters[d][2]:
			puntosy.append(p)

	plt.clf()
	plt.plot(puntosx, puntosy, 'r.')
	plt.savefig("lecturaClusters.jpg")

	fichero.close()
	###########################################################################
	'''
	CARACTERIZACION
	'''
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

		cont = 0
		puntosXpos = []
		puntosYpos = []
		puntosXneg = []
		puntosYneg = []
		for dic in objetos:
			if prediccion[cont] == 0:
				for p in dic['puntosX']:
					puntosXneg.append(p)
				for p in dic['puntosY']:
					puntosYneg.append(p)
			else:
				for p in dic['puntosX']:
					puntosXpos.append(p)
				for p in dic['puntosY']:
					puntosYpos.append(p)
			cont += 1

	plt.clf()
	plt.plot(puntosXpos, puntosYpos, 'r.')
	plt.plot(puntosXneg, puntosYneg, 'b.')
	plt.savefig("prediccion.jpg")




	###########################################################################
	os.chdir(dir_p2)

