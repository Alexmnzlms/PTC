# -*- coding: utf-8 -*-

def redondear(numero, decimales):
    numero = numero * (10 ** decimales)
    numero += 0.5
    numero = (int)(numero)
    numero = numero / (10 ** decimales)
    
    return numero


def variacion_absoluta(a,b):
    sol = abs(a - b)
    return redondear(sol,2)

def variacion_relativa(a,b):
    sol = (a / b) * 100.0
    return redondear(sol,2)


def pasar_exponente_decimal(a):
    exp = int(a[-1::1])
    a = float(a[:len(a)-2])
    a = a * (10 ** exp)
    return int(a + 0.5)