# -*- coding: utf-8 -*-

import numpy as np
from bs4 import BeautifulSoup
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

def compare_float(a, b):
    epsilon = 0.0001
    if a - b > epsilon:
        return False
    else:
        return True

def variacion_absoluta(a,b):
    sol = a - b
    return sol

def variacion_relativa(a,b):
    sol = (a / b) * 100.0
    return sol

def pasar_exponente_decimal(a):
    exp = int(a[-1::1])
    a = float(a[:len(a)-2])
    a = a * (10 ** exp)
    return int(a + 0.5)

def eliminar_valor_lista(lista,valor):
    l = []
    for v in lista:
        if v != valor:
            l.append(v)
            
    return l

def print_dic(dic):
    for d in dic:
        print(d, ':', len(dic[d]), dic[d])
        
def open_csv_data(ruta): 
    datos = open(ruta, "r", encoding="utf-8")
    
    tabla = datos.read()
    
    datos.close()
        
    primero = tabla.find("Total")
    ultimo = tabla.find("Notas")
    
    # print(primero)
    # print(ultimo)
    
    tabla = tabla[primero:ultimo]
    
    # print(tabla)
    
    data = tabla.split("\n")
    
    data = np.array(data)
    
    return data

def escribir_archivo(ruta, contenido):
    f = open(ruta,'w', encoding="utf8" )
    f.write(contenido)
    f.close()
    
def obtener_var_abs_rel(col_i, col_f):
    data = open_csv_data("entradas/poblacionProvinciasHM2010-17.csv")
    
    # print(data)
    
    dic = {}
    
    for i in data[2:len(data)-1]:
        aux = np.array(i.split(";"))
        # print(aux)
        dic[aux[0]] = aux[col_i:col_f]
        
    # print(dic)
    
    for i in dic["Total Nacional"]:
        # print(i)
        i = pasar_exponente_decimal(i)
        # print(i)
    
    variaciones_absolutas = {}
    variaciones_relativas = {}
    
    for d in dic.keys():
        var_abs = np.array([])
        var_rel = np.array([])    
        for i in range(1,len(dic[d])):
            # print(d, dic[d][i-1], dic[d][i])
            abso = variacion_absoluta(float(dic[d][i-1]), float(dic[d][i]))
            rel = variacion_relativa(abso, float(dic[d][i]))
            # print(abso, rel)
            var_abs = np.append(var_abs, abso)
            var_rel = np.append(var_rel, rel)
        variaciones_absolutas[d] = var_abs
        variaciones_relativas[d] = var_rel
        
    return dic, variaciones_absolutas, variaciones_relativas
    
def obtener_tabla_html(ruta):
    listaValores = []
    
    html = open(ruta, "r", encoding="utf-8")
    
    datos=html.read()
    
    soup=BeautifulSoup(datos, 'html.parser')
    celdas=soup.find_all('td')
    
    for celda in celdas:
        listaValores.append(celda.get_text())
    
    return listaValores
    
def obtener_provincias_por_comunidad(com_aut, prov):
    listaValores = obtener_tabla_html(com_aut)
        
    # print("\nLista con los valores extraidos de las celdas\n",listaValores)
    
    comunidades = np.array([])
    for i in range(0, len(listaValores) - 1, 2):
        if (listaValores[i] == '08 '):
            comunidades = np.append(comunidades, (listaValores[i] + 'Castilla-La Mancha'))
        else:
            comunidades = np.append(comunidades, (listaValores[i] + listaValores[i+1]))
    
    # print(comunidades)
    
    dic_cod = {}
    for k in comunidades:
        dic_cod[k] = np.array([])
    
    # print(dic_cod)
    
    listaValores1 = obtener_tabla_html(prov)
    
    listaValores1 = eliminar_valor_lista(listaValores1,'')
    listaValores1 = eliminar_valor_lista(listaValores1,'Ciudades    Autónomas:')
    
    # print("\nLista con los valores extraidos de las celdas\n",listaValores1)
    
    provincias = np.array([])
    for i in range(0, len(listaValores1) - 1, 2):
        provincias = np.append(provincias, (listaValores1[i] + ' ' + listaValores1[i+1]))
    
    # print(provincias)
    
    for i in range(0,len(provincias) - 1, 2):
        try:
            dic_cod[provincias[i]] = np.append(dic_cod[provincias[i]], provincias[i+1])
        except:
            pass
    
    # print()
    # print('Provincias que pertenecen a cada comunidad:')
    return dic_cod

def diccionario_pob_com(com, prov, ruta):
    dic_cod = obtener_provincias_por_comunidad(com, prov)
        
    # fn.print_dic(dic_cod)
    
    dic_datos = {}
    
    for k in dic_cod.keys():
        for p in dic_cod[k]:
            dic_datos[p] = np.array([])
            
    data = open_csv_data(ruta)
    
    data = data[3:len(data)-1]
    
    for dato in data:
        linea = np.array(dato.split(";"))
        indice = linea[0:1]
        try:
            dic_datos[indice[0]] = np.append(dic_datos[indice[0]], linea[9:len(linea) - 1])
            dic_datos[indice[0]] = list(map(lambda x: float(x), dic_datos[indice[0]]))
        except:
            pass
    
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
    
    return dic_datos_com

def obtener_mas_pobladas(dic, num):

    dic_aux = {}
    
    for d in dic.keys():
        cont = 0.0
        for i in dic[d]:
            cont += i
        
        dic_aux[d] = cont
        
    list_keys = []
    for i in range(num):
        max = 0
        key = ""
        for d in dic_aux.keys():
            if max < dic_aux[d]:
                max = dic_aux[d]
                key = d
        list_keys.append(key)
        del dic_aux[key]
    
    dic_mp = {}
    for k in list_keys:
        dic_mp[k] = dic[k]
    
    return dic_mp

def autolabel(rects,ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{:.2f}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
   
def generar_var_abs_rel(dic_cod, dic, var_abs, var_rel):
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
                # print(c,p,i,var_abs[p][i],var_rel[p][i],var_abs_com[c][i],var_rel_com[c][i])
    
    return var_abs_com, var_rel_com

def tabla_var_provincias(dic, variaciones_absolutas, variaciones_relativas):
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
    
    return table

def tabla_pob_com_autonoma(dic_datos_com):
    table = '<table><thead><tr><th rowspan="2"></th><th colspan="7">Población de Hombres</th><th colspan="7">Población de Mujeres</th>'
    table += '</tr><tr><td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td><td>2010</td><td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td><td>2010</td></tr></thead>'
    table += '<tbody>'
        
    for d in dic_datos_com.keys():
        table += ('<tr><td>' + str(d) + '</td>')
        for i in dic_datos_com[d]:
             table += ('<td>' + locale.format_string('%.2f',i, grouping=True) + '</td>')
        table += '</tr>'
    table += '</body></table>'
    
    return table

def tabla_var_com_autonoma(dic_cod, var_abs_com, var_rel_com):
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
    
    return table
    