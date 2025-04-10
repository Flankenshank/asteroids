import pygame
import random
from circleshape import *
from constants import *

class Asteroid(pygame.sprite.Sprite):
	def __init__(self, x, y, radius):
		super().__init__(self.containers)
		self.position = pygame.Vector2(x, y)
		self.velocity = pygame.Vector2(0, 0)
		self.radius = radius

	def update(self, dt=0):
		self.position += self.velocity * dt

	def draw(self, screen):
		pygame.draw.circle(screen,"white", (self.position.x, self.position.y), self.radius, 2)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		random_angle = random.uniform(20,50)
		vector1 = self.velocity.rotate(random_angle) * 1.2
		vector2 = self.velocity.rotate(-random_angle) * 1.2
		new_asteroid1 = Asteroid(self.position.x, self.position.y,self.radius - ASTEROID_MIN_RADIUS)
		new_asteroid1.velocity = vector1
		new_asteroid2 = Asteroid(self.position.x, self.position.y,self.radius - ASTEROID_MIN_RADIUS)
		new_asteroid2.velocity = vector2
