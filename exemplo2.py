"""import cv2
import numpy as np

imagem = cv2.imread("grid.jpg")

cv2.circle( imagem, (83,90), 10, (0,0,255), -1 )

cv2.imshow("minhaImagem", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""
import cv2
import numpy as np

imagem = cv2.imread("grid.jpg")
altura, largura = imagem.shape[:2]

cv2.circle( imagem, (83,90), 10, (0,0,255,), -1)
cv2.circle( imagem, (447,90), 10, (0,0,255,), -1)
cv2.circle( imagem, (83,468), 10, (0,0,255,), -1)

ponto1= np.float32( [ [83,90], [447,90], [83,472]])
ponto2=  np.float32( [ [0,0], [447,90], [150,472]])

matriz = cv2.getAffineTransform(ponto1, ponto2)
imagem_transformacao_afim = cv2.warpAffine( imagem, matriz, (largura, altura) )

cv2.imshow("Output", imagem)
cv2.imshow( "Affine Transformation", imagem_transformacao_afim)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
import cv2
import numpy as np

imagem = cv2.imread("grid.jpg")
altura, largura = imagem.shape[:2]
cv2.circle( imagem, (83,90), 10, (0,0,255), -1)
cv2.circle( imagem, (447,90), 10, (0,0,255), -1)
cv2.circle( imagem, (83,468), 10, (0,0,255), -1)

ponto1 = np.float32( [ [83,90],[447,90],[83,472]])
ponto2 = np.float32( [ [0,0],[447,90],[150,472]])

matriz = cv2.getAffineTransform( ponto1, ponto2)
imagem_transformacao_afim= cv2.warpAffine( imagem, matriz, (largura, altura))

cv2.imshow("Input", imagem)
cv2.imshow("Output", imagem_transformacao_afim)
cv2.waitKey(0)
cv2.destroyAllWindows()
