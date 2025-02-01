import time 
import random
import os
import keyboard
import sys
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
    global comida
    comida = []
    
  def objeto(self,posicaoX,posicaoY) :   
        
    cordenada = dict({ "tipo": self.tipo , "X" : posicaoX, "Y" : posicaoY})

    if self.tipo == "cobra":
      lista.append(cordenada)

    if self.tipo == "comida" :
       comida.append(cordenada)
       
  def printe(self):

    for i in comida :
      self.canvas[i.get("Y")][i.get("X")] = "◇"

    for i in lista :
        self.canvas [i.get("Y")][i.get("X")] = "■"

class MOVE():

  def cima():
    lista [0]["Y"] -= 1
    
    if lista [0]["Y"] == 0:
      sys.exit()
    
  def baixo():
    lista [0]["Y"] += 1
    
    if lista[0]["Y"] == len(canvas):
      sys.exit()
    
  def esquerdo():
    lista[0]["X"] -= 1
    
  def direito():
    lista[0]["X"] += 1
    
A = 0
while True:

  A += 1

  canvas = canvas_esqueto(24,20)
  bordar(canvas)
  
  if A == 1:
    OBJETOS(canvas,"cobra").objeto(8,9)
    OBJETOS(canvas,"comida").objeto(4,9)
  
  OBJETOS(canvas,"cobra").printe()
  OBJETOS(canvas,"comida").printe()
  
  #key = keyboard.read_event()
  
  #if key.name == "w":
    #MOVE.cima()
  #if key.name == "s":
    #MOVE.baixo()
  #if key.name == "a":
    #MOVE.esquerdo()
  #if key.name == "d":
    #MOVE.direito()
    
  
  
  
  MOVE.baixo()
  
  canvas_imprecao(canvas)
  print(A)
  time.sleep(0.1)
  render()
  

      
    


  
