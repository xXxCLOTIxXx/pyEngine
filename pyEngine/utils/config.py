import pygame
import math
from time import sleep as s
from os import system as shell
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
pygame.init()
shell("cls||clear")

__version__ = "1.0"

class _screen_settings:
	monitor_info = pygame.display.Info()
	FULL_WIDTH: int = monitor_info.current_w
	FULL_HEIGHT: int = monitor_info.current_h
	WINDOWED_WIDTH: int = FULL_WIDTH - FULL_WIDTH/3
	WINDOWED_HEIGHT: int = FULL_HEIGHT - FULL_HEIGHT/3
	size: tuple = (FULL_WIDTH, FULL_HEIGHT)
	title: str = f"pyEngine {__version__}"
	mouse_set_visible: bool = False
	run: bool = True
	full_screen = True
	FPS: int = 60
	static_icon = "pyEngine/static/icon.png"

screen_settings = _screen_settings()