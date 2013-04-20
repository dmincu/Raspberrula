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
		self.portal_collision = [0, None]
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
		i = 0
		for device in self.devices:
			upper_limit = device.get_upper()
			lower_limit = device.get_lower()
			
			portal_x = (device.get_portal_coord())[0]
			portal_y = (device.get_portal_coord())[1]

			my_pos = self.pos
			
			if (cmp(device.get_name(), 'PLACA') == 0):
				if (	(self.pos.x < upper_limit[0]
				    or self.pos.x > lower_limit[0])
				    or (self.pos.y < upper_limit[1]
				    or self.pos.y > lower_limit[1])
				   ):
					self.collision = 1
			else:
				if (	self.pos.x > upper_limit[0]
				    and self.pos.x < lower_limit[0]
				    and self.pos.y > upper_limit[1]
				    and self.pos.y < lower_limit[1]
				   ):
					self.collision = 1
				
				if (    self.pos.x + 18 > portal_x
                                    and self.pos.x + 18 < portal_x + 34
                                    and self.pos.y + 16 > portal_y
                                    and self.pos.y + 16 < portal_y + 36
                                   ):
                                        self.portal_collision[0] = 1
					self.portal_collision[1] = device
					print "Coliziune cu ursul"
			i += 1
	
	def blitme(self):
		self.screen.blit(self.image, self.pos);	

	def move_down(self):
        	""" Move the raspberry down """
		displacement = vec2d(0, self.speed)
		self.pos += displacement
		self.collisions()
		if (self.collision == 1):
			self.pos -= displacement
			self.screen.blit(self.image, self.pos)
        def move_up(self):
        	""" Move the raspberry up
        	"""
		displacement = vec2d(0, -self.speed)
                self.pos += displacement
		self.collisions()
		if (self.collision == 1):
			self.pos -= displacement
			self.screen.blit(self.image, self.pos)

        def move_left(self):
        	""" Move the raspberry to left
        	"""
		displacement = vec2d(-self.speed, 0)
                self.pos += displacement
		self.collisions()
		if (self.collision == 1):
			self.pos -= displacement
			self.screen.blit(self.image, self.pos)

        def move_right(self):
        	""" Move the raspberry to right
		"""
		displacement = vec2d(self.speed, 0)
               	self.pos += displacement
		self.collisions()
		if (self.collision == 1):
			self.pos -= displacement
			self.screen.blit(self.image, self.pos)
