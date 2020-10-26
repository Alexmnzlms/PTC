# -*- coding: utf-8 -*-
"""
Ejercicio 7

Realizar un programa que pida el nombre de una persona, primer apellido, segundo apellido y
que muestre por pantalla como sería el nombre completo en una sola línea. También mostrar el
nombre completo pero al revés. Finalmente volver a descomponer el nombre completo en sus tres
componentes y mostrarlos por pantalla.

Autor: Alejandro Manzanares Lemus
"""

nombre = input('Nombre: ')
apellido1 = input('Primer apellido: ')
apellido2 = input('Segundo apellido: ')

print()
print('Nombre completo: ', nombre + ' ' + apellido1 + ' ' + apellido2)
print('Nombre completo al revés: ', apellido2 + ' ' + apellido1 + ' ' + nombre)
nombre_completo = nombre + apellido1 + apellido2
print('Nombre completo al revés(2):', nombre_completo[::-1])
print('Nombre: ', nombre)
print('Primer apellido: ', apellido1)
print('Segundo apellido: ', apellido2)
