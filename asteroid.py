from circleshape import CircleShape
from constants import *
import pygame 
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            self.radius,
            LINE_WIDTH,
        )    

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        print(self.velocity)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vector1 = pygame.Vector2(1, 0).rotate(self.rotation + angle)
            vector2 = pygame.Vector2(1, 0).rotate(self.rotation - angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1*120
            print("velocity:", asteroid1.velocity)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = vector2*120
        