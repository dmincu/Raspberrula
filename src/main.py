import pygame, sys
from pygame.locals import *

width = 800
height = 600

if __name__ == "__main__":
	pygame.init()

	fpsClock = pygame.time.Clock()
	size = (width, height)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Raspberrula")
	backgroundImg = pygame.image.load("../Images/Raspberrula.Intro.Scaled.jpg").convert()
	backgroundImg = pygame.transform.scale(backgroundImg, (width, height))	
	backgroundRect = backgroundImg.get_rect()	

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
		screen.blit(backgroundImg, backgroundRect)
		pygame.display.update()



