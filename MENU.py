import sys , pygame, gameInstructions
from Main import gamemain


## Text menu in Python

pygame.init()

def menu():
    
    def print_menu():       ## Your menu design here

        print('Hello there!')
        print('')
        print('What would you like to do')
        print('')
        print (30 * "-" , "MENU" , 30 * "-")
        print ("1. Play game")
        print ("")
        print ("2. Instructions")
        print ("")      
        print ("3. Exit")
        print (67 * "-")
      
    loop=True      
      
    while loop:         ## While loop which will keep going until loop = False
        print_menu()    ## Displays menu
        choice = int(input("Enter your choice [1-3]: "))
         
        if choice==1:          
            print ("Have a good time!")
            gamemain()
            break
        
        elif choice==2:
            gameInstructions.instructions()
            
        elif choice==3:
            print ("I'm sorry to see you leave :( ")
  
            loop= False
            break
         
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print('')
            int(input("Wrong option selection. Enter any key to try again.."))

menu()
