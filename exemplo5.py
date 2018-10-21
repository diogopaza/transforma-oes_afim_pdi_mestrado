

import cv2


image = cv2.imread('jogador.jpg')
( h,w )= image.shape[:2]

cv2.imshow('input', image)
