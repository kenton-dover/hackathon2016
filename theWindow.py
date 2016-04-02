import pygame, sys #this is my imports
pygame.init()#initializes the pygame

gameDisplay = pygame.display.set_mode((800,600))#creates the display
pygame.display.set_caption('the game')#sets the caption of the window
clock = pygame.time.Clock()# creates a game clock

theGameCrashed = False#sets a flag incase the game crashes



WHITE = (255,255,255)
BLUE = ( 0,0,255)
gameDisplay.fill(WHITE)#fills the back ground 


while not theGameCrashed:#checks to see if the game has crashed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()

