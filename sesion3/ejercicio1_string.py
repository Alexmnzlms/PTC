# -*- coding: utf-8 -*-
"""
Ejercicio 1
    
Escribe una función contar_letras(palabra, letra) que devuelva el número de veces que aparece
una letra en una palabra.

Autor: Alejandro Manzanares Lemus
"""

def contar_letras(palabra, letra):
    return palabra.count(letra)

palabra = input('Introducza una palabra: ')
letra = input('Introduza una letra: ')

print('El numero de', letra, 'de', palabra, 'es', contar_letras(palabra, letra))