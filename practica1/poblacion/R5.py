# -*- coding: utf-8 -*-
'''
R5. Usando Matplotlib, para las 10 comunidades elegidas en el punto R3 generar un gráfico de líneas
que refleje la evolución de la población total de cada comunidad autónoma desde el año 2010 a 2017,
salvar el gráfico a fichero e incorporarlo a la página web 3 del punto R4.

Autor:Alejandro Manzanares Lemus
'''

import locale
import numpy as np
import funciones as fn
import matplotlib.pyplot as plt

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

def main(com, prov, salida, graph):
    dic = fn.diccionario_pob_com(com, prov, "entradas/poblacionProvinciasHM2010-17.csv")
    
    dic = fn.obtener_mas_pobladas(dic, 10)
    
    # Obtenemos la suma de los datos
    
    dic_sum = {}
    for d in dic.keys():
        aux = np.array([])
        for i in range(int(len(dic[d])/2)):
            aux = np.append(aux, (dic[d][i] + dic[d][i+8]))
            
        dic_sum[d] = aux
    
    # Generamos el gráfico
    
    list_years = []
    for i in range(2017, 2009, -1):
        list_years.append(i)
        
    fig, ax = plt.subplots()
    ax.set_ylabel('Población')
    ax.set_title('Variación de la población')
    
    
    for d in dic_sum.keys():
        ax.plot(list_years, dic_sum[d], marker='o', label=d)
        
        
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        
    fig.set_size_inches(12.5,5.5)
    fig.tight_layout()
    
    plt.savefig(graph,bbox_inches='tight')
    
    dic, var_abs, var_rel = fn.obtener_var_abs_rel(10,25)
    dic_cod = fn.obtener_provincias_por_comunidad(com, prov)
    
    var_abs_com, var_rel_com = fn.generar_var_abs_rel(dic_cod, dic, var_abs, var_rel)
    
    table = fn.tabla_var_com_autonoma(dic_cod, var_abs_com, var_rel_com)
    
    # Insertamos el gráfico en el html
    
    graph = graph.replace("imagenes","../imagenes")
    
    page = '<img src="' + graph + '">' + table
    
    fn.escribir_archivo(salida, page)

if __name__ == "__main__":      
    main("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/variacionComAutonomas.html", "imagenes/R5.png")