class snake:
    def __init__(self):
        self.y = random.randrange(1,400)
        self.x = random.randrange(1,300)
        self.speed = 10
        self.length = 1
        self.direction =

    def draw(self,screen):
        pygame.draw.rect(screen,(0,0,255),[self.x,self.y,100,15,15],0)