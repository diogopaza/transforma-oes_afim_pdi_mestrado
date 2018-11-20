

import cv2
import numpy as np

#Pega as dimensões da imagem e depois determina o centro
image = cv2.imread('jogador.jpg')
angle = 45

( h,w )= image.shape[:2]
( cX, cY) = ( w//2, h//2)

"""
Pega a matriz de rotação( aplicando
o negativo do ângulo para girar no sentido horário), então pega o seno
e cosseno
"""
matrizM = cv2.getRotationMatrix2D( (cX, cY), angle, 0.5)
cos = np.abs( matrizM[0,0])
sen = np.abs( matrizM[0,1])

#Calcula as novas dimensões limites da imagem
nW = int( (h*sen) + ( w*cos))
nH = int( (h * cos) + ( w * sen) )

#Ajustar a matriz de rotação levando em conta as novas dimensões
matrizM[0,2] += ( nW / 2 ) -cX
matrizM[1,2] += ( nH / 2 ) - cY

#Realizar a rotação real e retornar a imagem
imagem_rotacionada = cv2.warpAffine( image, matrizM, (nW, nH))

cv2.imshow('Imagem Rotacionada', imagem_rotacionada)
