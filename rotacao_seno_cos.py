import math
import numpy as np
import cv2

angulo=45
img = cv2.imread("jogador.jpg")
#cv2.imshow("original", img)

#pega altura e largura da imagem
h,w= img.shape[:2]

#define o novo tamanho da imagem apartir do angulo
novo_tamanho = (int(abs(w * math.cos(angulo % 180)) + abs(h * math.sin(angulo % 180))),int(abs(w * math.sin(angulo % 180)) + abs(h * math.cos(angulo % 180))))

#define o centro como ponto de rotação
ponto_rotacao = (w / 2, h / 2)


cos,seno = math.cos(angulo), math.sin(angulo)

#rotacionando matriz(imagem)
rotacionar_matriz = np.matrix([
    [cos,seno,(1-cos) * ponto_rotacao[0] - seno * ponto_rotacao[1]],
    [-1 * seno,cos,seno * ponto_rotacao[0] + (1 - cos) * ponto_rotacao[1]],
    [0,0,1]
  ])


x,y = (novo_tamanho[0] - w) / 2, (novo_tamanho[1] - h) / 2

#aplicando transformação geometrica
matriz_final = np.matrix([
    [1, 0, x],
    [0, 1, y],
    [0, 0, 1]
  ])


#multiplicando a matriz transformada com a matriz rotacionada
matriz = (matriz_final * rotacionar_matriz)[:2]

img_rotacionada = cv2.warpAffine(img, matriz, novo_tamanho)
cv2.imshow("imagem_rotacionada", img_rotacionada)
