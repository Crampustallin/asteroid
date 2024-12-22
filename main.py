# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    cl = pygame.time.Clock()
    dt = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color='black')
        pygame.display.flip()

        dt = cl.tick(60) / 1000

if __name__ == "__main__":
    main()
