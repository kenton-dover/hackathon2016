import pygame
from pygame.locals import *
import constants
import random
from constants import *
from array import array
pygame.init();
dimensions = ( SCREEN_WIDTH , SCREEN_HEIGHT )
color =   ( colorRed , colorBlue , colorGreen )
screen = pygame.display.set_mode(dimensions)
picture = pygame.image.load("flippyboard.png")
picture = pygame.transform.scale(picture,(SCREEN_WIDTH,SCREEN_HEIGHT))
background_image = picture.convert()

clock = pygame.time.Clock()
#inital position
theWeapon = pygame.Rect(0,0,0,0)#have to initialize for the collision
score = 0;
pygame.display.set_caption("Score: %s" % score)



def main():
    x = 30
    y = 30
    enemyX = 0
    enemyY = 0
    numberOfEnemies = 10
    battleField = 0
    arrayOfEnemies = []
    arrayIsFull = False
    theWeapon = pygame.Rect(0,0,0,0)#have to initialize for the collision
    score = 0;
    pygame.display.set_caption("Score: %s" % score)
    going = True
    while going == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
        screen.fill(color)
        screen.blit(background_image, [0, 0])
    
    
        pressed = pygame.key.get_pressed()

        thePerson = pygame.Rect(x, y, rectHeight, rectLength)
    
    
    
    
        if pressed[pygame.K_w] and (y > 0):# added boundes for rectangle
            y -= 10
        
            if pressed[pygame.K_SPACE]:
                theWeapon = pygame.Rect(thePerson.centerx,y+30,5,-85)
                pygame.draw.rect(screen, (0, 0, 0), theWeapon)#create rectangle in the window
        
        elif pressed[pygame.K_s]and (y < SCREEN_HEIGHT - rectLength):# bounds = screen height - rectangle height 
            y += 10
        
            if pressed[pygame.K_SPACE]:
                theWeapon = pygame.Rect(thePerson.centerx,y,5,85)
                pygame.draw.rect(screen, (0, 0, 0), theWeapon)#create rectangle in the window
        elif pressed[pygame.K_a] and (x > 0):
            x -= 10
       
            if pressed[pygame.K_SPACE]:
                theWeapon = pygame.Rect(x-50,thePerson.centery,85,5)
                pygame.draw.rect(screen, (0, 0, 0), theWeapon)#create rectangle in the window
       
        elif pressed[pygame.K_d]and (x < SCREEN_WIDTH - rectHeight):
            x += 10
        
            if pressed[pygame.K_SPACE]:
                theWeapon = pygame.Rect(x,thePerson.centery,85,5)
                pygame.draw.rect(screen, (0, 0, 0), theWeapon)#create rectangle in the window

        pygame.draw.rect(screen, (0, 128, 255), thePerson)#create rectangle in the window
    

        if not(arrayIsFull):
            for i in range(numberOfEnemies):
                enemyX = random.randint(0,SCREEN_WIDTH)
                enemyY = random.randint(0,SCREEN_HEIGHT)
                theEnemy = pygame.Rect(enemyX,enemyY,50,50)
                arrayOfEnemies.append(theEnemy)
                pygame.draw.rect(screen,(0,0,0),theEnemy)
                if arrayOfEnemies.index(theEnemy) == 9:
                    arrayIsFull = True     
        for i in range(numberOfEnemies):
            tempEnemy = arrayOfEnemies.pop(i)
            pygame.draw.rect(screen,(0,0,0),tempEnemy)#prints the enemies
            if not theWeapon.colliderect(tempEnemy):
                arrayOfEnemies.insert(i, tempEnemy)
            else:
                enemyX = random.randint(0,SCREEN_WIDTH)
                enemyY = random.randint(0,SCREEN_HEIGHT)
                theEnemy = pygame.Rect(enemyX,enemyY,50,50)
                arrayOfEnemies.insert(i, theEnemy)
                pygame.draw.rect(screen,(0,0,0),theEnemy)

                score = score + 1
                pygame.display.set_caption("Score: %s" % score)
               
            
        for i in range(numberOfEnemies):
            tempEnemy = arrayOfEnemies.pop(i)
            direction = random.randint(0, 1000)
            if direction < 250:
                tempEnemy = tempEnemy.move(-10,0)
            elif direction < 500 and direction > 250:
                tempEnemy = tempEnemy.move(0,-10)
            elif direction < 750 and direction > 500:
                tempEnemy = tempEnemy.move(10,0)
            elif direction < 1000 and direction > 750:
                tempEnemy = tempEnemy.move(0,10)
            arrayOfEnemies.insert(i, tempEnemy)
    
        pygame.display.flip()#updates the window to every change that happens
    
        clock.tick(20)


    pygame.quit()

       

if __name__ == '__main__':
    main()
                                       



