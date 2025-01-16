import json 
import sys


class dado:
	def  __init__ (self, Lista , Name):
		self.Lista = f"{Lista}.json"
		self.Name = Name
	
	def add(self):

		try:
			with open(self.Lista, "r") as file:
				
				info = json.load(file)
			
		except FileNotFoundError: 
		
				info = [ ]
				
		info.append(self.Name)
		
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
		