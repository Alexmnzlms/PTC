'''
Archivo: caracteristicas.py
Autor: Alejandro Manzanares Lemus

'''
import json
import funciones as fn

def caracteristicas():
	print("Ejecutando caracteristicas...")

	for file in ["clustersPiernas.json", "clustersNoPiernas.json"]:

		objetos=[]
		with open(file, 'r') as f:
			for line in f:
				objetos.append(json.loads(line))

		if file == "clustersPiernas.json":
			espierna = 1
			file_w = "caracteristicasPiernas.dat"
		elif file == "clustersNoPiernas.json":
			espierna = 0
			file_w = "caracteristicasNoPiernas.dat"

		fichero = open(file_w, "w")

		for dic in objetos:
####		perimetro = 0

####		x0 = dic['puntosX'][0]
####		y0 = dic['puntosY'][0]
####		xn = dic['puntosX'][dic['numero_puntos'] - 1]
####		yn = dic['puntosY'][dic['numero_puntos'] - 1]

####		anchura = fn.distancia_dos_puntos(x0,y0,xn,yn)
####		width_x, width_y, width_t = fn.recta_dos_puntos(x0,y0,xn,yn)

####		profundidad = fn.distancia_punto_recta(x0,y0,width_x,width_y,width_t)

####		for punto in range(dic['numero_puntos'] - 1):
####			x1 = dic['puntosX'][punto]
####			y1 = dic['puntosY'][punto]
####			x2 = dic['puntosX'][punto+1]
####			y2 = dic['puntosY'][punto+1]

####			perimetro += fn.distancia_dos_puntos(x1,y1,x2,y2)

####			p = fn.distancia_punto_recta(x2,y2,width_x,width_y,width_t)

####			if p > profundidad:
####				profundidad = p

			perimetro, profundidad, anchura = fn.caracterizacion(dic['numero_puntos'], dic['puntosX'], dic['puntosY'])

			caract = {"numero_cluster":dic['numero_cluster'], "numero_puntos":dic['numero_puntos'], "perimetro":perimetro, "profundidad":profundidad, "anchura":anchura, "esPierna":espierna}

			fichero.write(json.dumps(caract)+'\n')

	file_w = "piernasDataset.csv"
	fichero = open(file_w, "w")

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



