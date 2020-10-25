# -*- coding: utf-8 -*-
"""
Ejercicio 9

Partiendo de una disolución de ácido sulfúrico en agua al 80 % de concentración, quiero obtener
una cantidad x de centímetros cúbicos a una concentración y% (y<80%). Siendo x, e y valores de
entrada al programa, calcular cuantos centímetros cúbicos de la disolución al 80% y de agua son
necesarios para obtener los x centímetros cúbicos deseados al y% de concentración.

Autor: Alejandro Manzanares Lemus
"""
x = float(input('Centimetros cubicos: '))
y = float(input('Concentracion (0, 100]: '))

CONCENTRACION = 0.8

x = x / 100.0
y = y / 100.0

if y < CONCENTRACION:
    agua = ((0.8 * x * x) / y - x) * 100
    disol = x * 100 - agua
    print('Los cc de agua son:', agua)
    print('Los cc de disolucion son:', disol)
