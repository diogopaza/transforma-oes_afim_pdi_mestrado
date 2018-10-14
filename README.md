<h1>Rotacionando uma imagem</h1>
<p>Em latin affinis significa "conectado com" ou que possui conexão. Uma das transformações em geometria que também é 
utilizada em processamento digital de imagem se chama affine.</p>
<p>Rotação é um tipo de transformação affine</p>
<h3>Exemplo: </h3>

import cv2

imagem = cv2.imread("jogador.jpg")
altura, largura = imagem.shape[:2]
cv2.imshow("janela", imagem)