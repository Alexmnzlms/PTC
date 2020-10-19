# -*- coding: utf-8 -*-
"""
Ejercicio 8

Realizar un programa que pida un valor X de porcentaje de alcohol de una marca de cerveza y
que según dicho porcentaje calcule cuantos tercios de esa marca de cerveza (333cc) puedo tomar si
no quiero ingerir más de 50 cc de alcohol. Dar el resultado en valor entero.

Autor: Alejandro Manzanares Lemus
"""
porcentaje = float(input('Por favor introduzca un porcentaje de alcohol en el intervalor (0,100]: '))

CERVEZACC = 333.0
MAXIMOCC = 50.0

porcentaje = porcentaje / 100

porcentaje = porcentaje * CERVEZACC

cervezas = MAXIMOCC / porcentaje

print('Maximo numero de cervezas: %d' % (cervezas))

