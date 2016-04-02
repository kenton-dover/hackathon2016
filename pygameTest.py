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
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 60, 60))
    pygame.display.flip()
    clock.tick(20)


pygame.quit()
