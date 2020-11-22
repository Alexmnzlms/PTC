# -*- coding: utf-8 -*-

import numpy as np
from bs4 import BeautifulSoup

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
            print('Clave no encontrada:', provincias[i])
    
    # print()
    # print('Provincias que pertenecen a cada comunidad:')
    return dic_cod