# -*- coding: utf-8 -*-
"""
Ejercicio 6

Pedir tres valores reales x1,x2,x3, obtener su máximo y su mínimo y mostrarlos por pantalla. (No
usar la funcion max y min de python).

Autor: Alejandro Manzanares Lemus
"""

x_1 = float(input('Primer valor:\n'))
x_2 = float(input('Segundo valor:\n'))
x_3 = float(input('Tercer valor:\n'))

maximo = x_1
minimo = x_1

if maximo < x_2:
    maximo = x_2
    
if maximo < x_3:
    maximo = x_3
    
if minimo > x_2:
    minimo = x_2

if minimo > x_3:
    minimo = x_3
    
print('Maximo:', maximo)
print('Minimo:', minimo)
    
