import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, PLAYER_RADIUS, LINE_WIDTH, PLAYER_SPEED, PLAYER_TURN_SPEED,SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
        # clamps the position of the asteroid to the screen
        # self.position.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.position.x))
        # self.position.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.position.y))
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20,50)
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid1.velocity = velocity1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid2.velocity = velocity2 * 1.2

        