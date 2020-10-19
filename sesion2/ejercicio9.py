# -*- coding: utf-8 -*-
"""
Ejercicio 9

Realizar un programa que tomando como entrada la radiación solar media por día en Kwh/m 2
calcule el número mínimo de paneles solares que se necesitan para producir, al menos, 1000 Kwh
en un mes (30 días) teniendo en cuenta que los paneles solares tienen un 17% de rendimiento y que
son de un tamaño de 1.6 m 2 .

Autor: Alejandro Manzanares Lemus
"""

kwdiario = float(input('Introduzca la cantidad media diaria de kwh/m2: '))
M2PANEL = 16.0
RENDIMIENTO = 0.17
OBJETIVO = 1000

kwdiario = kwdiario * M2PANEL * RENDIMIENTO * 30

numpaneles = OBJETIVO / kwdiario

print('El numero minimo de paneles es %d' % (numpaneles+1))
