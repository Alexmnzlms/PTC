# -*- coding: utf-8 -*-
"""
Ejercicio 8
    
Escribe una función inicio_fin_vocal(palabra) que determine si una palabra empieza y acaba con
una vocal.

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

def inicio_fin_vocal(palabra):
    if (es_vocal(palabra[0]) and es_vocal(palabra[len(palabra)-1])):
        return True
    
    return False
    
   
palabra = input('Introducza una palabra: ')

if inicio_fin_vocal(palabra):
    print('La palabra', palabra, 'empieza y termina por vocal')
else:
    print('La palabra', palabra, 'no empieza y termina por vocal')