import pygame,os,sys
from pygame.locals import *
from creeps_try import MoveRasp
from portal import DrawPortal
import easygui


class Game:

	def __init__(self, devices):
		pygame.init()
		self.portals = []
		self.devices = devices
		self.SCREEN_WIDTH = 760
		self.SCREEN_HEIGHT = 570
		self.RASP_FILENAME = "rasp.png"
		self.BG_COLOR = 150, 150, 80
		self.window = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT)) 
		pygame.display.set_caption('Raspberrula')
		self.screen = pygame.display.get_surface()
		self.rasp = "../images/Raspberrula.jpg"
		self.rasp_surface = pygame.image.load(self.rasp)
		self.rasp_surface = pygame.transform.scale(self.rasp_surface, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
		self.screen.blit(self.rasp_surface, (0,0))
		self.rasp = MoveRasp(self.window,	\
				self.RASP_FILENAME,	\
				(self.SCREEN_WIDTH / 2,	\
				self.SCREEN_HEIGHT / 2),	\
				(1, 1),	\
				5,
				self.devices)
		# init portals
		i = 0
		for device in self.devices.my_list:
			portal_coord = device.get_portal_coord()
			self.portals.append(DrawPortal(self.window,
						"portal.png",
						portal_coord,
						))
	
	def run(self):
		self.screen.blit(self.rasp_surface, (0,0))
		self.rasp.blitme()
		for portal in self.portals:
			portal.blitme()
		pygame.display.update()
		while True:
			self.screen.blit(self.rasp_surface, (0,0))
			#self.window.fill(self.BG_COLOR)
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
						easygui.msgbox(self.rasp.portal_collision[1].get_info(), title=self.rasp.portal_collision[1].get_name())