import numpy as np
import cv2

imagem = cv2.imread("jogador.jpg")
altura, largura = imagem.shape[:2]
ponto_de_rotacao = ( largura/2, altura/2) #define o centro da figura 
rotacao = cv2.getRotationMatrix2D(ponto_de_rotacao, 45, 0.5 )
rotacionando = cv2.warpAffine( imagem, rotacao, (largura, altura))
cv2.imshow("Rotacionando 45 graus", rotacionando)

rotacao = cv2.getRotationMatrix2D(ponto_de_rotacao, 120, 0.5 )
rotacionando = cv2.warpAffine( imagem, rotacao, (largura, altura))
cv2.imshow("Rotacionando 120 graus", rotacionando)

cv2.waitKey(0)
cv2.destroyAllWindows()
