import pygame,os,sys
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((650, 486)) 
pygame.display.set_caption('Raspberrula')
screen = pygame.display.get_surface()
rasp = os.path.join("data","rasp.jpg");
rasp_surface = pygame.image.load(rasp)
screen.blit(rasp_surface, (0,0))
pygame.display.flip()

def input(events): 
   for event in events: 
      if event.type == QUIT: 
         sys.exit(0) 
      else: 
         print event 
 
while True: 
   input(pygame.event.get())
