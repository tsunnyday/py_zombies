import pygame
from constants import *
import random




class Zombie(pygame.sprite.DirtySprite):
	
	def __init__(self, x, y):
		super(Zombie, self).__init__()
		self.image = pygame.image.load("zombie.png").convert()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		self.sensed_player = False
		self.direction = [0,0]
		random.seed()
		
		self.randomize_direction()
		
	def update(self):
		print str(self.rect.x) + ":" + str(self.rect.y)
		if not self.sensed_player:
			self.move()
		
			
	def move(self):
		self.next_change_of_direction -= 1
		if self.next_change_of_direction:
			if not (0 <= self.rect.x + 32*self.direction[0] <= SCREEN_WIDTH - 32):
				print "OFF X"
				self.direction[0] *= -int(random.getrandbits(1))
				print self.direction[0]
			if not (0 <= self.rect.y + 32*self.direction[1] <= SCREEN_HEIGHT - 32):
				print "OFF Y"
				self.direction[1] *= -int(random.getrandbits(1))
				print self.direction[1]
			self.rect.x += self.direction[0]*32
			self.rect.y += self.direction[1]*32
		else:
			self.randomize_direction()
	
	def randomize_direction(self):
		self.next_change_of_direction = int(random.gauss(ZOMBIE_FOCUS, ZOMBIE_FOCUS_ERR))
		self.direction = [random.randrange(-1,2), random.randrange(-1,2)]
		print "CHANGED DIR TO:" + str(self.direction)
