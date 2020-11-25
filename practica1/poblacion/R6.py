# -*- coding: utf-8 -*-

import funciones as fn
import locale
import R2 as r2
import R3 as r3
import R4 as r4
import R5 as r5

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

def main():
    listaValores = fn.obtener_tabla_html("resultados/variacionProvincias.html")
    
    listaValores1 = fn.obtener_tabla_html("entradas/variacionProvincias2011-17.htm")
    
    listaValores = listaValores[14:len(listaValores)-1]
    
    for i in range(len(listaValores)):
        listaValores[i] = listaValores[i].replace(".","")
        listaValores[i] = listaValores[i].replace(",",".")
        
    listaValoresMod = []
    for i in range(len(listaValores)):
        try:
            listaValoresMod.append(float(listaValores[i]))
        except:
            pass
        
    for i in range(len(listaValores1)):
        listaValores1[i] = listaValores1[i].replace(".","")
        listaValores1[i] = listaValores1[i].replace(",",".")
        
    for i in range(len(listaValores1)):
        listaValores1[i] = float(listaValores1[i])
    
    # print(listaValoresMod)
    # print('--------------------------------------------------------------------------------------------')
    # print(listaValores1)
    
    fallo = False
    for i,j in zip(listaValoresMod,listaValores1):
        if i != j:
            fallo = True
            print('FALLO')
            print (i, '!=', j)
            
    if not fallo:
        print('TODOS LOS VALORES SON CORRECTOS')
        
    r2.main("entradas/comunidadesAutonomasBis.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/poblacionComAutonomasBis.html")
    r3.main("entradas/comunidadesAutonomasBis.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/poblacionComAutonomasBis.html", "resultados/R3_bis.png")
    r4.main("entradas/comunidadesAutonomasBis.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/variacionComAutonomasBis.html")
    r5.main("entradas/comunidadesAutonomasBis.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/variacionComAutonomasBis.html", "resultados/R5_bis.png")

if __name__ == "__main__":  
    main()