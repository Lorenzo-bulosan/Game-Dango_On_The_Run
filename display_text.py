import pygame , classes , sys ,MENU
from time import sleep

def display_lost(screen,background):

    font = pygame.font.SysFont("comicsansms", 200)
    text = font.render("YOU LOST!!!", True, (255,0,0 ))

    for enemies in classes.classenemy.List:
        protagonistkill = pygame.sprite.spritecollide(enemies, classes.classprotagonist.List, True)

        if len(protagonistkill) > 0:
            for kill in protagonistkill:
                    kill.destroy(classes.classprotagonist)
   
                                                     ##displaying new background with lost message
                    screen.blit(text,(900 - text.get_width() // 2, 450 - text.get_height() // 2))
                    enemies.destroy(classes.classenemy)
                    #MENU.menu()
        
def counter_string(screen):

    counter = 0
    font = pygame.font.SysFont("comicsansms", 30)
     
    for enemies in classes.classenemy.List:
        if enemies.health <=0:

            counter += 10
            text_counter = font.render("Score: " + str(counter) , True, (0, 128, 0))
            screen.blit(text_counter,(150 - text_counter.get_width() // 2, 100 - text_counter.get_height() // 2))
    
