
import pygame, random , math

##Defining "BaseClass" which will define all variables needed for the game

class BaseClass(pygame.sprite.Sprite):    ##sprite class as it contains motion, drawing etc, collision detection   

    allsprites = pygame.sprite.Group()   ##making allsprite hold like a list of all sprites in the game
    
    def __init__( self ,x,y,width,height,image_string):
        
            pygame.sprite.Sprite.__init__(self)     ##calling sprite classes "Sprite"
            BaseClass.allsprites.add(self)          ##adding to allsprites

    
        ##Sprite class gives as access to these
        
            self.image = pygame.image.load(image_string)   ##actual image // this is from sprite class

            self.rect = self.image.get_rect()    ##square of the image // controls width height absolute position
            self.rect.x = x
            self.rect.y = y

            self.width = width
            self.height = height

    def destroy (self , ClassName):                 ##creating method "destroy" to remove from list self

        ClassName.List.remove(self)
        BaseClass.allsprites.remove(self)
        del self 


class classprotagonist(BaseClass):       ##creating protagonist class
    
    List = pygame.sprite.Group()      ##list of protagonist specific group

    shurikenright = True            ##keep track of direction 
    
    def __init__(self,x,y,width,height,image_string):

            BaseClass.__init__(self,x,y,width,height,image_string)
            classprotagonist.List.add(self)  ##add all bugs to this list when theyre created

            self.velx = 0               ##defining horizontal velocity
            self.vely = 15              ##vertical velocity
            self.jumping = False        ##jumping is a two way process
            self.go_down = False            
        
    def motion(self,WIDTH,HEIGHT):

        if self.rect.x < 0:                 ##wall collision
            self.rect.x=0
            
        elif self.rect.x + self.width > WIDTH:      
            self.rect.x = WIDTH - self.width
        
                                           
        self.rect.x += self.velx            ##movement


        max_jump = 50                     ##set like a line for max jump but remember is 500 pixels downwards
        
        if self.jumping:

                if self.rect.y < max_jump:      ##Checking if it is more than predetermined value
                    self.go_down =  True

                if self.go_down:                ## motion of protagonist when going down
                    self.rect.y += self.vely

                    predicted_location = self.rect.y + self.vely    ## predicting the postion of the rectangle of the image as it has vertical velocity

                    if predicted_location + self.height > HEIGHT:       ## if the predicted is more than the vertical pixels then set to false
                        self.jumping = False                            ## to be able to jump again
                        self.go_down = False
                    
                else:
                    self.rect.y -= self.vely



class classenemy (BaseClass):                            ##enemyclass

    List = pygame.sprite.Group()

    
    def __init__(self,x,y,width,height,image_string):       

        BaseClass.__init__(self,x,y,width,height,image_string)
        classenemy.List.add(self)

        self.velx = random.randint ( 3 , 7)         ## to give the enemy different speeds in integers 
        self.amplitude, self.period = random.randint (0, 500), random.randint (1,10)/1000.0 

        health_increase = 0
        FPS = 30
        time = 15
        seconds = FPS * time
        totalframes = 0
        
        self.health = 100

        if totalframes % time == 0:                 ##health increase every "time" seconds
            health_increase += 50
            self.health += health_increase
    

    @staticmethod 
    def update_all(WIDTH,HEIGHT):                                   ##predefine method
        for enemies in classenemy.List:
            enemies.enemymotion(WIDTH, HEIGHT)
            
            if enemies.health <= 0 :
                enemies.destroy (classenemy)
                
        
    def enemymotion(self,WIDTH,HEIGHT):

        if self.rect.x + self.width > WIDTH or self.rect.x < 0:         ##cheking if the enemy hits the wall 

            self.image = pygame.transform.flip (self.image , True, False)  ##arg == what image, horizontal flip, vertical flip (in boolean)
            self.velx = -self.velx
            
        self.rect.x += self.velx

        self.rect.y = self.amplitude * math.sin (self.period * self.rect.x) + 450

##    @staticmethod
##    def movement(WIDTH,HEIGHT):
##        for enemies in classenemy.List:
##            enemies.enemymotion(WIDTH,HEIGHT)
##    

class classshuriken (pygame.sprite.Sprite):                                    ##classshuriken
    
    List= pygame.sprite.Group()
    normal_list = []                                ## second list
    
    def __init__ (self,x,y,width,height,image_string):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(image_string)   ##actual image // this is from sprite class

        self.rect = self.image.get_rect()    ##square of the image // controls width height absolute position
        self.rect.x = x
        self.rect.y = y

        self.width = width
        self.height = height

        try:                                                    ## setting rules on shuriken
            lasts_element = classshuriken.normal_list[-1]
            difference = abs(self.rect.x - last_element.rect.x)

            if difference < self.width:
                return

        except Exception:
            pass

        classshuriken.normal_list.append(self)                  ##adding to both list .. "append" for normal python list
        classshuriken.List.add(self)

        self.velx = None

    @staticmethod
    def movement():
        
        for shuriken in classshuriken.List:
            shuriken.rect.x += shuriken.velx

    def destroy (self):
        classshuriken.List.remove(self)
        classshuriken.normal_list.remove(self)
        del self


        
        


