# -*- coding: utf-8 -*-
'''
R2. Usando el listado de comunidades autónomas que podemos obtener del fichero
comunidadesAutonomas.html, así como de las provincias de cada comunidad autónoma que podemos
obtener de comunidadAutonoma-Provincia.html y los datos de poblacionProvinciasHM2010-
17.csv, hay que generar una página web 2 (fichero poblacionComAutonomas.html) con una tabla
con los valores de población de cada comunidad autónoma en cada año de 2010 a 2017, indicando
también los valores desagregados por sexos (de manera semejante a como aparece en el fichero
poblacionProvinciasHM2010-17.csv)

Conservar el orden que presenta comunidadesAutonomas.html

Autor:Alejandro Manzanares Lemus
'''

import funciones as fn
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

def main(com, prov, salida):
    
    dic_datos_com = fn.diccionario_pob_com(com, prov, "entradas/poblacionProvinciasHM2010-17.csv")
    
    table = fn.tabla_pob_com_autonoma(dic_datos_com)
        
    fn.escribir_archivo(salida, table)

if __name__ == "__main__":  
    main("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/poblacionComAutonomas.html")