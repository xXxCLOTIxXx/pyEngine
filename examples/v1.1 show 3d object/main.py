from pyEngine.utils.libs import *
from pyEngine import Engine, Settings
from pyEngine.utils.types import FUNC_BEFORE_RUNNING, ON_CHANGE_DISPLAY_MODE
from pyEngine import get_object_from_file




objects = get_object_from_file("test.obj")

settings = Settings(title="example 3d", debug=True)
engine = Engine(settings, use_camera=True)

@engine.register_function(FUNC_BEFORE_RUNNING)
def visual_settings():
	gluPerspective(600, (engine.settings.screen_settings.size[0]/engine.settings.screen_settings.size[1]), 0.1, 50.0)
	glTranslatef(0.0, 0.0, -5)
	glRotatef(0, 0, 0, 0)


@engine.register_function(ON_CHANGE_DISPLAY_MODE)
def change_visual_settings(full_screen: bool, size: tuple):
	if full_screen:
		glTranslatef(0.0, 0.0, 0)
	else:
		glTranslatef(0.0, 0.0, 0)


@engine.register_function()
def show_cube():
	glBegin(GL_LINES)
	glColor3f(0.0, 1.0, 0.0)
	for obj in objects:
		glVertex3fv(obj)
	glEnd()


if __name__ == "__main__":
	engine.run()