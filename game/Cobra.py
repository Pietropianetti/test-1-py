import time 
import random
import os

def render():
  
  return os.system("cls" if os.name == "nt" else"clear")

def canvas_esqueto(largura, altura) :
    
    return [["□" for _ in range(largura)]  for _ in range(altura)]
    
def canvas_imprecao(canvas):
    for i in canvas:
    	print(" ".join(i))
    	
def bordar(canvas):
  for i in range(len(canvas)):
    for j in range(len(canvas[i])):
      
      # linha topo
      if i == 0 :
          canvas[0][j] = f"■"
      
      # linha esquerda
      if j == 0 :
          canvas[i][j] = f"■"
      
      #linha lado direita
      if j  == len(canvas[i]) - 1:
        canvas[i][j] = f"■"
      
      #linha de baixo
      if i == len(canvas) - 1:
        canvas[i][j] = f"■"

class cobra_corpo():      
  def __init__(self,Canvas,Tipo):
    
    inicializacao = False
    
  self.tipo = Tipo
  self.canvas = Canvas
    
  if inicializacao = False
    lista = []
    inicializacao =True
    
  def cobra(posicaoY,posicaoX) :
      
    def criar(posicaoY,posicaoX,**kwargs):
        
        cordenada = { "tipo": self.tipo "X" : posicaoY , "Y" : posicaoX}
        
        cordenada.update(kwargs)
        return cordenada
      
        lista.append(criar(posicaoY, posicaoX))
    
    
    
    
    canvas[self.posicaoY][self.posicaoX] = "■"

posicaoX = 0
a = 0
while a < 300:
  a += 1
  
  if posicaoX > 19 :
    posicaoX = 1
  else:
    posicaoX += 1
  
  canvas = canvas_esqueto(24,20)
  bordar(canvas)
  cobra_corpo()
  canvas_imprecao(canvas)
  render()

      
    


  
