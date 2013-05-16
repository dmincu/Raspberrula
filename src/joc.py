# Raspberrula Game - Raspberry Hack

import pygame
import os
import sys
import easygui
from pygame.locals import *
from raspberry import MoveRasp
from portal import DrawPortal
from configure import DeviceConfigure


class Game:
	"""
		Class that implements game functionality and draw-ing of objects
	"""
	def __init__(self, devices):
		pygame.init()

		# Set class variables
		self.portals = []
		self.devices = devices
		self.screen_width = 760
		self.screen_height = 570
		self.rasp_filename = "../images/rasp.png"
		self.bg_color = 150, 150, 80
		self.window = pygame.display.set_mode((self.screen_width, self.screen_height))

		# Init game window
		pygame.display.set_caption('Raspberrula')
		self.screen = pygame.display.get_surface()
		self.rasp = "../images/Raspberrula.jpg"
		self.rasp_surface = pygame.image.load(self.rasp)
		self.rasp_surface = pygame.transform.scale(self.rasp_surface, (self.screen_width, self.screen_height))
		self.screen.blit(self.rasp_surface, (0,0))
		self.rasp = MoveRasp(self.window,	\
				self.rasp_filename,	\
				(self.screen_width / 2,	\
				self.screen_height / 2),	\
				(1, 1),	\
				1,
				self.devices)
		self.devconf = DeviceConfigure(self.devices)		

		# init portals
		i = 0
		for device in self.devices.my_list:
			portal_coord = device.get_portal_coord()
			self.portals.append(DrawPortal(self.window,
						"../images/portal.png",
						portal_coord,
						))
	
	def run(self):
		self.screen.blit(self.rasp_surface, (0,0))
		self.rasp.blitme()
		for portal in self.portals:
			portal.blitme()
		pygame.display.update()

		# Draw objects on screen
		while True:
			self.screen.blit(self.rasp_surface, (0,0))
			self.input(pygame.event.get())
			for portal in self.portals:
                        	portal.blitme()
			self.rasp.blitme()
			pygame.display.update(Rect((self.rasp.pos.x - 10, self.rasp.pos.y - 10), (80, 80)))


	def input(self,events):
		for event in events:
                        if event.type == QUIT:
                                sys.exit(0)

		keys = pygame.key.get_pressed()
		if keys[K_LEFT]:
			self.rasp.move_left()
		if keys[K_RIGHT]:
			self.rasp.move_right()
		if keys[K_DOWN]:
			self.rasp.move_down()
		if keys[K_UP]:
			self.rasp.move_up()

		if (self.rasp.portal_collision[0] == 1):
			for event in events:
                        	if event.type == KEYDOWN:
					if event.key == K_RETURN:
						self.devconf.popup(self.rasp.portal_collision[1])	
