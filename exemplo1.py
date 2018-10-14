import cv2

imagem = cv2.imread("jogador.jpg")
altura, largura = imagem.shape[:2]
print(altura)
print(largura)
ponto_inicial = cv2.getRotationMatrix2D((0,0), 30, 1)
                    
imagem_rotacionada =  cv2.warpAffine(imagem, ponto_inicial, (largura, altura))

cv2.imshow("imagem rotacionada", imagem_rotacionada)

#cv2.imshow("janela", imagem)