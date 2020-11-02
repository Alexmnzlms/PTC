# -*- coding: utf-8 -*-
"""
Ejercicio 5
    
Escribe una función num_vocales(palabra) que devuelva el número de vocales que aparece en la
palabra.

Autor: Alejandro Manzanares Lemus
"""

def num_vocales(palabra):
    vocales = "aeiou"
    n_vocales = 0
    for v in palabra:
        for i in vocales:
            if v == i:
                n_vocales += 1
                break
    
    return n_vocales
   
            
        
        
palabra = input('Introducza una palabra: ')

print('El numero de vocales en la palabra', palabra, 'es', num_vocales(palabra))