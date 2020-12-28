#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:44:28 2020

@author: juane99
"""

import time

def buscar(palabra, sub):
    pos = -1
    coincidencias = 0
    iterador_palabra = 0
    iterador_sub = 0
    encontrado = False
    
    
    while(iterador_palabra < len(palabra) and (encontrado == False)):
            
        if palabra[iterador_palabra] == sub[iterador_sub]:
            coincidencias = coincidencias + 1
            iterador_sub = iterador_sub + 1
        else:
            if coincidencias != 0:
                iterador_palabra = iterador_palabra - 1

            coincidencias = 0
            iterador_sub = 0
                
        if coincidencias == len(sub):
            encontrado = True
            pos = iterador_palabra - len(sub) + 1
            
        iterador_palabra = iterador_palabra + 1
            
    return pos


start_time = time.time()
buscar("me llamo pepito","ito")
end_time = time.time()

print(end_time-start_time)