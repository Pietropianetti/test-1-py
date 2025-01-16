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
				print(infoq{)
			
		except FileNotFoundError: 
				info = [ ]
				
		print(info)	
			
		info.append(self.Name ) 
		
		print(info)
		
		with open(self.Lista, "w") as file:
			json.dump(info , file)
	
		print(self.Name)
		print(self.Lista)
		
		
dado("oi","d").add()
