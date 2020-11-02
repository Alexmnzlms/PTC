# -*- coding: utf-8 -*-
"""
Segundo fichero llamado “principalEuros.py”

Debe pedir por teclado una cantidad de dinero en euros, un interes anual en tanto por ciento y un
número de años. Todos los valores deben pasar por un mecanismo de validación de modo que solo
admita valores válidos como por ejemplo, capital: 5689.34 interés: 10.05 % años: 12.

El programa debe darnos como respuesta el capital acumulado, aplicando el interés anual durante el
número de años indicado, usando las funciones del módulo financiacion.py

Las funciones de validación de las entrada pueden estar en el fichero principal si se estima
conveniente.

Autor: Alejandro Manzanares Lemus
"""

import financiacion as fn

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

capitalAcumulado = fn.calcularCapitalFinal(euros,porcentaje)

for i in range(tiempo-1):
    capitalAcumulado += fn.calcularCapitalFinal(euros,porcentaje)

capitalAcumulado = fn.redondear(capitalAcumulado,2)

print('El capital acumulado para una cantidad incial', euros, 'euros con un interes del', porcentaje, 'por ciento durante', tiempo, 'años es de:')
print(capitalAcumulado)