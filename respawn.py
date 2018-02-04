

import pygame,sys, random,classes

pygame.init()

def process(protagonist, FPS, totalframes,WIDTH,screen,background):

    for event in pygame.event.get():    ##loop all posible event in pygame framework
        if event.type == pygame.QUIT:   ## if the types is that the program wants to quit then 
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
                                                ##horizontal movement
    if keys[pygame.K_d]:
        classes.classprotagonist.shurikenright = True           ##when going right shuriken direction is true
        
        protagonist.image = pygame.image.load("imagesgame/protagonist_noback.png")
        protagonist.velx = 15
        
        
    elif keys [ pygame.K_a]:            ##backwards movements and flipped image
        classes.classprotagonist.shurikenright = False          ##when goin left shuriken is not going right

        protagonist.velx = -15
        protagonist.image = pygame.image.load("imagesgame/protagonist_noback_flip.png")
        
    else:
        protagonist.velx = 0
                                                ##Vertical movement
    
    if keys [pygame.K_SPACE]:
        protagonist.jumping = True

    if keys [pygame.K_l]:                       ##shuriken at same starting position that protagonist
        s = classes.classshuriken(protagonist.rect.x, protagonist.rect.y, 150,150, "imagesgame/shuriken_noback.png")

        if classes.classprotagonist.shurikenright:                  ## shukri9ken velocity
            s.velx = 20

        else:
            s.velx = -20
        

    spawn (FPS,totalframes)
    collision(WIDTH,screen,background,FPS,totalframes)

    
def spawn (FPS, totalframes):

    n = 6                           ## n = BE n2 = exodia n3= biomba /// respawn time in seconds
    n2= 8
    n3 = 12
    seconds = FPS * n
    seconds2 = FPS * n2
    seconds3 = FPS * n3
    x = 1900-400

    
    if totalframes % seconds == 0:              ## every n seconds respawn
        r = random.randint (1,2)
        n -= 0.5
        
        if r == 1 :
            x = 1

        classes.classenemy (x ,random.randint(0,900), 400, 244,  "imagesgame/enemy_noback.png")
        
    if totalframes % seconds2 == 0:            
        r = random.randint (1,2)
        n2 -= 0.5
        
        if r == 1 :
            x = 1        
        classes.classenemy (x ,random.randint(0,900), 300, 287,  "imagesgame/exodia_noback.png")
        
    if totalframes % seconds3 == 0:
        r = random.randint (1,2)
        n3 -= 0.5
        
        if r == 1 :
            x = 1
            
        classes.classenemy(x,random.randint(0,900), 90, 80, "imagesgame/bomb_noback.png")

    
        

def collision (WIDTH,screen,background,FPS, totalframes):

    n = 8
    seconds = FPS*n
    health_lost = 25
    
    for enemies in classes.classenemy.List:
        shurikenkill = pygame.sprite.spritecollide(enemies, classes.classshuriken.List, True)  ##arg = object , group , dokill
##        protagonistkill = pygame.sprite.spritecollide(enemies, classes.classprotagonist.List, True)

        if len(shurikenkill) > 0:        ## if its greater than 0 theres atleast 1 that hit the enemy
            for hit in shurikenkill:
            
                enemies.health -= health_lost
                
        if totalframes % seconds == 0:
            health_lost += 25                       ## cambia la vida
                
##        elif len(protagonistkill) > 0:
##            for kill in protagonistkill:
##                 kill.destroy(classes.classprotagonist)
            
            
    for shuri in classes.classshuriken.List:                                    ##for shurikens that didnt hit anyone so it doesnt appear again from the other side

        if shuri.rect.x + shuri.width > WIDTH  or shuri.rect.x + shuri.width < 0 :
            shuri.destroy()




    
    
    













