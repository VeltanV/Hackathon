import random
import pygame
from snake import snake
#from snake import snake
#
HEIGHT = 300
WIDTH = 400
snakero = snake()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

def init():
    pygame.init()
    pygame.display.set_caption("Hackathon Snake Game")


def gameloop():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            snakero.movement(event)
        snakero.snake_direction()
        screen.fill((255,255,255))
        snakero.draw(screen)
        pygame.display.update()
        clock.tick(50)


def main():
    #This is the main function
    init()
    gameloop()




if __name__ == "__main__":
    main()



