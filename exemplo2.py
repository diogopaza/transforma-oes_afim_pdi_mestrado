import cv2
import numpy as np

imagem = cv2.imread("grid.jpg")

cv2.imshow("minhaImagem", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
