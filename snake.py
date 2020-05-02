import pygame
import random

class snake:
    def __init__(self):
        #Initialize the snake with coords,speed,length
        self.x = random.randrange(1,400)
        self.y = random.randrange(1,300)
        self.speed = 1
        self.length = 1
        self.direction = random.randrange(1,5)

    def draw(self,screen,height,width):
        if self.x >= height:
            self.x = 5
        elif self.x <= 0:
            self.x = height - 15
        if self.y >= width:
            self.y = 5
        elif self.y <= 0:
            self.y = width - 15

        pygame.draw.rect(screen,(0,0,255),[self.y,self.x,15,15])

    def movement(self,key):
        #this handles key input
        if key.type == pygame.KEYDOWN:
            if key.key == pygame.K_LEFT:
                self.direction  = 1;

            if key.key == pygame.K_UP:
                self.direction  = 2;

            if key.key == pygame.K_DOWN:
                self.direction  = 3;

            if key.key == pygame.K_RIGHT:
                self.direction  = 4;


    def snake_direction(self):
        #this handles self movement based of direction off the snake
            if self.direction == 1:
                #left
                self.y -= self.speed
            elif self.direction == 2:
                #up
                self.x -= self.speed
            elif self.direction == 3:
                #down
                self.x += self.speed
            elif self.direction == 4:
                #right
                self.y += self.speed


class food:
    def __init__(self):
        self.y = random.randrange(1,400)
        self.x = random.randrange(1,300)
        self.spawned = False
    def draw(self,screen):
        if self.spawned == False:
            pygame.draw.rect(screen,(0,255,0),[self.y,self.x,15,15])
    def respawn(self):
        self.y = random.randrange(1,400)
        self.x = random.randrange(1,300)