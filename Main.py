smport sys
import CLASS

class main:
        
    def __init__(self):

        acao = input("\n You would like to add or remove : ").upper()
              
        if acao == "ADD" :

            list_Modify =  input("\n Which list do you want to modify/add : ").upper()
            name_add = input("\n what do you want to add(don't foget the coma) : ").upper()
            
            CLASS.dado(list_Modify, name_add).add()

            print(CLASS.dado(list_Modify).ver())
        if acao == "REMOVE" :
          print(5)

print("Welcome") 
CLASS.apagar()
print("Let's star")
print("Do you want to add/remove something on the liste")
    
user = input("S for Yes and N to Nope : ").upper()

if user == "S":
    
    main()
