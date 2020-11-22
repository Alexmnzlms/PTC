# -*- coding: utf-8 -*-

import R1 as r1
import R2 as r2
import R4 as r4
import R6 as r6
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

r1.R1()
r2.R2("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/poblacionComAutonomas.html")
r4.R4("entradas/comunidadesAutonomas.htm","entradas/comunidadAutonoma-Provincia.htm","resultados/variacionComAutonomas.html")
r6.R6()