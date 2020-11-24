# -*- coding: utf-8 -*-

import csv
import numpy as np
import funciones as fn
from bs4 import BeautifulSoup
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

def R2(com, prov, salida):
    
    dic_datos_com = fn.diccionario_pob_com(com, prov, "entradas/poblacionProvinciasHM2010-17.csv")
    
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