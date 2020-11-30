# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:03:37 2020

@author: Alejandro Manzanares Lemus
"""

# Método tradicional

lista = []
for numero in range(1,11):
    lista.append(numero**2)
    
pares = []
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
        
# Versión compresion de lista        

pares_comp = [x**2 for x in range(1,11) if x**2 % 2 == 0 ]

print('Método tradicional', pares)
print('Compresión de listas', pares_comp)