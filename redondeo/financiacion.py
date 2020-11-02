# -*- coding: utf-8 -*-
"""
Primer fichero llamado “financiacion.py”

redondear(numero, decimales)
    entrada: un float y la cantidad de decimales a redondear (usaremos 2)
    salida: un float redondeado hacia arriba a partir de 0.5 (como en el caso de los euros)

calcularCapitalFinal(capitalInicial, interes)
    entrada: un float en euros, con dos decimales, y un interés en tanto por cien con dos decimales
    salida: suma de capital inicial + interes obtenido
    la salida tiene que estar redondeada a 2 decimales pues estamos trabajando en euros

Autor: Alejandro Manzanares Lemus
"""

def redondear(numero, decimales):
    numero = numero * (10 ** decimales)
    numero += 0.5
    numero = (int)(numero)
    numero = numero / (10 ** decimales)
    
    return numero

def calcularCapitalFinal(capitalInicial, intereses):
    capitalFinal = capitalInicial + (capitalInicial*intereses/100.0)
    
    return redondear(capitalFinal, 2)
    
    

