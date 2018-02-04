import pygame, sys , random ,MENU
import classes, display_text
from respawn import process
from time import sleep

def gamemain():
    
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init() ## initialising the library
    pygame.mixer.init()

    ##audio

    ##screen
    WIDTH,HEIGHT = 1900 ,900
    screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32) ## takes four arguments, screen size, flags, colour
    clock = pygame.time.Clock()
    FPS = 30
    totalframes =0
    seconds = FPS*5
    background = pygame.image.load("imagesgame/backgroundday.png")

    ##character
    protagonist= classes.classprotagonist(900 ,HEIGHT-150, 150 ,150, "imagesgame/protagonist_noback.png")   ##starting position, dimension

    ##text

        
    while True:
        
            ##PROCESS
            
        process(protagonist,FPS,totalframes,WIDTH,screen,background)    ## calling function that contains key assignments (mistake called it respawn)
            
            
            ##LOGIC
        classes.classprotagonist.motion(protagonist,WIDTH, HEIGHT)
        classes.classshuriken.movement()
        classes.classenemy.update_all(WIDTH,HEIGHT)
            
            
        totalframes += 1

        ##Draw       
        screen.blit(background, (0,0) )             ## arg = what to display and where does it start from. so upper left
        display_text.counter_string(screen)
        
        display_text.display_lost(screen,background)
                                    
        classes.BaseClass.allsprites.draw(screen)               ##two different baseclass so drawing them individually
        classes.classshuriken.List.draw(screen)
            
            
            
        pygame.display.flip() ## if left alone it will not close screen properly
            
            
        clock.tick (FPS)
            
    return


