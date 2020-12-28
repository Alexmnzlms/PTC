'''
Archivo: mainInterfaz.py
Autor: Alejandro Manzanares Lemus

Implementación de la interfaz gráfica con tkinter
'''

import tkinter
from tkinter import *

def exit():
	global root
	root.destroy()

def main():
	global root
	root = tkinter.Tk()
	root.geometry("700x300")
	root.title("Práctica PTC Tkinter Robótica")

	status = StringVar()

	warning = Label(root, text="Es necesario ejecutar el simulador VREP")
	conectar = Button(root, text="Conectar con VREP")
	detydesc = Button(root, text="Detener y Desconectar VREP")
	estado = Label(root, text=status)
	capturar = Button(root, text="Capturar")
	agrupar = Button(root, text="Agrupar")
	excaract = Button(root, text="Extraer caracteristicas")
	enclasif = Button(root, text="Entrenar clasificador")
	predecir = Button(root, text="Predecir")
	salir = Button(root, text="Salir", command=exit)

	parametros = Label(root, text="Parámetros")
	iteraciones = Label(root, text="Iteraciones:")
	cerca = Label(root, text="Cerca:")
	media = Label(root, text="Media:")
	lejos = Label(root, text="Lejos:")
	minp = Label(root, text="MinPuntos:")
	maxp = Label(root, text="MaxPuntos:")
	umbrald = Label(root, text="UmbralDistancia:")
	cambiar = Button(root, text="Cambiar")

	varit = Entry(root,width=5)
	varcer = Entry(root,width=5)
	varmed = Entry(root,width=5)
	varlej = Entry(root,width=5)
	varmin = Entry(root,width=5)
	varmax = Entry(root,width=5)
	varud = Entry(root,width=5)

	ficheros = Label(root, text="Ficheros para la captura")
	lista = Listbox(root, width=35, height=12)

	warning.grid(row=0, column=0)
	conectar.grid(row=1, column=0)
	detydesc.grid(row=2, column=0)
	estado.grid(row=3, column=0)
	capturar.grid(row=4, column=0)
	agrupar.grid(row=5, column=0)
	excaract.grid(row=6, column=0)
	enclasif.grid(row=7, column=0)
	predecir.grid(row=8, column=0)
	salir.grid(row=9, column=0)

	parametros.grid(row=1, column=1)
	iteraciones.grid(row=2, column=1)
	cerca.grid(row=3, column=1)
	media.grid(row=4, column=1)
	lejos.grid(row=5, column=1)
	minp.grid(row=6, column=1)
	maxp.grid(row=7, column=1)
	umbrald.grid(row=8, column=1)
	cambiar.grid(row=9, column=1)

	varit.grid(row=2, column=2)
	varcer.grid(row=3, column=2)
	varmed.grid(row=4, column=2)
	varlej.grid(row=5, column=2)
	varmin.grid(row=6, column=2)
	varmax.grid(row=7, column=2)
	varud.grid(row=8, column=2)

	ficheros.grid(row=1,column=3)
	lista.grid(row=3, column=3, rowspan=6)

	root.mainloop()

main()
