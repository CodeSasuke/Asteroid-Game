from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SPEED, PLAYER_TURN_SPEED,SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

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
        
