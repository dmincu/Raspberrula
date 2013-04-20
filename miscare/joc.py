import pygame,os,sys
from pygame.locals import *
from creeps_try import MoveRasp

pygame.init()
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 486
RASP_FILENAME = "rasp.png"
BG_COLOR = 150, 150, 80
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption('Raspberrula')
screen = pygame.display.get_surface()
rasp = os.path.join("data","rasp.jpg")
rasp_surface = pygame.image.load(rasp)
screen.blit(rasp_surface, (0,0))

rasp = MoveRasp(window,
		RASP_FILENAME,
		(SCREEN_WIDTH / 2,
		SCREEN_HEIGHT / 2),
		(1, 1),
		1)


def input(events):
	for event in events:
		if event.type == QUIT:
			sys.exit(0)
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				rasp.move_up()
				print event
			elif event.key == pygame.K_DOWN:
				rasp.move_down()
				print event
			elif event.key == pygame.K_LEFT:
				rasp.move_left()
				print event
			elif event.key == pygame.K_RIGHT:
				rasp.move_right()
				print event

while True:
	screen.blit(rasp_surface, (0,0))
	#window.fill(BG_COLOR)
	input(pygame.event.get())
	rasp.blitme()
	pygame.display.flip()


