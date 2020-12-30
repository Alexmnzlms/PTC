'''
Archivo: clasificarSVM.py
Autor: Alejandro Manzanares Lemus

'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import GridSearchCV
import pickle

# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)
simplefilter(action='ignore', category=DeprecationWarning)

def clasificarSVM():
	print("Ejecutando clasificarSVM...")

	# Assign colum names to the dataset
	colnames = ['perimetro', 'profundidad', 'anchura', 'clase']

	# cargamos los datos
	# Read dataset to pandas dataframe
	piernasdata = pd.read_csv("piernasDataset.csv", names=colnames)

	# Separamos las características de la etiqueta que nos dices a la clase que corresponde
	X = piernasdata.drop('clase', axis=1)
	y = piernasdata['clase']

	'''
	Dividimos en conjunto de entrenamiento y de prueba de forma aleatoria
	con random_state fijamos la semmilla del generador aleatorio para que no
	vayan cambiando los resultados entre una ejecución y otra
	'''

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=25)

	''' Veamos la diferencia entre usar un kernel lineal, polinómico o radial
	ir a
	https://medium.com/all-things-ai/in-depth-parameter-tuning-for-svc-758215394769
	'''
###############################################################################
	print("------------------------------------------------------------------")
	'''
	KERNEL LINEAL
	'''
	print("Clasificación con kernek Lineal")

	svcLineal = SVC(kernel='linear')
	svcLineal.fit(X_train, y_train)

	# Con el clasificador obtenido hacemos la predicción sobre el conjunto de test incial

	y_pred = svcLineal.predict(X_test)

	acc_test=accuracy_score(y_test, y_pred)

	print("Acc_test Lineal: (TP+TN)/(T+P)  %0.4f" % acc_test)

	print("Matriz de confusión Filas: verdad Columnas: predicción")
	'''
	 Cij observaciones que son de clase i pero que se predicen a la clase j.
	 La suma por filas son los ejemplos reales que hay de cada clase=soporte.
	( TN	FP
	  FN	TP )
	'''

	print(confusion_matrix(y_test, y_pred))

	'''
	La precisión mide la capacidad del clasificador en no etiquetar como positivo un ejemplo que es negativo.
	El recall mide la capacidad del clasificador para encontrar todos los ejemplos positivos.
	'''

	print("Precision= TP / (TP + FP), Recall= TP / (TP + FN)")
	print("f1-score es la media entre precisión y recall")
	print(classification_report(y_test, y_pred))

	#Para asegurarnos de que el resultado no depende del conjunto de test elegido
	#tenemos que realizar validación cruzada

	svcLineal2 = SVC(kernel='linear')

	scores = cross_val_score(svcLineal2, X, y, cv=5)

	# exactitud media con intervalo de confianza del 95%
	print("Accuracy 5-cross validation: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))
	print("------------------------------------------------------------------")
###############################################################################
	print("------------------------------------------------------------------")
	'''
	KERNEL POLINOMICO
	'''
	grado=3

	print("Clasificación con kernek polinomico de grado ", grado)

	svcPol = SVC(kernel='poly', degree=grado)
	svcPol.fit(X_train, y_train)


	# Con el clasificador obtenido hacemos la predicción sobre el conjunto de test incial

	y_pred = svcPol.predict(X_test)

	acc_test=accuracy_score(y_test, y_pred)

	print("Acc_test Polinomico: (TP+TN)/(T+P)  %0.4f" % acc_test)

	print("Matriz de confusión Filas: verdad Columnas: predicción")
	'''
	 Cij observaciones que son de clase i pero que se predicen a la clase j.
	 La suma por filas son los ejemplos reales que hay de cada clase=soporte.
	( TN	FP
	  FN	TP )
	'''

	print(confusion_matrix(y_test, y_pred))

	'''
	La precisión mide la capacidad del clasificador en no etiquetar como positivo un ejemplo que es negativo.
	El recall mide la capacidad del clasificador para encontrar todos los ejemplos positivos.
	'''

	print("Precision= TP / (TP + FP), Recall= TP / (TP + FN)")
	print("f1-score es la media entre precisión y recall")
	print(classification_report(y_test, y_pred))

	#Para asegurarnos de que el resultado no depende del conjunto de test elegido
	#tenemos que realizar validación cruzada

	svcPol2 = SVC(kernel='poly', degree=grado)

	scores = cross_val_score(svcPol2, X, y, cv=5)

	# exactitud media con intervalo de confianza del 95%
	print("Accuracy 5-cross validation: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))
	print("------------------------------------------------------------------")
###############################################################################
	print("------------------------------------------------------------------")
	'''
	KERNEL RADIAL

	Parámetros

	C: por defecto vale 1.0. Penaliza el error de clasificación de los ejemplos,
	   a mayor valor más se ajusta al conjunto de ejemplos.
	gamma: por defecto auto = 1/ num_características
	    inversa del tamaño del "radio" del kernel. Una valor grande genera muchos
	    conjuntos de radios pequeños
	'''
	print("Clasificación con kernek de base radial con C=1 y gamma=auto")

	svcRBF = SVC(kernel='rbf', gamma='auto')
	svcRBF.fit(X_train, y_train)


	# Con el clasificador obtenido hacemos la predicción sobre el conjunto de test incial

	y_pred = svcRBF.predict(X_test)

	acc_test=accuracy_score(y_test, y_pred)

	print("Acc_test RBF: (TP+TN)/(T+P)  %0.4f" % acc_test)

	print("Matriz de confusión Filas: verdad Columnas: predicción")
	'''
	 Cij observaciones que son de clase i pero que se predicen a la clase j.
	 La suma por filas son los ejemplos reales que hay de cada clase=soporte.
	( TN	FP
	  FN	TP )
	'''

	print(confusion_matrix(y_test, y_pred))

	'''
	La precisión mide la capacidad del clasificador en no etiquetar como positivo un ejemplo que es negativo.
	El recall mide la capacidad del clasificador para encontrar todos los ejemplos positivos.
	'''

	print("Precision= TP / (TP + FP), Recall= TP / (TP + FN)")
	print("f1-score es la media entre precisión y recall")
	print(classification_report(y_test, y_pred))

	#Para asegurarnos de que el resultado no depende del conjunto de test elegido
	#tenemos que realizar validación cruzada

	svcRBF2 = SVC(kernel='rbf', gamma='auto')

	scores = cross_val_score(svcRBF2, X, y, cv=5)

	# exactitud media con intervalo de confianza del 95%
	print("Accuracy 5-cross validation: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))
	print("------------------------------------------------------------------")
###############################################################################
	print("------------------------------------------------------------------")
	#utilizamos un Kernel Gausiano de base radial
	#busqueda de parámetros
	print("Búsqueda de parámetros en un rango en el caso de RBF")


	param_grid={'C':[1,10,100,1000],
	            'gamma': [0.001, 0.005, 0.01, 0.1]}

	clf=GridSearchCV(SVC(kernel='rbf', class_weight="balanced"), param_grid)

	clf=clf.fit(X_train, y_train)
	print("Mejor estimador encontrado")

	print(clf.best_estimator_)

	mejorSVC=clf.best_estimator_

	# Con el clasificador obtenido hacemos la predicción sobre el conjunto de test incial

	y_pred=mejorSVC.predict(X_test)


	acc_test=accuracy_score(y_test, y_pred)


	print("Acc_test_best: (TP+TN)/(T+P)  %0.4f" % acc_test)


	print("Matriz de confusión Filas: verdad Columnas: predicción")
	'''
	 Cij observacions que son de clase i pero que se predicen a la clase j.
	 La suma por filas son los ejemplos reales que hay de cada clase=soporte.
	( TN	FP
	  FN	TP )
	'''

	print(confusion_matrix(y_test, y_pred))

	'''
	La precisión mide la capacidad del clasificador en no etiquetar como positivo un ejemplo que es negativo.
	El recall mide la capacidad del clasificador para encontrar todos los ejemplos positivos.
	'''

	print("Precision= TP / (TP + FP), Recall= TP / (TP + FN)")
	print("f1-score es la media entre precisión y recall")
	print(classification_report(y_test, y_pred))



	#realizando validación cruzada 5-cross validation, si hay 150 muestras
	#entonces está usandos 30 muestras de ejemplo cada vez y eso lo realiza 5 veces

	svcRBF2 = SVC(kernel='rbf', C=100, gamma=0.005)

	scores = cross_val_score(svcRBF2, X, y, cv=5)

	# exactitud media con intervalo de confianza del 95%
	print("Accuracy 5-cross validation: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))
	print("------------------------------------------------------------------")
###############################################################################

	print("------------------------------------------------------------------")
	print("Salvamos el mejor clasificador a disco, fichero clasificador.pkl")

	# Guardamos el clasificador
	with open("clasificador.pkl", "wb") as archivo:
		pickle.dump(mejorSVC, archivo)

	print("------------------------------------------------------------------")
