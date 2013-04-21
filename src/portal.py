# Raspberrula Game - Raspberry Hack

import os
import sys
import pygame
from random import randint, choice
from math import sin, cos, radians
from pygame.sprite import Sprite
from vec2d import vec2d

class DrawPortal(Sprite):
        """ 
			Class that implements draw functionality for Info RaspBears
        """
        def __init__(
                self, screen, img_filename, init_position):

                Sprite.__init__(self)
                self.collision = 0
                self.screen = screen
                self.base_image = pygame.image.load(img_filename).convert_alpha()
		self.size = (self.base_image.get_width(), self.base_image.get_height())
                self.base_image = pygame.transform.scale(self.base_image, self.size)
                self.image = self.base_image

      	 	 # base image holds the original image, positioned to
       		 # angle 0.

                self.pos = vec2d(init_position)

	def blitme(self):
                self.screen.blit(self.image, self.pos);


