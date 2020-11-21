# -*- coding: utf-8 -*-

import csv
import numpy as np
import funciones as fn

def R1():
    datos = open("entradas/poblacionProvinciasHM2010-17.csv", "r", encoding="utf-8")
    
    tabla = datos.read()
    
    datos.close()
        
    primero = tabla.find("Total")
    ultimo = tabla.find("Notas")
    
    print(primero)
    print(ultimo)
    
    tabla = tabla[primero:ultimo]
    
    print(tabla)
    
    data = tabla.split("\n")
    
    data = np.array(data)
    
    print(data)
    
    dic = {}
    
    for i in data[2:len(data)-1]:
        aux = np.array(i.split(";"))
        print(aux)
        dic[aux[0]] = aux[1:9]
        
    print(dic)
    
    for i in dic["Total Nacional"]:
        print(i)
        i = fn.pasar_exponente_decimal(i)
        print(i)
    
    variaciones_absolutas = {}
    variaciones_relativas = {}
    
    for d in dic.keys():
        var_abs = np.array([])
        var_rel = np.array([])    
        for i in range(1,len(dic[d])):
            print(d, dic[d][i-1], dic[d][i])
            abso = fn.variacion_absoluta(float(dic[d][i-1]), float(dic[d][i]))
            rel = fn.variacion_relativa(abso, float(dic[d][i]))
            print(abso, rel)
            var_abs = np.append(var_abs, abso)
            var_rel = np.append(var_rel, rel)
        variaciones_absolutas[d] = var_abs
        variaciones_relativas[d] = var_rel
        
    print(variaciones_absolutas)
    print(variaciones_relativas)
            
    for d in dic.keys():
        print(d, end=" ")
        for i in variaciones_absolutas[d]:
            print(i, end=" ")
        for i in variaciones_relativas[d]:
            print(i, end=" ")
        print("")
    
    
    table = '<table><thead><tr><th rowspan="2"></th><th colspan="7">Variación absoluta</th><th colspan="7">Variación relativa</th>'
    table += '</tr><tr><td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td><td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td></tr></thead>'
    table += '<tbody>'
    
    for d in dic.keys():
        table += ('<tr><td>' + str(d) + '</td>')
        for i in variaciones_absolutas[d]:
             table += ('<td>' + str(i) + '</td>')
        for i in variaciones_relativas[d]:
             table += ('<td>' + str(i) + '</td>')
        table += '</tr>'
    
    table += '</body></table>'
    print(table)
    
    f = open('resultados/variacionProvincias.html','w', encoding="utf8" )
    f.write(table)
    f.close()

R1()