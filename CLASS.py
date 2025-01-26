import sys
import json
import os
import time

class dado:
    def  __init__ (self, Lista , Name= None):
        self.Lista = f"{Lista}.json"
        self.Name = Name
        
    def add(self):

        name_l = self.Name.rsplit(",")

        try:
            with open(self.Lista, "r") as file:
                
                info = json.load(file)
            
        except FileNotFoundError: 
        
                info = [ ]
            
        for name in name_l:
            
            info.append(name)
            
        with open(self.Lista, "w") as file:
            
            json.dump(info , file)

    def re(self):
        try:
            with open(self.Lista, "r") as file:
                
                info = json.load(file)
            
        except FileNotFoundError: 
        
                print("Don't exist")
                
        info.remove(self.Name)

        with open(self.Lista, "w") as file:
            
            json.dump(info , file)
    
    def ver (self):
        with open(self.Lista, "r") as file:
             
             return json.load(file)
             
class apagar ():
  
  def __init__ (self) :
    
    def animar (sleep) :
      
      time.sleep(sleep)
      
      os.system("cls" if os.name == "nt" else "clear")
      
    def repido (self):
      
      os.system("cls" if os.name == "nt" else "clear")