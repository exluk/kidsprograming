import sys, pygame
import random
BLACK = 0, 0, 0
WHITE = 255, 255, 255

pygame.init()
screen = pygame.display.set_mode((1080, 720))
screens = (1080, 720)

clock = pygame.time.Clock()

class Human:
    raise_amount = 5
    def __init__(self, first_name, second_name, age, gender):
        self.age = age
        self.gender = gender
        self.first_name = first_name
        self.second_name = second_name
    def email(self):
        return '{}{}@gmail.com'.format(self.first_name, self.second_name), self.raise_amount


class Buttons:
    def __init__(self, x, y, colour, w, l):
        self.x = x
        self.y = y
        self.colour = colour
        self.w = w
        self.l = l
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.w, self.l))

class bombs:
    def __init__(self, amount, x, y, colour, w, l):
        self.amount = amount
        self.colour = colour
        self.x = x
        self.y = y
        self.w = w
        self.l = l
    def rect(self):
        for i in range(0, self.amount):
            pygame.draw.rect(screen, self.colour, self.x, self.y, self.w, self.l)


character = Buttons(50, 20, (155, 155, 155), 100, 100)
balls = Buttons(random.randint(0, 1080), random.randint(0, 720), (0, 255, 0), 50, 50)
def draw():
    character.draw(screen)
    balls.draw(screen)
    while True:
        balls.move_ip(0, 5)
        if 


rayhan = Human("naeem", "mujeeb", 5, "boy")
print(rayhan.email())
rayhan.raise_amount = 6
print(rayhan.email())
while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)
    draw()


    pygame.display.flip()
