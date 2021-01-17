'''
Archivo: agrupar.py
Autor: Alejandro Manzanares Lemus

Script correspondiente al apartado 4.3
Agrupar los puntos x,y en clústeres
'''
import matplotlib.pyplot as plt
import json
import os
import sys
import glob
import funciones as fn
import funciones as fn

def agrupar(params):
	print("Ejecutando agrupar...")

	dir_p2 = os.getcwd()

	#Repetimos para positivos y negativos
	for caso in ["positivo","negativo"]:

		lista = caso + "*"
		listaDir=sorted(glob.glob(lista))
		numDir=len(listaDir)

		if numDir > 0:
			print("Numero de directorios: ", numDir, listaDir)
		else:
			sys.exit("No hay directorios")

		iteracion = []
		puntosX = []
		puntosY = []

		#Para cada directorio de positivos o negativos
		for directorio in listaDir:
			os.chdir(directorio)

			#Segun en que carpeta estemos, actualizamos el fichero
			if os.getcwd().find("positivo1") != -1:
				file = "enPieCerca.json"
			elif os.getcwd().find("positivo2") != -1:
				file = "enPieMedia.json"
			elif os.getcwd().find("positivo3") != -1:
				file = "enPieLejos.json"
			elif os.getcwd().find("positivo4") != -1:
				file = "sentadoCerca.json"
			elif os.getcwd().find("positivo5") != -1:
				file = "sentadoMedia.json"
			elif os.getcwd().find("positivo6") != -1:
				file = "sentadoLejos.json"
			elif os.getcwd().find("negativo1") != -1:
				file = "cilindroMenorCerca.json"
			elif os.getcwd().find("negativo2") != -1:
				file = "cilindroMenorMedia.json"
			elif os.getcwd().find("negativo3") != -1:
				file = "cilindroMenorLejos.json"
			elif os.getcwd().find("negativo4") != -1:
				file = "cilindroMayorCerca.json"
			elif os.getcwd().find("negativo5") != -1:
				file = "cilindroMayorMedia.json"
			elif os.getcwd().find("negativo6") != -1:
				file = "cilindroMayorLejos.json"
			else:
				sys.exit("Directorio no encontrado")

			objetos=[]
			with open(file, 'r') as f:
				for line in f:
					objetos.append(json.loads(line))

			cabecera = objetos[0]
			segundos = cabecera['TiempoSleep']
			maxIter = cabecera['MaxIteraciones']

			iterTotalesDict = objetos[len(objetos)-1]
			iterTotales = iterTotalesDict['Iteraciones totales']

			#Obtenemos los puntos
			for i in range(iterTotales):
				iteracion.append(objetos[i+1]['Iteracion'])
				for x in objetos[i+1]['PuntosX']:
					puntosX.append(x)
				for y in objetos[i+1]['PuntosY']:
					puntosY.append(y)

			os.chdir(dir_p2)

		#Mostramos por terminal el numero de iteraciones y puntos
		print("Iteraciones: ", len(iteracion))
		print("PuntosX: ", len(puntosX))
		print("PuntosY: ", len(puntosY))

		#Calculamos los clusteres
		clusters = fn.clusterizacion(puntosX,puntosY,params)

		#Guardamos los clusteres en los archivos correspondientes
		if caso == "positivo":
			file = "clustersPiernas.json"
		elif caso == "negativo":
			file = "clustersNoPiernas.json"

		fichero = open(file, "w")

		for d in clusters.keys():
			cluster = {"numero_cluster":d, "numero_puntos":clusters[d][0], "puntosX":clusters[d][1], "puntosY":clusters[d][2]}
			fichero.write(json.dumps(cluster)+'\n')

	os.chdir(dir_p2)
