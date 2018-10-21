
import cv2
import numpy as np

image = cv2.imread('jogador.jpg')
altura,largura = image.shape[:2]
ponto_rotacao = largura/2, altura/2
rotacao = cv2.getRotationMatrix2D( ponto_rotacao, 45, 1)
result = cv2.warpAffine( image, rotacao, interpolation=cv2.INTER_LINEAR )

cv2.imshow('jj', result)
