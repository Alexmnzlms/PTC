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
		return 'Bill'
	elif tipo == 1:
		return 'Bill#0'
	elif tipo == 2:
		return 'Cylinder'
	elif tipo == 3:
		return 'Cylinder0'

def capturar(clientID, file, params):
	print("Ejecutando capturar...")

	print(file)
	params.show()

	escena_base = os.getcwd() + "/escenaTest.ttt"
	print(escena_base)

	vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot_wait)
	print("Simulación terminada")

	#vrep.simxCloseScene(clientID, vrep.simx_opmode_oneshot_wait)
	#print("Escena cerrada")

	vrep.simxLoadScene(clientID, escena_base, 0xFF, vrep.simx_opmode_oneshot_wait)
	print("Escena",escena_base,"cargada")

	#vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)
	#print("Simulación comenzada")

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

	seguir=True
	while(iteracion<=maxIter and seguir):

		#Situamos donde queremos a la persona sentada, unidades en metros
		returnCode = vrep.simxSetObjectPosition(clientID,objecthandle,-1,[1+2.0*iteracion/10,-0.4,0.0],vrep.simx_opmode_oneshot)
		#Cambiamos la orientacion, ojo está en radianes: Para pasar de grados a radianes hay que multiplicar por PI y dividir por 180
		returnCode = vrep.simxSetObjectOrientation(clientID, objecthandle, -1, [0.0,0.0,3.05-(0.20)*iteracion], vrep.simx_opmode_oneshot)

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

		#Convertir img a hsv y detectar colores
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		verde_bajos = np.array([49,50,50], dtype=np.uint8)
		verde_altos = np.array([80, 255, 255], dtype=np.uint8)
		mask = cv2.inRange(hsv, verde_bajos, verde_altos) #Crear mascara

		#Limpiar mascara y buscar centro del objeto verde
		moments = cv2.moments(mask)
		area = moments['m00']
		if(area > 200):
			x = int(moments['m10']/moments['m00'])
			y = int(moments['m01']/moments['m00'])
			cv2.rectangle(img, (x, y), (x+2, y+2),(0,0,255), 2)
			#Descomentar para printear la posicion del centro
			#print(x,y)

			#Si el centro del objeto esta en la parte central de la pantalla (aprox.), detener motores
			if abs(x-256/2) < 15:
				vrep.simxSetJointTargetVelocity(clientID, left_motor_handle,0,vrep.simx_opmode_streaming)
				vrep.simxSetJointTargetVelocity(clientID, right_motor_handle,0,vrep.simx_opmode_streaming)

			#Si no, girar los motores hacia la derecha o la izquierda
			elif x > 256/2:
				vrep.simxSetJointTargetVelocity(clientID, left_motor_handle,velocidad,vrep.simx_opmode_streaming)
				vrep.simxSetJointTargetVelocity(clientID, right_motor_handle,-velocidad,vrep.simx_opmode_streaming)
			elif x < 256/2:
				vrep.simxSetJointTargetVelocity(clientID, left_motor_handle,-velocidad,vrep.simx_opmode_streaming)
				vrep.simxSetJointTargetVelocity(clientID, right_motor_handle,velocidad,vrep.simx_opmode_streaming)

		#Mostrar frame y salir con "ESC"
		cv2.imshow('Image', img)
		cv2.imshow('Mask', mask)

		tecla = cv2.waitKey(5) & 0xFF
		if tecla == 27:
			seguir=False

		iteracion=iteracion+1

	os.chdir(dir_p2)

