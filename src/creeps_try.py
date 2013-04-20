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
		for device in self.devices:
			print device.get_name()	

	def blitme(self):
		self.screen.blit(self.image, self.pos);	

	def move_down(self):
        	""" Move the raspberry down """
		displacement = vec2d(0, self.speed)
		self.pos += displacement
		self.screen.blit(self.image, self.pos)
        def move_up(self):
        	""" Move the raspberry up
        	"""
		displacement = vec2d(0, -self.speed)
                self.pos += displacement
		self.screen.blit(self.image, self.pos)

        def move_left(self):
        	""" Move the raspberry to left
        	"""
		displacement = vec2d(-self.speed, 0)
                self.pos += displacement
		self.screen.blit(self.image, self.pos)

        def move_right(self):
        	""" Move the raspberry to right
		"""
		displacement = vec2d(self.speed, 0)
                self.pos += displacement
		self.screen.blit(self.image, self.pos)
