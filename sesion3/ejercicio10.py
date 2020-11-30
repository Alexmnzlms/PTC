# -*- coding: utf-8 -*-
"""
Ejercicio 10
    
Escribe una función es_inversa(palabra1, palabra2) que determine si una palabra es la misma
que la otra pero con los caracteres en orden inverso. Por ejemplo 'absd' y 'dsba'.

Autor: Alejandro Manzanares Lemus
"""

def es_inversa(palabra1,palabra2):
    palabra2 = palabra2[::-1]
   
    return palabra1 == palabra2

palabra1 = input('Introducza una palabra: ')
palabra2 = input('Introducza una palabra: ')

if es_inversa(palabra1,palabra2):
    print('La palabra', palabra1, 'y la palabra', palabra2, 'son iguales')
else:
    print('La palabra', palabra1, 'y la palabra', palabra2, 'no son iguales')