# Raspberrula Game - Raspberry Hack

class MoveRasp(Sprite):
	""" A raspberry controlled by pointing arrows
	"""
	def __init__(
		self, screen, img_filename, init_position,
		init_direction, speed):
	""" Create the raspberry
	
	screen:
                The screen on which the creep lives (must be a
                pygame Surface object, such as pygame.display)
            
        img_filaneme:
                Image file for the creep.
            
	init_position:
                A vec2d or a pair specifying the initial position
                of the creep on the screen.
            
	init_direction:
                A vec2d or a pair specifying the initial direction^M
                of the creep. Must have an angle that is a 
                multiple of 45 degres.
            
	speed: 
                Creep speed, in pixels/millisecond (px/ms)
	"""
	
	Sprite.__init__(self)
	self.screen = screen
	self.speed = speed
	self.base_image = pygame.image.load(img_filename).convert_alpha()
	self.image = self.base_image

	# base image holds the original image, positioned to
	# angle 0.
	
	self.pos = ve2d(init_direction).normalized()

	
