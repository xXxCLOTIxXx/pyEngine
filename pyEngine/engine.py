from .utils.libs import *
from .screen import Screen
from .camera import Camera
from datetime import datetime
from .utils.exception import FunctionTypeError
from .utils.objects import Settings
from .utils.types import (
__all__,
FUNC_BEFORE_RUNNING,
FUNC_WHILE_RUNNING,
ON_QUIT_PROGRAM,
ON_CHANGE_DISPLAY_MODE
)




class Engine(Screen, Camera):
	functions = dict()
	def __init__(self, settings: Settings = Settings(), use_camera: bool = False):
		self.settings = settings
		for i in __all__:
			self.functions[i]=list()

		Screen.__init__(self)
		if use_camera:Camera.__init__(self)
		

	def log(self, text: str, prefix: str = None):
		print(f"{datetime.now()} {f'[{prefix}] ' if prefix else ''}{text}")


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
				self.settings.temp_variables.run=False
				pygame.quit()
				exit()
			if keys[pygame.K_F11]:
				for func in self.functions[ON_CHANGE_DISPLAY_MODE]:func(self.settings.temp_variables.full_screen, self.settings.screen_settings.size)
				self.on_chage_display_mode()



	def main_loop(self):
		for func in self.functions[FUNC_BEFORE_RUNNING]:func()
		while self.settings.temp_variables.run:
			self.built_in_events()
			glClear(GL_COLOR_BUFFER_BIT)
			for func in self.functions[FUNC_WHILE_RUNNING]:func()
			pygame.display.flip()
			self.clock.tick(self.settings.screen_settings.FPS)


	def run(self):
		self.main_loop()