# -*- coding: utf-8 -*-
"""
Ejercicio 8
    
Escribe una función inicio_fin_vocal(palabra) que determine si una palabra empieza y acaba con
una vocal.

Autor: Alejandro Manzanares Lemus
"""
def inicio_fin_vocal(palabra):
    vocales = "aeiou"
    primera_vocal = False
    ultima_vocal = False
    
    for v in vocales:
        if palabra.startswith(v):
            primera_vocal = True
            break
    
    for v in vocales:
        if palabra.endswith(v):
            ultima_vocal = True
            break
        
    if (primera_vocal and ultima_vocal):
        return True
    else:
        return False
   
palabra = input('Introducza una palabra: ')

if inicio_fin_vocal(palabra):
    print('La palabra', palabra, 'empieza y termina por vocal')
else:
    print('La palabra', palabra, 'no empieza y termina por vocal')