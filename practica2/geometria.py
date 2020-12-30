'''
Archivo: geometria.py
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

