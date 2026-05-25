import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH )
        return

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        return

    def split(self, old):
        old.kill()
        if (old.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            log_event("asteroid_split")
            rand_rot = random.uniform(20, 50)
            split1_rot = old.velocity.rotate(rand_rot)
            split2_rot = old.velocity.rotate(-rand_rot)
            split_rad = old.radius - ASTEROID_MIN_RADIUS
            split1 = Asteroid(old.position.x, old.position.y, split_rad)
            split2 = Asteroid(old.position.x, old.position.y, split_rad)
            split1.velocity = split1_rot
            split2.velocity = split2_rot
