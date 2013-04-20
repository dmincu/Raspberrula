import pygame,os,sys
from pygame.locals import *
from creeps_try import MoveRasp


class Game:

	def __init__(self):
		pygame.init()
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
				10)

	def run(self):
		while True:
			self.screen.blit(self.rasp_surface, (0,0))
			#self.window.fill(self.BG_COLOR)
			self.input(pygame.event.get())
			self.rasp.blitme()
			pygame.display.update(Rect((self.rasp.pos.x - 10, self.rasp.pos.y - 10), (10, 10)))

	"""
	def input(self, events):
		for event in events:
			if event.type == QUIT:
				sys.exit(0)
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.rasp.move_up()
					print event
				elif event.key == pygame.K_DOWN:
					self.rasp.move_down()
					print event
				elif event.key == pygame.K_LEFT:	
					self.rasp.move_left()
					print event
				elif event.key == pygame.K_RIGHT:
					self.rasp.move_right()
					print event
	"""

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
				
