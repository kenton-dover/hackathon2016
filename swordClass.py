import pygame
import sys
import random
import math
import constants

class swordAttack:

    swordUp = pygame.image.load("Sword_Up.png")
    swordDown = pygame.image.load("Sword_Down.png")
    swordLeft = pygame.image.load("Sword_Left.png")
    swordRight = pygame.image.load("Sword_Right.png")
    
    
    def __init__(self,location,xDirection, yDirection):
        
        self.location = location
        self.xDirection = xDirection
        self.yDirection = yDirection
        self.rect = swordAttack.swordDown.get_rect()
    

    
    def draw(self, screen):
        print(self.xDirection, self.yDirection)
        if self.yDirection == 0 and self.xDirection == 0:
            newPosition = swordAttack.swordDown
        elif self.yDirection == 1 and self.xDirection == 0:
            newPosition = swordAttack.swordUp
        elif self.yDirection == 0 and self.xDirection == 1:
            newPosition = swordAttack.swordLeft
        elif self.yDirection == 1 and self.xDirection == 1:
            newPosition = swordAttack.swordRight
        
        newPosition.set_colorkey((255, 255, 255))
        rect = newPosition.get_rect()
        if self.yDirection == 0 and self.xDirection == 0:
            rect.midtop = self.location
        elif self.yDirection == 1 and self.xDirection == 0:
            rect.midbottom = self.location
        elif self.yDirection == 0 and self.xDirection == 1:
            rect.midright = self.location
        elif self.yDirection == 1 and self.xDirection == 1:
            rect.midleft = self.location
        self.rect = rect
        
        
        screen.blit(newPosition, rect)
