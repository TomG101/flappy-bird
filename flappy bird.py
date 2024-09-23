import pygame

WIDTH = 864
HEIGHT = 930
TITLE = "Flappy Bird"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
run = True
bird = pygame.image.load("bird.png")
bird2 = pygame.image.load("bird2.png")
bird3 = pygame.image.load("bird3.png")
floor = pygame.image.load("floor.png")
tube = pygame.image.load("tube.png")
restart = pygame.image.load("restart.png")
sky = pygame.image.load("sky.png")

#variables

floor_x = 0
game_over = False
flying = False

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images = [bird,bird2,bird3]
        self.index = 0
        self.image =  self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 0
        self.click = False
        self.counter = 0
    def update(self):
        if flying == True:
            if self.vel < 2:
                self.vel += 0.1
            self.rect.y += self.vel
        if game_over == False:
            self.counter += 1
            if self.counter >= 30:
                self.counter = 0
                self.index += 1
                if self.index >= 3:
                    self.index = 0
                self.image =  self.images[self.index]
        

    
        

bird = Bird(300,465)
Bird_group = pygame.sprite.Group()
Bird_group.add(bird)


    

while run == True:
    screen.fill("black")
    screen.blit(sky,(0,0))
    Bird_group.draw(screen)
    Bird_group.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and game_over == False and flying == False:
            flying = True
    screen.blit(floor,(floor_x,768))
    floor_x -= 1
    if floor_x <= -36:
        floor_x = 0
    





    pygame.display.update()

