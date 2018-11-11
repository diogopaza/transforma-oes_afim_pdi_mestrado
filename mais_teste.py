
import cv2
import numpy as np
import math

image = cv2.imread('jogador.jpg')
angle = 45

( h,w )= image.shape[:2]
( cX, cY) = ( w//2, h//2)
th = math.pi/4

image[0][0] = [[np.cos(th),np.sin(th),0], [np.sin(th),np.cos(th),0], [0,0,1]] 
print( image[0][0] )
