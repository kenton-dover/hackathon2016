import pygame
import WarriorClass
import constants
import swordClass

class goesInClientLater:
        
    def run(self):
        dimensions = ( constants.SCREEN_WIDTH , constants.SCREEN_HEIGHT )
        background = pygame.image.load("flippyboard.png")
        color =   ( 0 , 0 , 0 )
        screen = pygame.display.set_mode(dimensions)
        going = True
        clock = pygame.time.Clock()
        x = 30
        y = 30
        character = WarriorClass.warriorCharacter()
        pygame.init();
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
                character.y -= 3
                character.yDirection = 1
                character.xDirection = 0

            elif pressed[pygame.K_s]and (character.y < constants.SCREEN_HEIGHT):# bounds = screen height - rectangle height 
                character.y += 3
                character.yDirection = 0
                character.xDirection = 0
                
            elif pressed[pygame.K_a] and (character.x > 0):
                character.x -= 3
                character.yDirection = 0
                character.xDirection = 1
            elif pressed[pygame.K_d]and (character.x < constants.SCREEN_WIDTH):
                character.x += 3
                character.yDirection = 1
                character.xDirection = 1
            if pressed[pygame.K_SPACE]:
                character.attack(screen)
                
            print(character.rect.centery, character.y)
            
            pygame.display.flip()#updates the window to every change that happens
    
            clock.tick(60)


        pygame.quit()
    
if __name__ == "__main__":
    newGame = goesInClientLater()
    newGame.run()
