import pygame
from circleshape import *
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
        self.angle = random.uniform(20,50)
        self.vector1 = self.velocity.rotate(self.angle)
        self.vector2 = self.velocity.rotate(-self.angle)
        self.vector3 = self.velocity.rotate(self.angle/2)
        self.vector4 = self.velocity.rotate(self.angle*2)
        self.new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        new_asteroid = Asteroid(self.position, self.position, self.new_radius)
        new_asteroid.velocity = self.vector2*1.2
        new_asteroid2 = Asteroid(self.position, self.position, self.new_radius)
        new_asteroid2.velocity = self.vector1*1.2
        new_asteroid3 = Asteroid(self.position, self.position, self.new_radius)
        new_asteroid3.velocity = self.vector1*3
        self.rand_num = random.uniform(1,4)
        if self.rand_num >= 2:
            new_asteroid5 = Asteroid(self.position, self.position, self.new_radius)
            new_asteroid5.velocity = self.vector4*4
        if self.rand_num >= 3.9:
            new_asteroid6 = Asteroid(self.position, self.position, self.new_radius+3)
            new_asteroid6.velocity = self.vector2*3.5
            new_asteroid7 = Asteroid(self.position, self.position, self.new_radius+12)
            new_asteroid7.velocity = self.vector1*5
            new_asteroid8 = Asteroid(self.position, self.position, self.new_radius+32)
            new_asteroid8.velocity = self.vector4*4
            new_asteroid9 = Asteroid(self.position, self.position, self.new_radius+3)
            new_asteroid9.velocity = self.vector2*3.5
            new_asteroid10 = Asteroid(self.position, self.position, self.new_radius+12)
            new_asteroid10.velocity = self.vector1*18
            new_asteroid11 = Asteroid(self.position, self.position, self.new_radius+6)
            new_asteroid11.velocity = self.vector4*4
            new_asteroid12 = Asteroid(self.position, self.position, self.new_radius+3)
            new_asteroid12.velocity = self.vector2*34
            new_asteroid13 = Asteroid(self.position, self.position, self.new_radius-7)
            new_asteroid13.velocity = self.vector1*0.4
            new_asteroid14 = Asteroid(self.position, self.position, self.new_radius-11)
            new_asteroid14.velocity = self.vector4*2.2
