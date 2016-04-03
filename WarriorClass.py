import pygame
import sys
import random
import math
import constants
import swordClass

class warriorCharacter:
    downSprite = pygame.image.load("Knight_Down_Still.png")
    upSprite = pygame.image.load("Knight_Up_Still.png")
    leftSprite = pygame.image.load("Knight_Left_Still.png")
    rightSprite = pygame.image.load("Knight_Right_Still.png")
    
    def __init__(self):
        self.x = random.randint(0, constants.SCREEN_WIDTH)
        self.y = random.randint(0, constants.SCREEN_HEIGHT)
        self.yDirection = 0
        self.xDirection = 0
        self.rect = warriorCharacter.downSprite.get_rect()
        self.location = self.rect.center

    
    def draw(self, screen):
        newPosition = warriorCharacter.downSprite
        if self.yDirection == 0 and self.xDirection == 0:
            newPosition = warriorCharacter.downSprite
        elif self.yDirection == 1 and self.xDirection == 0:
            newPosition = warriorCharacter.upSprite
        elif self.yDirection == 0 and self.xDirection == 1:
            newPosition = warriorCharacter.leftSprite
        elif self.yDirection == 1 and self.xDirection == 1:
            newPosition = warriorCharacter.rightSprite
        
        newPosition.set_colorkey((255, 255, 255))
        rect = newPosition.get_rect()
        rect.centerx = self.x
        rect.centery = self.y
        self.rect = rect
        if self.yDirection == 0 and self.xDirection == 0:
            self.location = rect.midbottom
        elif self.yDirection == 1 and self.xDirection == 0:
            self.location = rect.midtop
        elif self.yDirection == 0 and self.xDirection == 1:
            self.location = rect.midleft
        elif self.yDirection == 1 and self.xDirection == 1:
            self.location = rect.midright
        screen.blit(newPosition, rect)
        
    def attack(self, screen):
        
        
        
        sword = swordClass.swordAttack(self.location, self.xDirection, self.yDirection)
        sword.draw(screen)
