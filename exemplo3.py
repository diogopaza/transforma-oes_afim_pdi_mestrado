import numpy as np
import cv2

imagem = cv2.imread("teste.png")
altura, largura = imagem.shape[:2]
cv2.imshow("Input", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
