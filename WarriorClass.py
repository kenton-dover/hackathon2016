import pygame
import sys
import random
import math
import constants

class warriorCharacter:
    characterSprite = pygame.image.load("Knight_Down_Still.png")
    def __init__(self):
        self.x = random.randint(0, constants.SCREEN_WIDTH)
        self.y = random.randint(0, constants.SCREEN_HEIGHT)

    

    
    def draw(self, screen):
        newPosition = warriorCharacter.characterSprite
        newPosition.set_colorkey((255, 255, 255))
        rect = newPosition.get_rect()
        rect.centerx = self.x
        rect.centery = self.y
        
        screen.blit(newPosition, rect)
