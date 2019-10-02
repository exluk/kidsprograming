import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
size = (700, 500)
rectangleside =50
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
            #print("Hey, you pressed the key, '0'!",rectangleside)
        if event.key == pygame.K_1:
            rectangleside = rectangleside-1
            #print("Hey, you pressed the key, '1'!",rectangleside)            
    pygame.draw.rect(screen, BLACK, [rectangleside, rectangleside, rectangleside, rectangleside], 2)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()