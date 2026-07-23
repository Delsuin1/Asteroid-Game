import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt) -> None:
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        vector_velocity_1 = self.velocity.rotate(angle)
        vector_velocity_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        temp_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        temp_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        temp_asteroid_1.velocity += vector_velocity_1 * 1.2
        temp_asteroid_2.velocity += vector_velocity_2 * 1.2
        