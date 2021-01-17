'''
Archivo: funciones.py
Autor: Alejandro Manzanares Lemus

Script auxiliar de funciones
'''
import math

#Devuelve la distancia entre el punto P(x1,y1) y Q(x2,y2)
def distancia_dos_puntos(x1,y1,x2,y2):
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#Devuelve la recta Ax + By + C formada por los puntos P(x1,y1) y Q(x2,y2)
def recta_dos_puntos(x1,y1,x2,y2):
	coeficiente_x = (y2 - y1)
	coeficiente_y = -1 * (x2 - x1)
	termino_ind = -1 * x1 * (y2 - y1) + y1 * (x2 - x1)

	return coeficiente_x, coeficiente_y, termino_ind

#Devuelve la distancia entre la recta ax+by+c y el punto P(x,y)
def distancia_punto_recta(x,y,a,b,c):
	sup = abs(a*x + b*y + c)
	inf = math.sqrt(a**2 + b**2)
	dist = sup / inf

	return dist

#Devuelve el punto medio entre P(x1,y1) y Q(x2,y2)
def punto_medio(x1,y1,x2,y2):
	return (x1+x2)/2 , (y2+y1)/2

#Función de clusterización
#puntosX : Coordenadas X de los puntos a clusterizar
#puntosY : Coordenadas Y de los puntos a clusterizar
#params : parametros de la clusterización
def clusterizacion(puntosX, puntosY, params):
	clusters = {}

	n_puntos = 0
	n_cluster = 0
	puntosXcluster = []
	puntosYcluster = []

	puntosXcluster.append(puntosX[0])
	puntosYcluster.append(puntosY[0])
	n_puntos += 1

	#Recorremos los puntos desde el 0 hasta el penultimo
	for i in range(0,len(puntosX)-1):
		#Calculamos la distancia entre el punto i y el i+1
		dist = distancia_dos_puntos(puntosX[i], puntosY[i], puntosX[i+1], puntosY[i+1])

		# SI la distancia es mayor que la umbral o el número de puntos supera el maximo
		if(dist > params.ud or n_puntos >= params.maxp):
			#Si el número de puntos supera el mínimo, creamos un cluster
			if n_puntos >= params.minp:
				clusters[n_cluster] = [n_puntos, puntosXcluster, puntosYcluster]
				n_cluster += 1
				n_puntos = 1
				puntosXcluster = [puntosX[i+1]]
				puntosYcluster = [puntosY[i+1]]

			#Si no, descartamos el cluster
			else:
				n_puntos = 1
				puntosXcluster = [puntosX[i+1]]
				puntosYcluster = [puntosY[i+1]]

		#Si no, añadimos el punto al cluster actual
		else:
			puntosXcluster.append(puntosX[i+1])
			puntosYcluster.append(puntosY[i+1])
			n_puntos += 1

	return clusters

#Función de extraer características
#num : número de puntos
#puntosX : Coordenadas X de los puntos
#puntosY : Coordenadas Y de los puntos
def caracterizacion(num, puntosX, puntosY):

	#La anchura es la distancia entre el primer y el ultimo punto
	x0 = puntosX[0]
	y0 = puntosY[0]
	xn = puntosX[num - 1]
	yn = puntosY[num - 1]
	anchura = distancia_dos_puntos(x0,y0,xn,yn)

	width_x, width_y, width_t = recta_dos_puntos(x0,y0,xn,yn)
	profundidad = distancia_punto_recta(x0,y0,width_x,width_y,width_t)
	perimetro = 0
	for punto in range(num - 1):
		x1 = puntosX[punto]
		y1 = puntosY[punto]
		x2 = puntosX[punto+1]
		y2 = puntosY[punto+1]

		#El perimetro es la suma de la distancia entre todos los puntos seguidos
		perimetro += distancia_dos_puntos(x1,y1,x2,y2)

		p = distancia_punto_recta(x2,y2,width_x,width_y,width_t)

		#La profundidad es la distancia maxima de todos los puntos a la recta anchura
		if p > profundidad:
			profundidad = p

	return perimetro, profundidad, anchura
