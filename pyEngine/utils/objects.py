from .libs import pygame
from .info import __name__, __ver__

class Settings:
	debug = False


	class temp_variables:
		full_screen: bool = True
		run: bool = True
		mouse_set_visible: bool = False


	class screen_settings:
		monitor_info = pygame.display.Info()
		FULL_WIDTH: int = monitor_info.current_w
		FULL_HEIGHT: int = monitor_info.current_h
		WINDOWED_WIDTH: int = FULL_WIDTH - FULL_WIDTH/3
		WINDOWED_HEIGHT: int = FULL_HEIGHT - FULL_HEIGHT/3
		size: tuple = (FULL_WIDTH, FULL_HEIGHT)
		title: str = f"{__name__} {__ver__}"
		FPS: int = 60
		icon = "pyEngine/static/icon.png"

	class camera_settings:
		speed: float = 0.6



	def __init__(
		self,
		title: str = None,
		icon: str = None,
		FPS_MAX: str = None,
		debug: bool = False
		):
		self.debug = debug

		if title: self.screen_settings.title = title
		if icon: self.screen_settings.icon = icon
		if FPS_MAX: self.screen_settings.FPS = FPS_MAX