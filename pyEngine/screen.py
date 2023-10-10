from .utils.libs import pygame



class Keyboard:
	def get_key_pressed(self):
		return pygame.key.get_pressed()


class Screen(Keyboard):
	def __init__(self):
		Keyboard.__init__(self)
		self.screen=pygame.display.set_mode(self.settings.screen_settings.size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.FULLSCREEN)
		self.clock = pygame.time.Clock()
		pygame.display.set_caption(self.settings.screen_settings.title)
		pygame.display.set_icon(pygame.image.load(self.settings.screen_settings.icon))
		pygame.mouse.set_visible(False)



	def on_chage_display_mode(self):
		if self.settings.temp_variables.full_screen:
			self.settings.screen_settings.size=(self.settings.screen_settings.WINDOWED_WIDTH, self.settings.screen_settings.WINDOWED_HEIGHT)
			self.settings.temp_variables.full_screen = False
			pygame.display.set_mode(self.settings.screen_settings.size, pygame.DOUBLEBUF | pygame.OPENGL)
		else:
			self.settings.screen_settings.size=(self.settings.screen_settings.FULL_WIDTH, self.settings.screen_settings.FULL_HEIGHT)
			self.settings.temp_variables.full_screen = True
			pygame.display.set_mode(self.settings.screen_settings.size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.FULLSCREEN)
		if self.settings.debug:self.log(prefix="SCREEN MODE", text=f"Screen mode changed to {'full screen' if self.settings.temp_variables.full_screen else 'windowed'} {self.settings.screen_settings.size}")