import pygame
pygame.init();
dimensions = ( 640 , 480 )
color =   ( 255 , 255 , 255 )
screen = pygame.display.set_mode(dimensions)
background_image = pygame.image.load("ground.png").convert()
going = True
clock = pygame.time.Clock()
x = 30
y = 30

while going == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
    screen.fill(color) # ORDER MATTERS : should go Color, background, then objects
    screen.blit(background_image, [0, 0])
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and (y > 0): y -= 10 # added boundes for rectangle
    if pressed[pygame.K_DOWN]and (y < 480 - 60): y += 10 # bounds = screen height - rectangle height 
    if pressed[pygame.K_LEFT] and (x > 0): x -= 10
    if pressed[pygame.K_RIGHT]and (x < 640 - 60): x += 10
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 60, 60))
    pygame.display.flip()
    clock.tick(20)


pygame.quit()
