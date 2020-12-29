import parametros
import vrep
import sys
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
import json
import os

def check_file(file):
	tipo = ["enPie", "sentado", "cilindroMenor", "cilindroMayor"]
	distancia = ["Cerca", "Media", "Lejos"]

	for t in range(len(tipo)):
		if file.find(tipo[t]) != -1:
			tipo_encontrado = t

	for d in range(len(distancia)):
		if file.find(distancia[d]) != -1:
			dist_encontrada = d

	return tipo_encontrado, dist_encontrada

def chek_tipo(tipo):
	if tipo == 0:
		return 'Bill#2'
	elif tipo == 1:
		return 'Bill'
	elif tipo == 2:
		return 'Cylinder1'
	elif tipo == 3:
		return 'Cylinder0'

def check_dist(dist, params):
	if dist == 0:
		return params.cer, params.med
	elif dist == 1:
		return params.med, params.lej
	elif dist == 2:
		return params.lej, params.lej+1

def capturar(clientID, file, params):
	print("Ejecutando capturar...")

	print(file)
	params.show()

	_, robothandle = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx', vrep.simx_opmode_oneshot_wait)

	#Guardar la referencia de los motores
	_, left_motor_handle=vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', vrep.simx_opmode_oneshot_wait)
	_, right_motor_handle=vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', vrep.simx_opmode_oneshot_wait)

	#Guardar la referencia de la camara
	_, camhandle = vrep.simxGetObjectHandle(clientID, 'Vision_sensor', vrep.simx_opmode_oneshot_wait)

	#acceder a los datos del laser
	_, datosLaserComp = vrep.simxGetStringSignal(clientID,'LaserData',vrep.simx_opmode_streaming)

	velocidad = 0 #Variable para la velocidad de los motores, dejamos fijo el robot

	tipo, dist = check_file(file)
	objeto = chek_tipo(tipo)
	dist_min, dist_max = check_dist(dist, params)

	# obtenermos la referencia al objeto para moverlo
	_, objecthandle = vrep.simxGetObjectHandle(clientID, objeto, vrep.simx_opmode_oneshot_wait)

	#Iniciar la camara y esperar un segundo para llenar el buffer
	_, resolution, image = vrep.simxGetVisionSensorImage(clientID, camhandle, 0, vrep.simx_opmode_streaming)
	time.sleep(1)

	plt.axis('equal')
	plt.axis([0, 4, -2, 2])

	# mostramos el directorio de trabajo y vemos si existe el dir para salvar los datos
	dir_p2 = os.getcwd()
	print("Directorio de trabajo es: ", os.getcwd())

	direc = file.split("/")[0]

	if not os.path.isdir(direc):
		sys.exit("Error: no existe el directorio "+ direc)

	os.chdir(direc)
	print("Cambiando el directorio de trabajo: ", os.getcwd())

	segundos=5
	maxIter=params.it
	iteracion=1

	jsonfile = file.split("/")[1]

	cabecera={"TiempoSleep":segundos, "MaxIteraciones":maxIter}
	ficheroLaser=open(jsonfile, "w")
	ficheroLaser.write(json.dumps(cabecera)+'\n')

	returnCode = vrep.simxSetObjectPosition(clientID,objecthandle,-1,[dist_min,0.0,0.0],vrep.simx_opmode_oneshot)
	returnCode = vrep.simxSetObjectOrientation(clientID, objecthandle, -1, [0.0,0.0,0.0], vrep.simx_opmode_oneshot)

	print(dist_min,dist_max)

	seguir=True
	while(iteracion<=maxIter and seguir):

		#print("Rotación:", [0.0,0.0,3.05-(0.20)*iteracion])
		#Cambiamos la orientacion, ojo está en radianes: Para pasar de grados a radianes hay que multiplicar por PI y dividir por 180
		returnCode = vrep.simxSetObjectOrientation(clientID, objecthandle, -1, [0.0,0.0,3.05-(0.20)*iteracion], vrep.simx_opmode_oneshot)

		#print("Posición:", [dist_min+dist_max*iteracion/maxIter,0.0,0.0])
		#Situamos donde queremos a la persona sentada, unidades en metros
		returnCode = vrep.simxSetObjectPosition(clientID,objecthandle,-1,[dist_min+dist_max*iteracion/maxIter,0.0,0.0],vrep.simx_opmode_oneshot)


		time.sleep(segundos) #esperamos un tiempo para que el ciclo de lectura de datos no sea muy rápido

		puntosx=[] #listas para recibir las coordenadas x, y z de los puntos detectados por el laser
		puntosy=[]
		puntosz=[]
		returnCode, signalValue = vrep.simxGetStringSignal(clientID,'LaserData',vrep.simx_opmode_buffer)

		datosLaser=vrep.simxUnpackFloats(signalValue)
		for indice in range(0,len(datosLaser),3):
			puntosx.append(datosLaser[indice+1])
			puntosy.append(datosLaser[indice+2])
			puntosz.append(datosLaser[indice])

		print("Iteración: ", iteracion)
		plt.clf()
		plt.plot(puntosx, puntosy, 'r.')
		plt.show()

		#Guardamos los puntosx, puntosy en el fichero JSON
		lectura={"Iteracion":iteracion, "PuntosX":puntosx, "PuntosY":puntosy}
		#ficheroLaser.write('{}\n'.format(json.dumps(lectura)))
		ficheroLaser.write(json.dumps(lectura)+'\n')

		#Guardar frame de la camara, rotarlo y convertirlo a BGR
		_, resolution, image=vrep.simxGetVisionSensorImage(clientID, camhandle, 0, vrep.simx_opmode_buffer)
		img = np.array(image, dtype = np.uint8)
		img.resize([resolution[0], resolution[1], 3])
		img = np.rot90(img,2)
		img = np.fliplr(img)
		img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
		if iteracion == 1 or iteracion == maxIter:
			cv2.imwrite('Iteracion'+str(iteracion)+'.jpg', img)

		iteracion=iteracion+1

	finFichero={"Iteraciones totales":iteracion-1}
	#ficheroLaser.write('{}\n'.format(json.dumps(finFichero)))
	ficheroLaser.write(json.dumps(finFichero)+'\n')
	ficheroLaser.close()

	os.chdir(dir_p2)

