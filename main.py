# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import * 
from player import Player
import sys

def main():
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('Game Over!', False, (255,255,255))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    cl = pygame.time.Clock()
    dt = 0
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)

    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    a = AsteroidField()



    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill(color='black')

        for updatable in updatables:
            updatable.update(dt)
        for drawable in drawables:
            drawable.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(p):
                screen.blit(text_surface, (0,0))
                sys.exit()


        pygame.display.flip()

        dt = cl.tick(60) / 1000

if __name__ == "__main__":
    main()
