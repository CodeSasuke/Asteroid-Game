from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
import pygame
from pygame import Vector2

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: float = 0
    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(), LINE_WIDTH)

        # in the Player class
    def triangle(self):
        forward:pygame.Vector2  = pygame.Vector2(0, 1)
        forward = forward.rotate(self.rotation)

        right: pygame.Vector2 = pygame.Vector2(0, 1)
        right = right.rotate(self.rotation + 90)
        right = right * (self.radius / 1.5)
        a: pygame.Vector2 = self.position + (forward * self.radius)
        b: pygame.Vector2 = self.position - (forward * self.radius) - right
        c: pygame.Vector2 = self.position - (forward * self.radius) + right

        return [a, b, c]