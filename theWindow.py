import pygame
import WarriorClass
import constants
import random

class goesInClientLater:
        
    def run(self):
        pygame.init();
        enemyX = 0
        enemyY = 0
        score = 0
        numberOfEnemies = 10
        battleField = 0
        arrayOfEnemies = []
        arrayIsFull = False
        dimensions = ( constants.SCREEN_WIDTH , constants.SCREEN_HEIGHT )
        screen = pygame.display.set_mode(dimensions)
        background = pygame.image.load("flippyboard.png")
        background = pygame.transform.scale(background,(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
        background_image = background.convert()
        color =   ( 0 , 0 , 0 )
        screen = pygame.display.set_mode(dimensions)
        going = True
        clock = pygame.time.Clock()
        x = 30
        y = 30
        character = WarriorClass.warriorCharacter()
        
        going = True
        while going == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    going = False
            screen.fill(color)
            screen.blit(background, [0, 0])
            character.draw(screen)
            pressed = pygame.key.get_pressed()
            
            if pressed[pygame.K_w] and (character.y > 0):# added boundes for rectangle
                character.y -= 5
                character.yDirection = 1
                character.xDirection = 0

            elif pressed[pygame.K_s]and (character.y < constants.SCREEN_HEIGHT):# bounds = screen height - rectangle height 
                character.y += 5
                character.yDirection = 0
                character.xDirection = 0
                
            elif pressed[pygame.K_a] and (character.x > 0):
                character.x -= 5
                character.yDirection = 0
                character.xDirection = 1
            elif pressed[pygame.K_d]and (character.x < constants.SCREEN_WIDTH):
                character.x += 5
                character.yDirection = 1
                character.xDirection = 1
            if pressed[pygame.K_SPACE]:
                character.attack(screen)
                
            if not(arrayIsFull):
                for i in range(numberOfEnemies):
                    enemyX = random.randint(0,constants.SCREEN_WIDTH)
                    enemyY = random.randint(0,constants.SCREEN_HEIGHT)
                    theEnemy = pygame.Rect(enemyX,enemyY,50,50)
                    arrayOfEnemies.append(theEnemy)
                    pygame.draw.rect(screen,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)),theEnemy)
                    if arrayOfEnemies.index(theEnemy) == 9:
                        arrayIsFull = True     
            for i in range(numberOfEnemies):
                tempEnemy = arrayOfEnemies.pop(i)
                pygame.draw.rect(screen,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)),tempEnemy)#prints the enemies
                if not character.sword.rect.colliderect(tempEnemy):
                    arrayOfEnemies.insert(i, tempEnemy)
                else:
                    enemyX = random.randint(0,constants.SCREEN_WIDTH)
                    enemyY = random.randint(0,constants.SCREEN_HEIGHT)
                    theEnemy = pygame.Rect(enemyX,enemyY,50,50)
                    arrayOfEnemies.insert(i, theEnemy)
                    pygame.draw.rect(screen,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)),theEnemy)

                    score = score + 1
                    pygame.display.set_caption("Score: %s" % score)
            
            for i in range(numberOfEnemies):
                tempEnemy = arrayOfEnemies.pop(i)
                direction = random.randint(0, 1000)
                if direction < 250:
                    if tempEnemy.centerx - 10 > 0:
                        tempEnemy = tempEnemy.move(-10,0)
                elif direction < 500 and direction > 250:
                    if tempEnemy.centery - 10 > 0:
                        tempEnemy = tempEnemy.move(0,-10)
                elif direction < 750 and direction > 500:
                    if tempEnemy.centerx + 10 < constants.SCREEN_WIDTH:
                        tempEnemy = tempEnemy.move(10,0)
                elif direction < 1000 and direction > 750:
                    if tempEnemy.centery + 10 < constants.SCREEN_HEIGHT:
                        tempEnemy = tempEnemy.move(0,10)
                arrayOfEnemies.insert(i, tempEnemy)            
                pygame.display.flip()#updates the window to every change that happens
    
            clock.tick(60)


        pygame.quit()
    
if __name__ == "__main__":
    newGame = goesInClientLater()
    newGame.run()
