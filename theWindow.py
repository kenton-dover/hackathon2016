import pygame
pygame.init();
dimensions = ( 640 , 480 )
color =   ( 0 , 0 , 0 )
screen = pygame.display.set_mode(dimensions)
going = True
clock = pygame.time.Clock()
x = 30
y = 30


while going == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
    screen.fill(color)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] and (y > 0):# added boundes for rectangle
        y -= 10
        theWeapon = pygame.Rect(x+50,y,5,-50)
        if pressed[pygame.K_SPACE]:
            pygame.draw.rect(screen, (0, 128, 255), theWeapon)#create rectangle in the window
    if pressed[pygame.K_s]and (y < 480 - 60):# bounds = screen height - rectangle height 
        y += 10
        theWeapon = pygame.Rect(x,y,5,100)
        if pressed[pygame.K_SPACE]:
            pygame.draw.rect(screen, (0, 128, 255), theWeapon)#create rectangle in the window
    if pressed[pygame.K_a] and (x > 0):
        x -= 10
        theWeapon = pygame.Rect(x-50,y,100,5)
        if pressed[pygame.K_SPACE]:
            pygame.draw.rect(screen, (0, 128, 255), theWeapon)#create rectangle in the window
        theWeapon = pygame.Rect(x,y+50,100,5)
    if pressed[pygame.K_d]and (x < 640 - 60):
        x += 10
        theWeapon = pygame.Rect(x+20,y,100,5)
        if pressed[pygame.K_SPACE]:
            pygame.draw.rect(screen, (0, 128, 255), theWeapon)#create rectangle in the window
    thePerson = pygame.Rect(x, y, 60, 60)
    
    pygame.draw.rect(screen, (0, 128, 255), thePerson)#create rectangle in the window
    
    pygame.display.flip()#updates the window to every change that happens
    
    clock.tick(20)


pygame.quit()
