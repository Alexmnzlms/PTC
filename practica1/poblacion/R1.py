# -*- coding: utf-8 -*-

import csv
import numpy as np
import funciones as fn
import locale
locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

def R1():
    dic, variaciones_absolutas, variaciones_relativas = fn.obtener_var_abs_rel(1,9)

    
    table = '<table><thead><tr><th rowspan="2"></th><th colspan="7">Variación absoluta</th><th colspan="7">Variación relativa</th>'
    table += '</tr><tr><td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td><td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td></tr></thead>'
    table += '<tbody>'
    
    for d in dic.keys():
        table += ('<tr><td>' + str(d) + '</td>')
        for i in variaciones_absolutas[d]:
             table += ('<td>' + locale.format_string('%.2f',i, grouping=True) + '</td>')
        for i in variaciones_relativas[d]:
             table += ('<td>' + locale.format_string('%.2f',i, grouping=True) + '</td>')
        table += '</tr>'
    
    table += '</body></table>'
    # print(table)
    
    fn.escribir_archivo('resultados/variacionProvincias.html', table)

R1()