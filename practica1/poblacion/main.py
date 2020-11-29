# -*- coding: utf-8 -*-
'''
Scritp que permite ejecutar todos los resultados R1.py-R6.py

Autor:Alejandro Manzanares Lemus
'''

import R1 as r1
import R2 as r2
import R3 as r3
import R4 as r4
import R5 as r5
import R6 as r6
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

print('Ejecutando resultado 1...')
r1.main()
print('Ejecutando resultado 2...')
r2.main("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/poblacionComAutonomas.html")
print('Ejecutando resultado 3...')
r3.main("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/poblacionComAutonomas.html", "resultados/R3.png")
print('Ejecutando resultado 4...')
r4.main("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/variacionComAutonomas.html")
print('Ejecutando resultado 5...')
r5.main("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/variacionComAutonomas.html", "resultados/R5.png")
print('Ejecutando resultado 6...')
r6.main()
print('Ejecución de todos los resultados exitosa')