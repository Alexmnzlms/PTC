# -*- coding: utf-8 -*-
"""
En el tercer fichero llamado “principalDecimal.py” implementamos el mismo programa en un
único fichero usando el modulo “decimal” y el tipo de dato decimal.Decimal para tratar los valores
en euros y comprobamos si obtenemos las mismas salidas para las mismas entradas en varios casos.

Autor: Alejandro Manzanares Lemus
"""

import decimal
from decimal import Decimal, getcontext


def calcularCapitalFinal(capitalInicial, intereses):
    
    getcontext().rounding = decimal.ROUND_HALF_UP
    capitalInicial = Decimal(capitalInicial)#.quantize(Decimal("0.01"))
    intereses = Decimal(intereses)#.quantize(Decimal("0.01"))
    
    capitalFinal = capitalInicial + (capitalInicial*intereses/Decimal(100.00))
    print(capitalFinal.quantize(Decimal("0.01")))

    return capitalFinal.quantize(Decimal("0.01"))

def val_input(numero, decimales):
    numero = numero * (10 ** decimales)
    numero = (int)(numero)
    numero = numero / (10 ** decimales)
    #numero = Decimal(numero).quantize(Decimal("0.01"))
    
    return numero
    
euros = val_input(float(input('Introduzca una cantidad en euros: ')), 2)
porcentaje = val_input(float(input('Introduzca un porcentaje: ')), 2)
tiempo = int(val_input(float(input('Introduzca un numero de años: ')), 0))

if ((porcentaje - 100.00) > 0.001):
    porcentaje = 100.00

capitalAcumulado = calcularCapitalFinal(euros,porcentaje)
for i in range(tiempo-1):
    capitalAcumulado = calcularCapitalFinal(capitalAcumulado,porcentaje)
    

print('El capital acumulado para una cantidad incial', euros, 'euros con un interes del', porcentaje, 'por ciento durante', tiempo, 'años es de:')
print(capitalAcumulado)