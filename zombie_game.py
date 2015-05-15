import pygame, sys, time
from pygame.locals import *
from constants import *
import zombie




pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ZOMBIES!")

instances = pygame.sprite.RenderUpdates()
instances.add(zombie.Zombie(32, 32))
instances.add(zombie.Zombie(320,64))
instances.add(zombie.Zombie(128, 256))


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	time.sleep(.5)
	
	instances.update()
		
	
	
	screen.fill((255, 255, 255))
	instances.draw(screen)
	pygame.display.update()
