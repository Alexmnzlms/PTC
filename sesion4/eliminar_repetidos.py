# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:10:02 2020

@author: Alejandro Manzanares Lemus
"""

def elim1(lista, n):
    while lista.count(n) > 0:
        lista.remove(n)
        
def elim2(lista, n):
    while lista.count(n) > 0:
        lista.pop(lista.index(n))
        
def elim3(lista, n):
    lista_aux = []
    for i in lista:
        if i != n:
            lista_aux.append(i)
    return lista_aux

def 

lista = []
for i in range(1,10):
    if i == 5:
        for i in range(6): lista.append(5)
    else:
        lista.append(i)

lista1 = lista[:]
lista2 = lista[:]
lista3 = lista[:]
lista4 = lista[:]
lista5 = lista[:]
lista6 = lista[:]

print('\nELIMINACION 1')
print(lista1)
elim1(lista1,5)
print(lista1)

print('\nELIMINACION 2')
print(lista2)
elim2(lista2,5)
print(lista2)

print('\nELIMINACION 3')
print(lista3)
lista3 = elim3(lista3,5)
print(lista3)