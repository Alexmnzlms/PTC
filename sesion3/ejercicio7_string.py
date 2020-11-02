# -*- coding: utf-8 -*-
"""
Ejercicio 7
    
Escribe una función mayusculas(palabra) que devuelva la palabra pasada a mayúsculas.

Autor: Alejandro Manzanares Lemus
"""

def mayusculas(palabra):
   return palabra.upper()
   
palabra = input('Introducza una palabra: ')

print('La palabra', palabra, 'pasada a mayusculas:', mayusculas(palabra))