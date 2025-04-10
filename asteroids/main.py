# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)
	player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		for shot in shots:
			for asteroid in asteroids:
				if shot.collision(asteroid):
					shot.kill()
					asteroid.kill()
		for i in asteroids:
			if player.collision(i) == True:
				print("Game over!")
				exit()
		for i in drawable:
			i.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		updatable.update(dt)

if __name__ == "__main__":
	main()
