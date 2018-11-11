import cv2
import numpy as np

"""
a = [ [1,2], [3,4]]
a = np.array(a)
print (3*a)


#a = np.array( [ 1,2,3,4])

#print(2*a)
image = cv2.imread('jogador.jpg')
#image[0:10] = 0,0,0
print( image[2] )
#cv2.imshow("sadf", image)

cx= np.array( [ [35,26,28], [11,2,4], [11,1,4] ])
cTeste = np.array( [ [1,0,0],[0,1,0],[0,0,1]])
#cosseno = np.cos( )
#print( cTeste *  )
"""

image = cv2.imread('jogador.jpg')

( h,w )= image.shape[:2]
( cX, cY) = ( w//2, h//2)
#print (image.shape[0])

#img_np = np.array( image )
#matrizM = cv2.getRotationMatrix2D( (cX, cY), 90, 0.5)
#print( matrizM )


pos0 = 0:10 * np.cos(90) - 0:10 * np.sin(90)
print( w )
cv2.imshow("sadf", image)
#image[0: image.shape[0]]=0,0,0
#cv2.imshow("teste", image)
