# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:39:45 2020

@author: Alejandro Manzanares Lemus
"""

# EJERCICIO DE COMPENSIÓN DE LISTAS

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

# EJERCICIO DE ELIMINACIÓN DE VALOR EN LISTA DE 6 FORMAS

def elim1(lista, n):
    while lista.count(n) > 0:
        lista.remove(n)
        
def elim2(lista, n):
    while lista.count(n) > 0:
        lista.pop(lista.index(n))
        
def elim3(lista, n):
    while lista.count(n) > 0:
        del lista[lista.index(n)]

def elim4(lista, n):
    lista_aux = []
    for i in lista:
        if i != n:
            lista_aux.append(i)
    return lista_aux
        
def elim5(lista, n):
    i = 0
    while(i < len(lista)):
        if lista[i] == n:
            del lista[i]
            i = i - 1
        else:
            i = i + 1

def elim6(lista, n):
    i = 0
    while(i < len(lista)):
        if lista[i] == n:
            lista.remove(lista[i])
            i = i - 1
        else:
            i = i + 1

lista = [2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 7, 9, 10]
lista.sort()
lista1 = lista[:]
lista2 = lista[:]
lista3 = lista[:]
lista4 = lista[:]
lista5 = lista[:]
lista6 = lista[:]

elim = 5

print('\nORIGINAL')
print(lista)

print('\nELIMINACION 1')
elim1(lista1,elim)
print(lista1)

print('\nELIMINACION 2')
elim2(lista2,elim)
print(lista2)

print('\nELIMINACION 3')
elim3(lista3,elim)
print(lista3)

print('\nELIMINACION 4')
lista4 = elim4(lista4,elim)
print(lista4)

print('\nELIMINACION 5')
elim5(lista5,elim)
print(lista5)

print('\nELIMINACION 6')
elim6(lista6,elim)
print(lista6)