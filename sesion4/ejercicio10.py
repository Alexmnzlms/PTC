# -*- coding: utf-8 -*-
"""
Ejercicio 10
    
Leer una frase de teclado e implementar una función que devuelva una lista de 
pares en la quedebe aparecer cada letra junto a su frecuencia de aparición. 
Los espacios no se deben tener encuenta. Dicha lista debe estar ordenada 
atendiendo al orden ascendente de las letras. Ejemplo: ante la entrada 
“programa” debe dar como salida 
[('a', 2), ('g', 1), ('m',1), ('o', 1), ('p',1), ('r',2)].

Autor: Alejandro Manzanares Lemus
"""
entrada = input('Introduzca una frase: ')
entrada = entrada.lower()

# Version sin usar los operadores de list

list_cont = []
for i in range(97,123):
    cont = 0
    for j in entrada:
        if j == chr(i):
            cont += 1
    if cont != 0:
        list_cont.append((chr(i),cont))

print('\nVersión sin operadores list')        
print('Las ocurrencias de cada letra son: ', list_cont)

# Version list

list_letras = list(entrada)

list_cont = []
for i in range(97,123):
    cont = list_letras.count(chr(i))
    if cont != 0:
        list_cont.append((chr(i),cont))
        
print('\nVersión list')   
print('Las ocurrencias de cada letra son: ', list_cont)