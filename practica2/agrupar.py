'''
Archivo: agrupar.py
Autor: Alejandro Manzanares Lemus

'''
import matplotlib.pyplot as plt
import json
import os
import sys
import glob
import geometria as geo

def agrupar(params):
	print("Ejecutando agrupar...")

	dir_p2 = os.getcwd()

	for caso in ["positivo","negativo"]:

		# mostramos el directorio de trabajo y leemeos los datos del primero
		print("Directorio de trabajo es: ", os.getcwd())
		lista = caso + "*"
		listaDir=sorted(glob.glob(lista))
		numDir=len(listaDir)

		if numDir > 0:
			print("Numero de directorios: ", numDir)
			print(listaDir)
		else:
			sys.exit("No hay directorios")

		iteracion = []
		puntosX = []
		puntosY = []

		for directorio in listaDir:
			os.chdir(directorio)
			print("Cambiando el directorio de trabajo a:", os.getcwd())

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


			for i in range(iterTotales):
				iteracion.append(objetos[i+1]['Iteracion'])
				for x in objetos[i+1]['PuntosX']:
					puntosX.append(x)
				for y in objetos[i+1]['PuntosY']:
					puntosY.append(y)

			os.chdir(dir_p2)

		print("Iteración: ", len(iteracion))
		print("PuntosX: ", len(puntosX))
		print("PuntosY: ", len(puntosY))

		clusters = {}

		n_puntos = 0
		n_cluster = 0
		puntosXcluster = []
		puntosYcluster = []

		puntosXcluster.append(puntosX[0])
		puntosYcluster.append(puntosY[0])
		n_puntos += 1

		for i in range(1,len(puntosX)-1):
			dist = geo.distancia_dos_puntos(puntosX[i], puntosY[i], puntosX[i+1], puntosY[i+1])

			if(dist > params.ud or n_puntos > params.maxp):
				if n_puntos > params.minp:
					clusters[n_cluster] = [n_puntos, puntosXcluster, puntosYcluster]
					n_cluster += 1
					n_puntos = 1
					puntosXcluster = [puntosX[i+1]]
					puntosYcluster = [puntosY[i+1]]

				else:
					n_puntos = 1
					puntosXcluster = [puntosX[i+1]]
					puntosYcluser = [puntosY[i+1]]

			else:
				puntosXcluster.append(puntosX[i+1])
				puntosYcluster.append(puntosY[i+1])
				n_puntos += 1

		if caso == "positivo":
			file = "clustersPiernas.json"
		elif caso == "negativo":
			file = "clustersNoPiernas.json"

		fichero = open(file, "w")

		for d in clusters.keys():
			cluster = {"numero_cluster":d, "numero_puntos":clusters[d][0], "puntosX":clusters[d][1], "puntosY":clusters[d][2]}
			fichero.write(json.dumps(cluster)+'\n')

	os.chdir(dir_p2)
