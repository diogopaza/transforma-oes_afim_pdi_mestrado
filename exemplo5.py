

import cv2
import numpy as np

#Pega as dimensões da imagem e depois determina o centro
image = cv2.imread('jogador.jpg')
angle = 90

( h,w )= image.shape[:2]
( cX, cY) = ( w//2, h//2)

"""
Pega a matriz de rotação( aplicando
o negativo do ângulo para girar no sentido horário), então pega o seno
e cosseno
"""
matrizM = cv2.getRotationMatrix2D( (cX, cY), -angle, 1)
cos = np.abs( matrizM[0,0])
sen = np.abs( matrizM[0,1])
print(cos)

cv2.imshow('input', image)
