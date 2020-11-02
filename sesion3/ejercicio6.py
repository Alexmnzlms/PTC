# -*- coding: utf-8 -*-
"""
Ejercicio 6
    
Escribe una función vocales(palabra) que devuelva las vocales que aparecen en la palabra.

Autor: Alejandro Manzanares Lemus
"""

def es_vocal(letra):
    vocales = "aeiou"
    vocal = False
    
    for i in vocales:
        if letra == i:
            vocal = True
            break

    return vocal

def vocales(palabra):
    vocales = ""
    
    for l in palabra:
        if es_vocal(l):
            vocales += l
            
    return vocales
    
   
palabra = input('Introducza una palabra: ')

print('Las vocales que aparecen en la palabra', palabra, 'son', vocales(palabra))