# -*- coding: utf-8 -*-
"""
Ejercicio 7
    
Escribe una función mayusculas(palabra) que devuelva la palabra pasada a mayúsculas.

Autor: Alejandro Manzanares Lemus
"""

def mayusculas(palabra):
    mayus = ""
    
    for l in palabra:
        if (ord(l) > 96 and ord(l) < 123):
            mayus += chr(ord(l) ^ 32)
                   
    return mayus
   
palabra = input('Introducza una palabra: ')

print('La palabra', palabra, 'pasada a mayusculas:', mayusculas(palabra))