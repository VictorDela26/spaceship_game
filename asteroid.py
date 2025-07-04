from circleshape import *
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            blue_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(blue_angle) * 1.2
            velocity2 = self.velocity.rotate(-blue_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid(self.position.x,self.position.y,new_radius).velocity = velocity1
            Asteroid(self.position.x,self.position.y,new_radius).velocity = velocity2