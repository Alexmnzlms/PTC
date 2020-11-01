# -*- coding: utf-8 -*-
"""
Ejercicio 2
    
Escribe una función eliminar_letras(palabra, letra) que devuelva una versión de palabra que no
contiene el carácter letra ninguna vez.

Autor: Alejandro Manzanares Lemus
"""

def eliminar_letras(palabra, letra):
    eliminada = ""
    
    for a in palabra:
        if a != letra:
            eliminada += a
            
    return eliminada

palabra = input('Introducza una palabra: ')
letra = input('Introduza una letra: ')

print('Eliminada', letra, 'de', palabra, ':', eliminar_letras(palabra, letra))