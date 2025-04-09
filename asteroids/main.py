# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		for i in drawable:
			i.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		updatable.update(dt)

if __name__ == "__main__":
	main()
