# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:28:24 2019

@author: Eugenio
Ejemplo para incluir el punto como separación de miles y la coma para los
decimales
"""

import locale

locale.setlocale(locale.LC_ALL,'')

capital_float=float(input("Dime capital en euros: "))

print("El capital inicial es ",locale.format_string('%.2f', capital_float, grouping=True))

#podemos seguir con problemas en el redondeo, probar con 323432432.435
#probar con 323432432.445

'''
Otros ejemlos y más información en 
https://python-para-impacientes.blogspot.com/2017/04/internacionalizacion-del-codigo-i.html

# Establecer la configuración que tenga el entorno del usuario
locale.setlocale(locale.LC_ALL, '')  

# Establecer configuraciones de países concretos:

# Establecer configuración para España en un sistema Windows
locale.setlocale(locale.LC_ALL, 'esp')  

# Establecer configuración para España en Ubuntu
locale.setlocale(locale.LC_ALL, 'es_ES.utf8')  

# Establecer configuración para España en otros sistemas GNU/Linux
locale.setlocale(locale.LC_ALL, 'es_ES')  
'''
