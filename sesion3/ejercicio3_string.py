# -*- coding: utf-8 -*-
"""
Ejercicio 3
    
Escribe una función mayusculas_minusculas(palabra) que devuelva una cadena en la que las
mayúsculas y las minúsculas estén al contrario.

Autor: Alejandro Manzanares Lemus
"""

def mayusculas_minusculas(palabra):
   return palabra.swapcase()
        
        
palabra = input('Introducza una palabra: ')

print('Cambiadas las mayusculas y minusculas de', palabra, ':', mayusculas_minusculas(palabra))