import pygame
import os
pygame.init()
WIDTH,HEIGHT = 900,500
WHITE = (255,255,255) 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

FPS = 60
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 65,50
FIRST_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('assets','spaceship1.png'))
FIRST_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(FIRST_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
SECOND_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('assets','spaceship2.png'))
SECOND_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(SECOND_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

def draw_window(first,second):
    WIN.fill((WHITE))
    WIN.blit(FIRST_SPACESHIP,(first.x,first.y))
    WIN.blit(SECOND_SPACESHIP,(second.x,second.y))
    pygame.display.update()


def main():
    first = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    second = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        first.x += 1        
        draw_window(first,second)        
    pygame.quit()



if __name__ == "__main__":
    main()                    