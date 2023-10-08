from .utils.config import *
from .screen import Screen
from datetime import datetime
from .utils.exception import FunctionTypeError
from .utils.types import (
__all__,
FUNC_BEFORE_RUNNING,
FUNC_WHILE_RUNNING,
ON_QUIT_PROGRAM,
ON_CHANGE_DISPLAY_MODE
)

class Engine(Screen):
	functions = dict()
	def __init__(self, size: tuple = screen_settings.size, icon: str = screen_settings.static_icon, title: str = screen_settings.title, debug: bool = False):
		self.debug = debug
		Screen.__init__(self, size, icon, title)
		for i in __all__:
			self.functions[i]=list()
		

	def log(self, text: str, prefix: str = None):
		print(f"{datetime.now()} {f'[{prefix}] ' if prefix else ''}{text}")



	def set_background_color()


	def register_function(self, type: str = FUNC_WHILE_RUNNING):
		def register(function):
			if type in self.functions:self.functions[type].append(function)
			else:raise FunctionTypeError(type)
			return function
		return register


	def built_in_events(self):
		keys = self.get_key_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				for func in self.functions[ON_QUIT_PROGRAM]:func()
				screen_settings.run=False
				pygame.quit()
				exit()
			if keys[pygame.K_F11]:
				for func in self.functions[ON_CHANGE_DISPLAY_MODE]:func(screen_settings.full_screen, screen_settings.size)
				self.on_chage_display_mode()



	def main_loop(self):
		for func in self.functions[FUNC_BEFORE_RUNNING]:func()
		while screen_settings.run:
			self.built_in_events()
			glClear(GL_COLOR_BUFFER_BIT)
			for func in self.functions[FUNC_WHILE_RUNNING]:func()
			pygame.display.flip()
			self.clock.tick(screen_settings.FPS)


	def run(self):
		self.main_loop()