import pygame
import sys
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


VERSION = pygame.version.ver

def main():
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0.0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    PLAYER = Player(x, y)
    ASTEROIDS = AsteroidField()
    
    while True:
        log_state()
        dt = clock.tick(60)/1000
        screen.fill("black")

        # Event Handler
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return
        # Update Handler
        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(PLAYER):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Draw Handler
        for thing in drawable:
            thing.draw(screen)

        #PLAYER.draw(screen)
        #PLAYER.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()

