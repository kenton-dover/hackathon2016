import pygame
import WarriorClass
import constants

class goesInClientLater:

        
    def run(self):
        dimensions = ( constants.SCREEN_WIDTH , constants.SCREEN_HEIGHT )
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
            character.draw(screen)
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w] and (y > 0):# added boundes for rectangle
                character.y -= 10
                character.yDirection = 1
                character.xDirection = 0

            elif pressed[pygame.K_s]and (y < 480 - 60):# bounds = screen height - rectangle height 
                character.y += 10
                character.yDirection = 0
                character.xDirection = 0
                
            elif pressed[pygame.K_a] and (x > 0):
                character.x -= 10
                character.yDirection = 0
                character.xDirection = 1
            elif pressed[pygame.K_d]and (x < 640 - 60):
                character.x += 10
                character.yDirection = 1
                character.xDirection = 1
    
            pygame.display.flip()#updates the window to every change that happens
    
            clock.tick(60)


        pygame.quit()
    
if __name__ == "__main__":
    newGame = goesInClientLater()
    newGame.run()
