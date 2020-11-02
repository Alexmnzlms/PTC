# -*- coding: utf-8 -*-
"""
Ejercicio 9
    
Escribe una función elimina_vocales(palabra) que elimine todas las vocales que aparecen en la
palabra.

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

def elimina_vocales(palabra):
    eliminada = ""
    
    for a in palabra:
        if not es_vocal(a):
            eliminada += a
            
    return eliminada

palabra = input('Introducza una palabra: ')

print('Eliminadas vocales de', palabra, ':', elimina_vocales(palabra))