# -*- coding: utf-8 -*-
"""
Ejercicio 9
    
Escribe una función elimina_vocales(palabra) que elimine todas las vocales que aparecen en la
palabra.
Autor: Alejandro Manzanares Lemus
"""

def elimina_vocales(palabra):
   vocales = "aeiou"
    
   for v in vocales:
       palabra = palabra.replace(v, "")
            
   return palabra

palabra = input('Introducza una palabra: ')

print('Eliminadas vocales de', palabra, ':', elimina_vocales(palabra))