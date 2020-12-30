'''
Archivo: mainInterfaz.py
Autor: Alejandro Manzanares Lemus

Implementación de la interfaz gráfica con tkinter
'''

import tkinter
from tkinter import *
from tkinter.messagebox import *
import vrep
import os
import parametros as param
import capturar as capture_py
import agrupar as group_py
import caracteristicas as caract_py
import clasificarSVM as svm_py
import predecir as predict_py


params = param.Parametros(50,0.5,1.5,2.5,3,10,0.05)

def conectar_con_VREP():
	global root, status, clientID, capturar, detydesc, detenido
	vrep.simxFinish(-1) #Terminar todas las conexiones

	#Iniciar una nueva conexion en el puerto 19999 (direccion por defecto)
	clientID = vrep.simxStart('127.0.0.1',19999,True,True,5000,5)

	if clientID != -1:
		showinfo("Práctica PTC Tkinter Robótica", "Conexión con VREP establecida")
		status.set("Conectado a VREP")
		capturar['state'] = 'normal'
		detydesc['state'] = 'normal'
		detenido = False

		agrupar['state'] = 'normal'
		excaract['state'] = 'normal'
		enclasif['state'] = 'normal'
		predecir['state'] = 'normal'

	else:
		showerror("Práctica PTC Tkinter Robótica", "Debe iniciar el simulador")

def detener_y_desconectar():
	global root, status, clientID, detenido, agrupar, excaract, enclasif, predecir

	if clientID != -1:
		vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot_wait)
		vrep.simxFinish(-1)
		showinfo("Práctica PTC Tkinter Robótica", "Se ha desconectado de VREP")
		status.set("No conectado a VREP")
		capturar['state'] = 'disabled'
		detydesc['state'] = 'disabled'
		#agrupar['state'] = 'disabled'
		#excaract['state'] = 'disabled'
		#enclasif['state'] = 'disabled'
		#predecir['state'] = 'disabled'
		detenido = True

def capture():
	global lista, agrupar, params, clientID

	if lista.curselection():
		seleccion = lista.get(lista.curselection()[0])
		carpeta = seleccion.split("/")[0]

		if not os.path.isfile(seleccion):
			pregunta = "Se va a crear el fichero:\n" + seleccion  + " ¿Está seguro?"
		else:
			pregunta = "El fichero: " + seleccion  + " Ya existe, Se creará de nuevo. ¿Está seguro?"

		permiso = askyesno("Práctica PTC Tkinter Robótica", pregunta)

		if permiso:
			#Llamar script capturar.py
			capture_py.capturar(clientID, seleccion, params)

		#agrupar['state'] = 'normal'

	else:
		showwarning("Práctica PTC Tkinter Robótica", "Debe elegir un fichero de la lista")

def group():
	global excaract

	# Llamar script agrupar.py
	group_py.agrupar(params)

	#excaract['state'] = 'normal'

def extraer():
	global enclasif

	# Llamar script caracteristicas.py
	caract_py.caracteristicas()

	#enclasif['state'] = 'normal'

def entrenar():
	global predecir

	# Llamar script clasificarSVM.py
	svm_py.clasificarSVM()

	#predecir['state'] = 'normal'

def predict():
	# Llamar script predecir.py
	predict_py.predecir()

def change():
	global varit, varcer, varmed, varlej, varmin, varmax, varud, params

	if varit.get():
		params.it = int(varit.get())

	if varcer.get():
		params.cer = float(varcer.get())

	if varmed.get():
		params.med = float(varmed.get())

	if varlej.get():
		params.lej = float(varlej.get())

	if varmin.get():
		params.minp = int(varmin.get())

	if varmax.get():
		params.maxp = int(varmax.get())

	if varud.get():
		params.ud = float(varud.get())

	params.show()

	varit.delete(0,'end')
	varcer.delete(0,'end')
	varmed.delete(0,'end')
	varlej.delete(0,'end')
	varmin.delete(0,'end')
	varmax.delete(0,'end')
	varud.delete(0,'end')

	varit.insert(0,params.it)
	varcer.insert(0,params.cer)
	varmed.insert(0,params.med)
	varlej.insert(0,params.lej)
	varmin.insert(0,params.minp)
	varmax.insert(0,params.maxp)
	varud.insert(0,params.ud)

def exit():
	global root, detenido

	if detenido:
		salir = askyesno("Práctica PTC Tkinter Robótica","¿Está seguro de qué desea salir?")
		if salir:
			root.destroy()
	else:
		showwarning("Práctica PTC Tkinter Robótica", "Antes de salir debe desconectar")

def main():
	global root, status, capturar, detydesc, detenido, lista, agrupar, excaract, enclasif, predecir, varit, varcer, varmed, varlej, varmin, varmax, varud
	root = tkinter.Tk()
	root.geometry("700x300")
	root.title("Práctica PTC Tkinter Robótica")

	status = StringVar()
	status.set("No conectado a VREP")
	detenido = True

	warning = Label(root, text="Es necesario ejecutar el simulador VREP")
	conectar = Button(root, text="Conectar con VREP", command=conectar_con_VREP)
	detydesc = Button(root, text="Detener y Desconectar VREP", command=detener_y_desconectar ,state=DISABLED)
	estado = Label(root, textvariable=status)
	capturar = Button(root, text="Capturar", command=capture ,state=DISABLED)
	agrupar = Button(root, text="Agrupar", command=group, state=DISABLED)
	excaract = Button(root, text="Extraer caracteristicas", command=extraer, state=DISABLED)
	enclasif = Button(root, text="Entrenar clasificador", command=entrenar, state=DISABLED)
	predecir = Button(root, text="Predecir", command=predict, state=DISABLED)
	salir = Button(root, text="Salir", command=exit)

	parametros_etiq = Label(root, text="Parámetros")
	iteraciones = Label(root, text="Iteraciones:")
	cerca = Label(root, text="Cerca:")
	media = Label(root, text="Media:")
	lejos = Label(root, text="Lejos:")
	minp = Label(root, text="MinPuntos:")
	maxp = Label(root, text="MaxPuntos:")
	umbrald = Label(root, text="UmbralDistancia:")
	cambiar = Button(root, command=change ,text="Cambiar")

	varit = Entry(root, width=5)
	varit.insert(0,params.it)
	varcer = Entry(root, width=5)
	varcer.insert(0,params.cer)
	varmed = Entry(root, width=5)
	varmed.insert(0,params.med)
	varlej = Entry(root, width=5)
	varlej.insert(0,params.lej)
	varmin = Entry(root, width=5)
	varmin.insert(0,params.minp)
	varmax = Entry(root, width=5)
	varmax.insert(0,params.maxp)
	varud = Entry(root, width=5)
	varud.insert(0, params.ud)

	ficheros = Label(root, text="Ficheros para la captura")
	lista = Listbox(root, width=35, height=12)
	ficheros_nombre = []
	tipo_humano = ["enPie", "sentado"]
	tipo_cilindro = ["cilindroMenor", "cilindroMayor"]
	distancia = ["Cerca", "Media", "Lejos"]

	cont = 1
	for i in tipo_humano:
		for j in distancia:
			f = "positivo" + str(cont) + "/" + i + j + ".json"
			ficheros_nombre.append(f)
			cont += 1

	cont = 1
	for i in tipo_cilindro:
		for j in distancia:
			f = "negativo" + str(cont) + "/" + i + j + ".json"
			ficheros_nombre.append(f)
			cont += 1


	for fichero in ficheros_nombre:
		lista.insert(tkinter.END ,fichero)

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

	parametros_etiq.grid(row=1, column=1)
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
