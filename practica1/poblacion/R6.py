# -*- coding: utf-8 -*-
'''
R6. Usando como entrada la página web 1 generada en el apartado 1 llamada
variacionProvincias.html y el fichero proporcionado variacionProvincias2011-17.html hay que
implementar un programa que compare los datos de variación de población de 2011 a 2017 (absoluta y
relativa) de ambos ficheros para comprobar que son los mismos valores en cada caso. Despúes usar el
fichero comunidadesAutonomasBis.html para generar una versión Bis de las páginas web 2 (ver R2
y R3) y web 3 (ver R4 y R5) con sus respectivos gráficos debiendo llamarse
poblacionComAutonomasBis.html y variacionComAutonomasBis.html respectivamente.

Autor:Alejandro Manzanares Lemus
'''

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
    
    # Formateamos los valores obtenidos
    
    for i in range(len(listaValores)):
        listaValores[i] = listaValores[i].replace(".","")
        listaValores[i] = listaValores[i].replace(",",".")
        
    # Convertimos los valores en float
    
    listaValoresMod = []
    for i in range(len(listaValores)):
        try:
            listaValoresMod.append(float(listaValores[i]))
        except:
            pass
        
    # Formateamos los valores obtenidos
    
    for i in range(len(listaValores1)):
        listaValores1[i] = listaValores1[i].replace(".","")
        listaValores1[i] = listaValores1[i].replace(",",".")
        
     # Convertimos los valores en float
        
    for i in range(len(listaValores1)):
        listaValores1[i] = float(listaValores1[i])
    
    # Realizamos la comparación
    
    fallo = False
    for i,j in zip(listaValoresMod,listaValores1):
        if i != j:
            fallo = True
            print('FALLO')
            print (i, '!=', j)
            
    if not fallo:
        print('TODOS LOS VALORES SON CORRECTOS')
        
    # Generamos los resultados nuevos llamando a los scripts anteriores
    
    r2.main("entradas/comunidadesAutonomasBis.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/poblacionComAutonomasBis.html")
    r3.main("entradas/comunidadesAutonomasBis.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/poblacionComAutonomasBis.html", "resultados/R3_bis.png")
    r4.main("entradas/comunidadesAutonomasBis.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/variacionComAutonomasBis.html")
    r5.main("entradas/comunidadesAutonomasBis.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/variacionComAutonomasBis.html", "resultados/R5_bis.png")

if __name__ == "__main__":  
    main()