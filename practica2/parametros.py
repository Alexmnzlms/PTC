#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Archivo: parametros.py
Autor: Alejandro Manzanares Lemus

Implementación de la clase Parametros que permite almacenar los parametros
que se utilizan en el programa
'''

class Parametros:
	def __init__(self, it, cer, med, lej, minp, maxp, ud):
		self.it = int(it)
		self.cer = float(cer)
		self.med = float(med)
		self.lej = float(lej)
		self.minp = int(minp)
		self.maxp = int(maxp)
		self.ud = float(ud)

	def show(self):
		print("Parametros:\n", self.it, self.cer, self.med, self.lej, self.minp, self.maxp, self.ud)


