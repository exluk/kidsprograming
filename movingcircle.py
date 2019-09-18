import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
cprama1 =10
cparam2 =10
cparam3 =10
size = (700, 500) #screen size define
rectangleside =50  #intial size of rectangle
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kids lesson")
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    #pygame.draw.line(screen, GREEN, [0, 0], [700, 500], 5)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_0:
            rectangleside = rectangleside+1
            cprama1 =10
            cparam2 =10
            cparam3 =10
            #print("Hey, you pressed the key, '0'!",rectangleside)
        if event.key == pygame.K_2: #horizontal
            cprama1 = cprama1+1
        if event.key == pygame.K_3: # down
            cparam2 = cparam2+1
        if event.key == pygame.K_4: #radius 
            cparam3 = cparam3+1        
            #print("Hey, you pressed the key, '1'!",rectangleside)            
    #pygame.draw.rect(screen, BLACK, [rectangleside, rectangleside, rectangleside, rectangleside], 2)
    #circle(surface, color, center, radius, width=0) -> Rect
    pygame.draw.circle(screen, RED, [cprama1,cparam2], cparam3, 0)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()