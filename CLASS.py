import json 
import sys


class dado:
	def  __init__ (self, Lista):
		self.Lista = Lista
	
	def add(self, name):	
	
		lista = self.Lista
		
		with open(lista, "w") as file:
			json.dump(name , file)
			

class remove():
    print("remove")