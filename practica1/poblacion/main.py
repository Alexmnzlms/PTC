# -*- coding: utf-8 -*-

import R1 as r1
import R2 as r2
import R3 as r3
import R4 as r4
import R5 as r5
import R6 as r6
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

r1.R1()
r2.R2("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/poblacionComAutonomas.html")
r3.R3("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/poblacionComAutonomas.html", "resultados/R3.png")
r4.R4("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/variacionComAutonomas.html")
r5.R5("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/variacionComAutonomas.html", "resultados/R5.png")
r6.R6()