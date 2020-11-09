# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:07:22 2020

@author: Eugenio

En este ejemplo vamos a leer una página web online, localizamos los datos
de la tabla y los guardarmos en un tipo lista.

Primero usamos bs4
si no está instalado instalar con 
pip3 install bs4

"""



import urllib.request
from bs4 import BeautifulSoup
import certifi
import ssl



listaValores=[]

url="https://www.ine.es/daco/daco42/codmun/cod_ccaa.htm"

print("\nProcesando ", url)
 
datos = urllib.request.urlopen(url, context=ssl.create_default_context(cafile=certifi.where())).read()  #en utf8

#datos = urllib.request.urlopen(url).read()  #en utf8

soup = BeautifulSoup(datos, 'html.parser')

tabla=soup.find_all('table')

print("\nLa tabla es\n", tabla)

cabecera=soup.find_all('th')

print("\nLa cabecera es\n", cabecera)

celdas=soup.find_all('td')

print("\nLas celdas son\n",celdas)

for celda in celdas:
    listaValores.append(celda.get_text())
    

print("\nLista con los valores extraidos de las celdas\n",listaValores)

''' Otra opción 
Usar lxml and Requests

'''

from lxml import html
import requests


print("\n------------------------------------------------------------\n")
print("\nProcesando ", url)

page = requests.get(url)
tree = html.fromstring(page.content)


cabecera= tree.xpath('//th/text()')

print("\nLa cabecera es\n", cabecera)

celdas= tree.xpath('//td/text()')

print("\nLas celdas son\n",celdas)


"Leemos ahora de una página web almacenada en un fichero local"
print("\n------------------------------------------------------------\n")

#leemos el fichero de Comunidades
#el valor de codificacion es necesario en linux

        
comunidadesFich=open('comunidadesAutonomas.htm', 'r', encoding="utf8")

comString=comunidadesFich.read()

print("\nFichero leido ")

soup = BeautifulSoup(comString, 'html.parser')

celdas=soup.find_all('td')

print(celdas)

lista=[]

for celda in celdas:
    lista.append(celda.get_text())

print("\nLista con los valores extraidos de las celdas\n",listaValores)


tree = html.fromstring(comString)

celdas= tree.xpath('//td/text()')

print("\nLas celdas son\n",celdas)



