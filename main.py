# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
import sys
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("My Game")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))

        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()
                    asteroid.kill()
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()


