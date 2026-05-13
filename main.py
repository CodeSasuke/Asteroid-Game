import pygame
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event
import sys
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    clock = pygame.time.Clock()
    Player.containers = (updatable, drawable)  #type: ignore
    Asteroid.containers = (asteroids, updatable, drawable) #type: ignore
    Shot.containers = (shots, updatable, drawable) #type: ignore
    AsteroidField.containers = (updatable) #type: ignore
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if player.collides_with(obj):
                log_event("player_hit")
                player.lives -= 1
                if player.lives == 0:
                    print("Game over!")
                    sys.exit()
            for shot in shots:
                if shot.collides_with(obj):
                    log_event("asteroid_shot")
                    obj.split()
                    shot.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        # print(dt)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
