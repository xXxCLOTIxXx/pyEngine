from pyEngine import Engine
from pyEngine.utils.config import *
from pyEngine.utils.types import FUNC_BEFORE_RUNNING, ON_CHANGE_DISPLAY_MODE

engine = Engine(debug=True)

@engine.register_function(FUNC_BEFORE_RUNNING)
def visual_settings():
	gluPerspective(45, (screen_settings.size[0]/screen_settings.size[1]), 0.1, 50.0)
	glTranslatef(0.0, 0.0, -5)
	glRotatef(0, 0, 0, 0)


@engine.register_function(ON_CHANGE_DISPLAY_MODE)
def change_visual_settings(full_screen: bool, size: tuple):
	if full_screen:
		glTranslatef(0.0, 0.0, -5)
	else:
		glTranslatef(0.0, 0.0, 5)




@engine.register_function()
def show_cube():
	verts = (
		(1, -1, -1),
		(1, 1, -1),
		(-1, 1, -1),
		(-1, -1, -1),
		(1, -1, 1),
		(1, 1, 1),
		(-1,-1,1),
		(-1, 1, 1),
	)
	edges = (
		(0, 1),
		(0, 3),
		(0, 4),
		(2, 1),
		(2, 3),
		(2, 7),
		(6, 3),
		(6, 4),
		(6, 7),
		(5, 1),
		(5, 4),
		(5, 7),
	)

	surf = (
		
	)

	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(verts[vertex])

	glEnd()



if __name__ == "__main__":
	engine.run()