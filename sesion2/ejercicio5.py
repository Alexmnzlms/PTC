# -*- coding: utf-8 -*-
"""
Ejercicio 5

Hacer un programa para calcular la diferencia en horas:minutos:segundos entre dos instantes de
tiempo dados en horas:minutos:segundos.

Autor: Alejandro Manzanares Lemus
"""

print('Por favor introduzca dos instantes de tiempo: (hh:mm:ss)')
hora_i, minuto_i, segundo_i = input().split(':')
hora_f, minuto_f, segundo_f = input().split(':')

fallo = False

segundo_i = int(segundo_i)
segundo_f = int(segundo_f)

if (segundo_i > 59 or segundo_f > 59):
    print('El numero de segundos no puede ser superior a 59')
    fallo = True
    
minuto_i = int(minuto_i)
minuto_f = int(minuto_f)

if (minuto_i > 59 or minuto_f > 59):
    print('El numero de minutos no puede ser superior a 59')
    fallo = True

hora_i = int(hora_i)
hora_f = int(hora_f)

if(not fallo):
    seg_i = abs((hora_i * 3600 + minuto_i * 60 + segundo_i) - (hora_f * 3600 + minuto_f * 60 + segundo_f))
    dif_h = int(seg_i/3600)
    seg_i = seg_i%3600
    dif_m = int(seg_i/60)
    dif_s = int(seg_i%60)
    print('Han pasado un total de:', dif_h, 'horas', dif_m, 'minutos', dif_s, 'segundos')
    
else:
    print('Formato hh:mm:ss incorrecto')