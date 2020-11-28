# -*- coding: utf-8 -*-

import funciones as fn
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

def main(com, prov, salida):
    
    dic_datos_com = fn.diccionario_pob_com(com, prov, "entradas/poblacionProvinciasHM2010-17.csv")
    
    table = fn.tabla_pob_com_autonoma(dic_datos_com)
    
    print(table)
        
    fn.escribir_archivo(salida, table)

if __name__ == "__main__":  
    main("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/poblacionComAutonomas.html")