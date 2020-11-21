# -*- coding: utf-8 -*-

import csv
import numpy as np
import funciones as fn
from bs4 import BeautifulSoup



listaValores = []

html = open("entradas/comunidadesAutonomas.htm", "r", encoding="utf-8")

datos = html.read()

soup = BeautifulSoup(datos, 'html.parser')

tabla=soup.find_all('table')

#print("\nLa tabla es\n", tabla)

cabecera=soup.find_all('th')

#print("\nLa cabecera es\n", cabecera)

celdas=soup.find_all('td')

#print("\nLas celdas son\n",celdas)

for celda in celdas:
    listaValores.append(celda.get_text())
    
print("\nLista con los valores extraidos de las celdas\n",listaValores)

dic_cod_auto = {}
for i in range(0, len(listaValores) - 1, 2):
    dic_cod_auto[listaValores[i]] = listaValores[i+1]
    
print(dic_cod_auto)


listaValores1 = []

html = open("entradas/comunidadAutonoma-Provincia.htm", "r", encoding="utf-8")

datos = html.read()

soup = BeautifulSoup(datos, 'html.parser')

tabla=soup.find_all('table')

#print("\nLa tabla es\n", tabla)

cabecera=soup.find_all('th')

#print("\nLa cabecera es\n", cabecera)

celdas=soup.find_all('td')

#print("\nLas celdas son\n",celdas)

for celda in celdas:
    listaValores1.append(celda.get_text())

print("\nLista con los valores extraidos de las celdas\n",listaValores1)

dic_cod_prov = {}
for i in range(2, len(listaValores1) - 1, 4):
    dic_cod_prov[listaValores1[i]] = listaValores1[i+1]
    
print(dic_cod_prov)