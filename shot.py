import circleshape
from constants import *
import pygame   

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, -1).rotate(direction) * 400

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "red",
            (int(self.position.x), int(self.position.y)),
            self.radius,
        )    

    def update(self, dt):
        self.position += self.velocity * dt