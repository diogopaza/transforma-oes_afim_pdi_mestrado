"""import cv2
import numpy as np

imagem = cv2.imread("grid.jpg")

cv2.circle( imagem, (83,90), 10, (0,0,255), -1 )

cv2.imshow("minhaImagem", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

import cv2
import numpy as np

imagem = cv2.imread("grid.jpg")

cv2.circle( imagem, (83,90), 10, (0,0,255,), -1)

cv2.imshow("Output", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
