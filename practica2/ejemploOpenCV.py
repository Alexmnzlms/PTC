#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:05:10 2018

@author: eaguirre
"""

import cv2

# cargar el archivo jpgindicado
img = cv2.imread('leon.jpg', cv2.IMREAD_COLOR)

# mostrar la imagen en una ventana
cv2.imshow('Imagen del Leon', img)

# esperar hasta que se presiona una tecla
cv2.waitKey(0)

# cierra las ventanas
cv2.destroyAllWindows()

