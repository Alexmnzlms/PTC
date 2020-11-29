# -*- coding: utf-8 -*-
'''
R4. Generar una página web 3 (fichero variacionComAutonomas.html) con una tabla con la
variación de población por comunidades autónomas desde el año 2011 a 2017, indicando variación
absoluta, relativa y desagregando dicha información por sexos, es decir, variación absoluta (hombres,
mujeres) y relativa (hombres, mujeres). Para los cálculos, hay que actuar de manera semejante que en el
apartado R1.

Autor:Alejandro Manzanares Lemus
'''

import funciones as fn
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

def main(com, prov, salida):
    dic, var_abs, var_rel = fn.obtener_var_abs_rel(10,25)
    
    dic_cod = fn.obtener_provincias_por_comunidad(com, prov)
    
    var_abs_com, var_rel_com = fn.generar_var_abs_rel(dic_cod, dic, var_abs, var_rel)
    
    table = fn.tabla_var_com_autonoma(dic_cod, var_abs_com, var_rel_com)
    
    fn.escribir_archivo(salida, table)

if __name__ == "__main__":  
    main("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/variacionComAutonomas.html")
