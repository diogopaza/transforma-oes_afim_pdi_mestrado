import cv2
from numpy import *
import math



imagem = cv2.imread('jogador.jpg')
"""
x1 = 80
y1 = 10
    
T= [[1,0,y1], [0,1,x1], [0,0,1]]

m,n = imagem.shape[:2];
x, y = indices((m,n));
    
PtosHomogenio = array([ x.ravel(), y.ravel(), ones(m*n) ])
PtosHomogenioLinha = dot(linalg.inv(T), PtosHomogenio)
    
xlinha = PtosHomogenioLinha[0].round(0).astype(int)
ylinha = PtosHomogenioLinha[1].round(0).astype(int)
    
Xnovo = maximum(0, minimum(m-1, xlinha)).reshape(m,n)
Ynovo = maximum(0, minimum(n-1, ylinha)).reshape(m,n)
C = imagem[Xnovo,Ynovo]
cv2.imshow("img", C)
"""





#rotação

th=math.pi/4
TrotacaoX  = [[cos(th),-sin(th),0], [sin(th),cos(th),0], [0,0,1]]

h,w = imagem.shape[:2]

x, y = indices((h,w))
PtosHomogenio = array([ x.ravel(), y.ravel(), ones(h*w) ])
PtosHomogenioLinha = dot(linalg.inv(TrotacaoX), PtosHomogenio)
    
xlinha = PtosHomogenioLinha[0].round(0).astype(int)
ylinha = PtosHomogenioLinha[1].round(0).astype(int)

Xnovo = maximum(0, minimum(h-1, xlinha)).reshape(h,w)
Ynovo = maximum(0, minimum(w-1, ylinha)).reshape(h,w)
TrotacaoX = imagem[Xnovo,Ynovo]       
Final = imagem[Xnovo,Ynovo]
cv2.imshow('Imagem Rotacionada', Final)

"""

#escala
x2 = 0.5
y2 = 0.5
Tescala   = [[y2,0,0], [0,x2,0], [0,0,1]]

m,n = imagem.shape[:2];
x, y = indices((m,n));
    
PtosHomogenio = array([ x.ravel(), y.ravel(), ones(m*n) ])
PtosHomogenioLinha = dot(linalg.inv(Tescala), PtosHomogenio)
    
xlinha = PtosHomogenioLinha[0].round(0).astype(int)
ylinha = PtosHomogenioLinha[1].round(0).astype(int)
    
Xnovo = maximum(0, minimum(m-1, xlinha)).reshape(m,n)
Ynovo = maximum(0, minimum(n-1, ylinha)).reshape(m,n)
F = imagem[Xnovo,Ynovo]
cv2.imshow("img escala", F)
"""



