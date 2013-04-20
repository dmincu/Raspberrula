# Raspberrula Game - Raspberry Hack
import os, sys
from random import randint, choice
from math import sin, cos, radians
import pygame
from pygame.sprite import Sprite
from vec2d import vec2d

class MoveRasp(Sprite):
	""" A raspberry controlled by pointing arrows
	"""
	def __init__(
		self, screen, img_filename, init_position,
		init_direction, speed, devices):
		
		Sprite.__init__(self)
		self.collision = 0
		self.screen = screen
		self.speed = speed
		self.devices = devices.my_list
		self.base_image = pygame.image.load(img_filename).convert_alpha()
		self.size = (self.base_image.get_width(), self.base_image.get_height())
		self.base_image = pygame.transform.scale(self.base_image, self.size)
		self.image = self.base_image

	# base image holds the original image, positioned to
	# angle 0.
	
		self.pos = vec2d(init_position)

	def collisions(self):
		self.collision = 0
		for device in self.devices:
			upper_limit = device.get_upper()
			lower_limit = device.get_lower()
			my_pos = self.pos
			if (self.pos.x > upper_limit[0] and \
			self.pos.x < lower_limit[0] and \
			self.pos.y > upper_limit[1] and \
			self.pos.y < lower_limit[1]):
				self.collision = 1
				print "coliziune"		

	def blitme(self):
		self.screen.blit(self.image, self.pos);	

	def move_down(self):
        	""" Move the raspberry down """
		self.collisions()
		print self.collision
		if (self.collision == 0):
			displacement = vec2d(0, self.speed)
			self.pos += displacement
			self.screen.blit(self.image, self.pos)
        def move_up(self):
        	""" Move the raspberry up
        	"""
		self.collisions()
		if (self.collision == 0):
			displacement = vec2d(0, -self.speed)
                	self.pos += displacement
			self.screen.blit(self.image, self.pos)

        def move_left(self):
        	""" Move the raspberry to left
        	"""
		self.collisions()
		if (self.collision == 0):
			displacement = vec2d(-self.speed, 0)
                	self.pos += displacement
			self.screen.blit(self.image, self.pos)

        def move_right(self):
        	""" Move the raspberry to right
		"""
		self.collisions()
		if (self.collision == 0):
			displacement = vec2d(self.speed, 0)
                	self.pos += displacement
			self.screen.blit(self.image, self.pos)
