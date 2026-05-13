import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self, self.containers) #type: ignore
        self.velocity = pygame.Vector2(0, 0)  # Initialize velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt