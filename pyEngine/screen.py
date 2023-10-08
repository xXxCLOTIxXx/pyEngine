from .utils.config import *

class Keyboard:
	def get_key_pressed(self):
		return pygame.key.get_pressed()


class Screen(Keyboard):
	def __init__(self, size: tuple, icon: str, title: str):
		Keyboard.__init__(self)
		self.size = size
		self.screen=pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.FULLSCREEN)
		self.clock = pygame.time.Clock()
		pygame.display.set_caption(title)
		pygame.display.set_icon(pygame.image.load(icon))
		#pygame.mouse.set_visible(False)



	def on_chage_display_mode(self):
		if screen_settings.full_screen:
			screen_settings.size=(screen_settings.WINDOWED_WIDTH, screen_settings.WINDOWED_HEIGHT)
			screen_settings.full_screen = False
			pygame.display.set_mode(screen_settings.size, pygame.DOUBLEBUF | pygame.OPENGL)
		else:
			screen_settings.size=(screen_settings.FULL_WIDTH, screen_settings.FULL_HEIGHT)
			screen_settings.full_screen = True
			pygame.display.set_mode(screen_settings.size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.FULLSCREEN)
		if self.debug:self.log(prefix="SCREEN MODE", text=f"Screen mode changed to {'full screen' if screen_settings.full_screen else 'windowed'} {screen_settings.size}")