<h1>Rotacionando uma imagem</h1>
<p>Em latin affinis significa "conectado com" ou que possui conexão. Uma das transformações em geometria que também é 
utilizada em processamento digital de imagem se chama affine.</p>
<p>Rotação é um tipo de transformação affine</p>
<h3>Exemplo rotação de imagem  </h3>

import cv2

imagem = cv2.imread("jogador.jpg")
altura, largura = imagem.shape[:2]
ponto_inicial = cv2.getRotationMatrix2D( (largura, altura), 45,0.5)

imagem_rotacionada = cv2.warpAffine( imagem, ponto_inicial, (largura,altura))
 
cv2.imshow("janela", imagem_rotacionada)

<h3>Exemplo3 rotação de imagem</h3>

import cv2<br>
import numpy as np<br>

imagem = cv2.imread("grid.jpg")<br>

cv2.circle( imagem, (83,90), 10, (0,0,255), -1) na sequencia os paramentros passados são a imagem onde o círculo será desenhado,
o local onde o círculo deve ficar na imagem, o terceiro parametro é a espessura do círculo e por fim a cor do círculo.


cv2.imshow("Output", imagem)<br>
cv2.waitKey(0)<br>
cv2.destroyAllWindows()<br>




<h2>Translação(deslocamento)</h2>
<p></p>
