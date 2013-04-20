import pygame, sys
from pygame.locals import *

width = 640
height = 480

if __name__ == "__main__":
	pygame.init()
	pygame.display.init()
	fpsClock = pygame.time.Clock()
	windowSurface = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Raspberrula")
	imgSurface = pygame.image.load('../Images/Raspberrula Intro.jpg');	
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()
