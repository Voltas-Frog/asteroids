import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

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

    Player.containers = (updatable, drawable)

    PLAYER = Player(x, y)
    
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

        # Draw Handler
        for thing in drawable:
            thing.draw(screen)

        #PLAYER.draw(screen)
        #PLAYER.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()

