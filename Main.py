import sys
import CLASS


class main():

    print("Welcome" "\n" "Let's star" "\n" "Do you want to add something on the liste")
    inicio = input("S for Yes and N to Nope : ").upper()

    while True:

        if inicio == "S" :
          list_Modify =  input("\n" "Wichi list do you want to modify/add : ").upper()
        break

main() 
CLASS.add()
