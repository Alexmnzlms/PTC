# -*- coding: utf-8 -*-
'''
R1. Calcular la variación de la población por provincias desde el año 2011 a 2017 en términos
absolutos y relativos generando la página web 1 (que debe llamarse variacionProvincias.html) que
contenga una tabla parecida a la que se puede observar en el siguiente ejemplo

Las fórmulas a aplicar son:
variación absoluta 2017=población 2017 – población 2016
variación relativa 2017=(variación absoluta 2017 / población 2016) * 100

Para una mejor comprensión se puede observar un ejemplo similar al fichero solicitado en la página
web con título: variacionProvincias2011-17.html también disponible en Prado.

Vamos a conservar el mismo orden de listado que aparece en el
poblacionProvinciasHM2010-17.csv para mantener la coherencia con los listados del INE.

Autor:Alejandro Manzanares Lemus
'''

import funciones as fn
import locale
locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

def main():
    dic, variaciones_absolutas, variaciones_relativas = fn.obtener_var_abs_rel(1,9)

    table = fn.tabla_var_provincias(dic, variaciones_absolutas, variaciones_relativas)
    
    fn.escribir_archivo('resultados/variacionProvincias.html', table)

if __name__ == "__main__":
    main()