# -*- coding: utf-8 -*-
"""
En el tercer fichero llamado “principalDecimal.py” implementamos el mismo programa en un
único fichero usando el modulo “decimal” y el tipo de dato decimal.Decimal para tratar los valores
en euros y comprobamos si obtenemos las mismas salidas para las mismas entradas en varios casos.

Autor: Alejandro Manzanares Lemus
"""

from decimal import Decimal

def calcularCapitalFinal(capitalInicial, intereses):
    
    capitalFinal = capitalInicial + (capitalInicial*intereses/100.0)
    
    print(type(str(capitalFinal)))
    return Decimal(str(capitalFinal)).quantize(Decimal("1.00"))

def val_input(numero, decimales):
    numero = numero * (10 ** decimales)
    numero = (int)(numero)
    numero = numero / (10 ** decimales)
    
    return numero
    
euros = val_input(float(input('Introduzca una cantidad en euros: ')), 2)
porcentaje = val_input(float(input('Introduzca un porcentaje: ')), 2)
tiempo = int(val_input(float(input('Introduzca un numero de años: ')), 0))

if ((porcentaje - 100.00) > 0.001):
    porcentaje = 100.00

capitalAcumulado = calcularCapitalFinal(euros,porcentaje)

for i in range(tiempo-1):
    capitalAcumulado += calcularCapitalFinal(euros,porcentaje)
    
capitalAcumulado = Decimal(str(capitalAcumulado))

print('El capital acumulado para una cantidad incial', euros, 'euros con un interes del', porcentaje, 'por ciento durante', tiempo, 'años es de:')
print(capitalAcumulado)