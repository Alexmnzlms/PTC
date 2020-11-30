# -*- coding: utf-8 -*-
"""
Ejercicio 4
    
Escribe una función buscar(palabra, sub) que devuelva la posición en la que se puede encontrar
sub dentro de palabra o -1 en caso de que no esté.

Autor: Alejandro Manzanares Lemus
"""

def buscar(palabra,sub):
    return palabra.find(sub)
            
        
        
palabra = input('Introducza una palabra: ')
sub = input('Introducza una subcadena: ')

print('En la palabra', palabra, 'la subcadena', sub, 'aparece en la posición:', buscar(palabra, sub))