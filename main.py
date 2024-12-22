# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * 
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    cl = pygame.time.Clock()
    dt = 0
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color='black')

        p.draw(screen)

        pygame.display.flip()

        dt = cl.tick(60) / 1000

if __name__ == "__main__":
    main()
