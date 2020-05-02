import random
import pygame
from snake import snake,food
#from snake import snake
#
HEIGHT = 500
WIDTH = 500
snake = snake()
food = food()
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
            snake.movement(event)
        snake.snake_direction()
        screen.fill((255,255,255))
        snake.draw(screen,HEIGHT,WIDTH)
        if food.x < snake.x < food.x + 15 and food.y < snake.y < food.y + 15 or food.x < snake.x + 15 < food.x + 15 and food.y < snake.y + 15 < food.y + 15 :
            food.respawn()
        food.draw(screen)
        pygame.display.update()
        clock.tick(100)


def main():
    #This is the main function
    init()
    gameloop()




if __name__ == "__main__":
    main()



