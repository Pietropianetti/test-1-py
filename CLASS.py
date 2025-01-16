import sys
import json

class dado:
	def  __init__ (self, Lista , Name):
		self.Lista = f"{Lista}.json"
		self.Name = Name.rsplit(" , ")
		
	def add(self):

		try:
			with open(self.Lista, "r") as file:
				
				info = json.load(file)
			
		except FileNotFoundError: 
		
				info = [ ]
			
		for name in self.Name:
			
			info.append(name)
			
		with open(self.Lista, "w") as file:
			
			json.dump(info , file)

	def remove(self):

		try:
			with open(self.Lista, "r") as file:
				
				info = json.load(file)
			
		except FileNotFoundError: 
		
				Print("Don't exist")
				
		info.remove(self.name)
		with open(self.Lista, "w") as file:
			
			json.dump(info , file)
		