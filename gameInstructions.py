import MENU, Main

def text_instructions():

    print(30*'-', 'Instructions', 30*'-')
    print('')
    print('To move left and right press "A" and "D" keys accordingly')
    print("")
    print('To jump press the "Spacebar"')
    print('')
    print('Shoot with "L" key')
    print('')
    print('press (1) to go back to the menu or (2) to play the game')
    print('')
    print(72*'-')
    return
    
def instructions():
    
    loop = True
    
    while loop:

        text_instructions()
        choice = int(input('Enter choice: '))

        if choice==1:
            break

        elif choice==2:
            Main.gamemain()

        else:
            print('')
            int(input('Select a valid option, press (1) to go back or (2) to play the game'))
    return
