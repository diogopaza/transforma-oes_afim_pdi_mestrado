"""
import cv2

imagem = cv2.imread("jogador.jpg")
altura, largura = imagem.shape[:2]
print(altura)
print(largura)
ponto_inicial = cv2.getRotationMatrix2D((largura,altura), 30, 1)
                    
imagem_rotacionada =  cv2.warpAffine(imagem, ponto_inicial, (largura, altura))

cv2.imshow("imagem rotacionada", imagem_rotacionada)

#cv2.imshow("janela", imagem)
"""
import cv2
import numpy as np

imagem = cv2.imread("jogador.jpg")
altura, largura = imagem.shape[:2]
ponto_medio = ( largura/2, altura/2)
rotacao = cv2.getRotationMatrix2D( ponto_medio, 60, 1)


imagem_rotacionada = cv2.warpAffine( imagem, rotacao, (largura,altura))
cv2.circle( imagem, (0,largura), 10, (0,0,255), -1 )
cv2.imshow("normal", imagem)
cv2.imshow("janela", imagem_rotacionada)
