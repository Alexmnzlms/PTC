'''
Archivo: funciones.py
Autor: Alejandro Manzanares Lemus

'''
import math

def distancia_dos_puntos(x1,y1,x2,y2):
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def recta_dos_puntos(x1,y1,x2,y2):
	coeficiente_x = (y2 - y1)
	coeficiente_y = -1 * (x2 - x1)
	termino_ind = -1 * x1 * (y2 - y1) + y1 * (x2 - x1)

	return coeficiente_x, coeficiente_y, termino_ind

def distancia_punto_recta(x1,x2,a,b,c):
	sup = abs(a*x1 + b*x2 + c)
	inf = math.sqrt(a**2 + b**2)
	dist = sup / inf

	return dist

def punto_medio(x1,y1,x2,y2):
    return (x1+x2)/2 , (y2+y1)/2

def clusterizacion(puntosX, puntosY, params):
	clusters = {}

	n_puntos = 0
	n_cluster = 0
	puntosXcluster = []
	puntosYcluster = []

	puntosXcluster.append(puntosX[0])
	puntosYcluster.append(puntosY[0])
	n_puntos += 1

	for i in range(1,len(puntosX)-1):
		dist = distancia_dos_puntos(puntosX[i], puntosY[i], puntosX[i+1], puntosY[i+1])

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
				puntosYcluster = [puntosY[i+1]]

		else:
			puntosXcluster.append(puntosX[i+1])
			puntosYcluster.append(puntosY[i+1])
			n_puntos += 1

	return clusters

def caracterizacion(num, puntosX, puntosY):
	perimetro = 0

	x0 = puntosX[0]
	y0 = puntosY[0]
	xn = puntosX[num - 1]
	yn = puntosY[num - 1]

	anchura = distancia_dos_puntos(x0,y0,xn,yn)
	width_x, width_y, width_t = recta_dos_puntos(x0,y0,xn,yn)

	profundidad = distancia_punto_recta(x0,y0,width_x,width_y,width_t)

	for punto in range(num - 1):
		x1 = puntosX[punto]
		y1 = puntosY[punto]
		x2 = puntosX[punto+1]
		y2 = puntosY[punto+1]

		perimetro += distancia_dos_puntos(x1,y1,x2,y2)

		p = distancia_punto_recta(x2,y2,width_x,width_y,width_t)

		if p > profundidad:
			profundidad = p

	return perimetro, profundidad, anchura
