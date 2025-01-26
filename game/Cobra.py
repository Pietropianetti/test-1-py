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

class OBJETOS():   

  inicializacao = False

  def __init__(self,Canvas,Tipo):
    
    self.tipo = Tipo
    self.canvas = Canvas
    
  if inicializacao == False :
    
    global lista
    lista = []
    inicializacao = True
    
  def objeto(self,posicaoY,posicaoX) :   
        
    cordenada = dict({ "tipo": self.tipo , "X" : posicaoY , "Y" : posicaoX})

    lista.append(cordenada)

    for i in lista :
      self.canvas [i.get("Y")][i.get("X")] = "■"

a = 0    
while a < 300:
  a += 1
  
  canvas = canvas_esqueto(24,20)
  bordar(canvas)
  OBJETOS(canvas,"cobra").objeto(8,9)
  canvas_imprecao(canvas)
  print(OBJETOS)
  render()

      
    


  
