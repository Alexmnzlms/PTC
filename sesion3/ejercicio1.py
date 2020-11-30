# -*- coding: utf-8 -*-
"""
Ejercicio 1
    
Escribe una función contar_letras(palabra, letra) que devuelva el número de veces que aparece
una letra en una palabra.

Autor: Alejandro Manzanares Lemus
"""

def contar_letras(palabra, letra):
    n = 0
    for l in palabra:
        if l == letra:
            n += 1
    
    return n

palabra = input('Introducza una palabra: ')
letra = input('Introduza una letra: ')

print('El numero de', letra, 'de', palabra, 'es', contar_letras(palabra, letra))