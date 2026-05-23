import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

VERSION = pygame.version.ver

def main():
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
    pygame.init()

    screen = pygame.display.set_mode((SCREEND_WIDTH, SCREEN_HEIGHT))
    
    while True:
        log_state()
        for event in pygame.event.get():
            fill("black")
            display.flip()


