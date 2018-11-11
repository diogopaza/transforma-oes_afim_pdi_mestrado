import cv2
import numpy as np

image = cv2.imread("jogador.jpg")
(h,w) = image[:2]
( cX, cY) = ( w//2, h//2)

print(cX)

#matrizM = cv2.getRotationMatrix2D( (cX, cY), angle, 1)
#print( matrizM[0,0])

#cv2.imshow('img', image)
