from .utils.libs import *
from .utils.types import (
FUNC_WHILE_RUNNING,
)

class Camera:
	def __init__(self):
		self.functions[FUNC_WHILE_RUNNING].append(self.camera_move)
		self.camera_settings = self.settings.camera_settings


	
	def camera_move(self):
		keys = self.get_key_pressed()
		if keys[pygame.K_a]:
			glTranslatef(self.camera_settings.speed, 0, 0)
		elif keys[pygame.K_d]:
			glTranslatef(-self.camera_settings.speed, 0, 0)
		elif keys[pygame.K_LSHIFT]:
			glTranslatef(0, self.camera_settings.speed, 0)
		elif keys[pygame.K_SPACE]:
			glTranslatef(0, -self.camera_settings.speed, 0)
		elif keys[pygame.K_w]:
			glTranslatef(0, 0, self.camera_settings.speed)
		elif keys[pygame.K_s]:
			glTranslatef(0, 0, -self.camera_settings.speed)

		if keys[pygame.K_UP]:
			glRotatef(self.camera_settings.speed, 2, 0, 0)
		elif keys[pygame.K_DOWN]:
			glRotatef(-self.camera_settings.speed, 2, 0, 0)
		if keys[pygame.K_LEFT]:
			glRotatef(self.camera_settings.speed, 0, 2, 0)
		elif keys[pygame.K_RIGHT]:
			glRotatef(-self.camera_settings.speed, 0, 2, 0)