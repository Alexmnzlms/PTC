# -*- coding: utf-8 -*-

import funciones as fn
import locale
locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

def main():
    dic, variaciones_absolutas, variaciones_relativas = fn.obtener_var_abs_rel(1,9)

    table = fn.tabla_var_provincias(dic, variaciones_absolutas, variaciones_relativas)
    
    fn.escribir_archivo('resultados/variacionProvincias.html', table)

if __name__ == "__main__":
    main()