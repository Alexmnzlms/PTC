# -*- coding: utf-8 -*-

import csv
import numpy as np
import funciones as fn
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

def R4(com, prov, salida):
    dic, var_abs, var_rel = fn.obtener_var_abs_rel(10,25)
    dic_cod = fn.obtener_provincias_por_comunidad(com, prov)
     
    fn.print_dic(dic)
    fn.print_dic(dic_cod)
    fn.print_dic(var_abs)
    fn.print_dic(var_rel)
    
    var_abs_com = {}
    var_rel_com = {}
    for c in dic_cod.keys():
        var_abs_com[c] = np.zeros(14)
        var_rel_com[c] = np.zeros(14)
    
    for c in dic_cod.keys():
        for p in dic_cod[c]:
            for i in range(len(dic[p])-1):
                var_abs_com[c][i] += var_abs[p][i]
                var_rel_com[c][i] += var_rel[p][i]
                print(c,p,i,var_abs[p][i],var_rel[p][i],var_abs_com[c][i],var_rel_com[c][i])
    
    table = '<table><thead><tr><th></th><th colspan="14">Variación absoluta</th><th colspan="14">Variación relativa</th></tr></thead>'
    table += '<tbody><tr><td></td><td colspan="7">Hombres</td><td colspan="7">Mujeres</td><td colspan="7">Hombres</td><td colspan="7">Mujeres</td></tr><tr><td></td>'
    table += '<td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td><td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td><td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td><td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td></tr>'
    
    for d in dic_cod.keys():
        table += ('<tr><td>' + str(d) + '</td>')
        for i in var_abs_com[d]:
             table += ('<td>' + locale.format_string('%.2f',i, grouping=True) + '</td>')
        for i in var_rel_com[d]:
             table += ('<td>' + locale.format_string('%.2f',i, grouping=True) + '</td>')
        table += '</tr>'
    
    table += '</tbody></table>'
    # print(table)
    
    fn.escribir_archivo(salida, table)

R4("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/variacionComAutonomas.html")
