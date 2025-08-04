import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
   
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        updateable.update(dt)
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
     
        ms_passed = clock.tick(60)
        dt = ms_passed / 1000


if __name__ == "__main__":

    main()