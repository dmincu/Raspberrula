# Raspberrula Game - Raspberry Hack

import pygame, sys
from pygame.locals import *
import easygui
from info import *
from joc import *

width = 760
height = 570

if __name__ == "__main__":
	# Initialize pygame module	
	pygame.init()
	fpsClock = pygame.time.Clock()
	
	# Initialize background
	size = (width, height)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Raspberrula")
	backgroundImg = pygame.image.load("../images/Raspberrula Intro.jpg").convert()
	backgroundImg = pygame.transform.scale(backgroundImg, (width, height))	
	backgroundRect = backgroundImg.get_rect()	

	# Initialize components
	devices = Devices()
	devices.add_all_devices()

	# Initialize game
	game = Game()

	# Run Game
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
		screen.blit(backgroundImg, backgroundRect)
		pygame.display.update()
		pygame.time.delay(3000)

		#easygui.msgbox(devices.list[5].get_info(), title=devices.list[5].get_name())
		
		#TODO: go to game module
		game.run()
