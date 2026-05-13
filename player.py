import pygame
from circleshape import CircleShape
from shot import Shot

from constants import (
    PLAYER_RADIUS, 
    LINE_WIDTH, 
    PLAYER_SPEED, 
    PLAYER_TURN_SPEED,
    SCREEN_WIDTH, 
    SCREEN_HEIGHT, 
    PLAYER_SHOOT_SPEED, 
    SHOT_RADIUS, 
    PLAYER_SHOOT_COOLDOWN_SECONDS
)


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: float = 0
        self.shoot_cooldown = 0
        self.lives = 3
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
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown <= 0:
                self.shoot()
                self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt
            if self.shoot_cooldown < 0:
                self.shoot_cooldown = 0
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
        self.position.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.position.x))
        self.position.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.position.y))
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        velocity = rotated_vector * PLAYER_SHOOT_SPEED
        shot.velocity = velocity