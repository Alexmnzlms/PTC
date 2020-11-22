# -*- coding: utf-8 -*-

import csv
import numpy as np
import funciones as fn
from bs4 import BeautifulSoup
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')
def R2(com, prov, salida):

    dic_cod = fn.obtener_provincias_por_comunidad(com, prov)
        
    fn.print_dic(dic_cod)
    
    dic_datos = {}
    
    for k in dic_cod.keys():
        for p in dic_cod[k]:
            dic_datos[p] = np.array([])
       
    data = fn.open_csv_data("entradas/poblacionProvinciasHM2010-17.csv")
    
    data = data[3:len(data)-1]
    
    for dato in data:
        linea = np.array(dato.split(";"))
        indice = linea[0:1]
        try:
            dic_datos[indice[0]] = np.append(dic_datos[indice[0]], linea[9:len(linea) - 1])
            dic_datos[indice[0]] = list(map(lambda x: float(x), dic_datos[indice[0]]))
        except:
            print('Clave no encontrada:', indice[0])
    
    # fn.print_dic(dic_datos)
    
    dic_datos_com = {}
    
    for d in dic_cod.keys():
        dic_datos_com[d] = np.zeros((2017-2010+1)*2)
        
    for c in dic_cod.keys():
        for p in dic_cod[c]:
            for i in range(len(dic_datos[p])):
                dic_datos_com[c][i] += dic_datos[p][i]
                # print(c,p,i,dic_datos[p][i],dic_datos_com[c][i])
    
    # fn.print_dic(dic_datos_com)
    
    table = '<table><thead><tr><th rowspan="2"></th><th colspan="7">Población de Hombres</th><th colspan="7">Población de Mujeres</th>'
    table += '</tr><tr><td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td><td>2010</td><td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td><td>2010</td></tr></thead>'
    table += '<tbody>'
        
    for d in dic_datos_com.keys():
        table += ('<tr><td>' + str(d) + '</td>')
        for i in dic_datos_com[d]:
             table += ('<td>' + locale.format_string('%.2f',i, grouping=True) + '</td>')
        table += '</tr>'
    table += '</body></table>'
        
    fn.escribir_archivo(salida, table)
    
R2("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/poblacionComAutonomas.html")