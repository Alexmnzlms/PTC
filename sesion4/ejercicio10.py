# -*- coding: utf-8 -*-
"""
Ejercicio 10
    
Leer una frase de teclado e implementar una función que devuelva una lista de 
pares en la quedebe aparecer cada letra junto a su frecuencia de aparición. 
Los espacios no se deben tener encuenta. Dicha lista debe estar ordenada 
atendiendo al orden ascendente de las letras. Ejemplo: antela entrada 
“programa” debe dar como salida 
[('a', 2), ('g', 1), ('m',1), ('o', 1), ('p',1), ('r',2)].

Autor: Alejandro Manzanares Lemus
"""

entrada = input('Introduzca una frase por favor: ')
entrada = entrada.lower()
entrada_sin_esp = ""

for i in entrada:
    if i != ' ':
        entrada_sin_esp += i
        
entrada = entrada_sin_esp

list_cont = []
for i in range(97,123):
    cont = 0
    for j in entrada:
        if j == chr(i):
            cont += 1
    if cont != 0:
        list_cont.append((chr(i),cont))
        
print('Las ocurrencias de cada letra son: ', list_cont)