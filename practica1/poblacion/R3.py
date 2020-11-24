# -*- coding: utf-8 -*-

import R2 as r2
import locale
import numpy as np
import funciones as fn
import matplotlib.pyplot as plt

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

def R3(com, prov, salida, graph):
    
    dic = fn.diccionario_pob_com(com, prov, "entradas/poblacionProvinciasHM2010-17.csv")
    
    dic = fn.obtener_mas_pobladas(dic, 10)
    
    # fn.print_dic(dic)
    
    dic_total = {}
    for d in dic.keys():
        cont = 0.0
        med = 0
        for i in dic[d][:7]:
            cont += i
            med += 1
            
        pob_hom = cont / med
        
        cont = 0.0
        med = 0
        for i in dic[d][8:len(dic[d])-1]:
            cont += i
            med += 1
            
        pob_muj = cont / med
            
        dic_total[d] = np.array([pob_hom,pob_muj])
        
    # fn.print_dic(dic_total)
    
    list_keys = []
    list_hom = []
    list_muj = []
    
    for d in dic_total.keys():
        list_keys.append(d)
        list_hom.append(dic_total[d][0])
        list_muj.append(dic_total[d][1])
    
    
    x = np.arange(len(list_keys))  # the label locations
    width = 0.35  # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, list_hom, width, label='Poblacíon de Hombres')
    rects2 = ax.bar(x + width/2, list_muj, width, label='Poblacíon de Mujeres')
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Población')
    ax.set_title('Media de población entre el año 2017-2010')
    ax.set_xticks(x)
    ax.set_xticklabels(list_keys)
    ax.legend()
    
    fn.autolabel(rects1,ax)
    fn.autolabel(rects2,ax)
    
    fig.set_size_inches(25, 10.5)
    fig.tight_layout()
    
    plt.savefig(graph,bbox_inches='tight')
    
    table = '<table><thead><tr><th rowspan="2"></th><th colspan="7">Población de Hombres</th><th colspan="7">Población de Mujeres</th>'
    table += '</tr><tr><td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td><td>2010</td><td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td><td>2010</td></tr></thead>'
    table += '<tbody>'
    
    for d in dic.keys():
        table += ('<tr><td>' + str(d) + '</td>')
        for i in dic[d]:
             table += ('<td>' + locale.format_string('%.2f',i, grouping=True) + '</td>')
        table += '</tr>'
    table += '</body></table>'
    
    graph = graph.replace("resultados/","")
    
    page = '<img src="' + graph + '">' + table
    
    fn.escribir_archivo(salida, page)
    
R3("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/poblacionComAutonomas.html", "resultados/R3.png")