from .libs import np

def convert_object(vertex):
	objects = list()
	np_vertex =  np.array([np.array(v) for v in vertex])
	for obj in np_vertex:
		objects.append(list(obj)[0:3])
	return objects

def get_object_from_file(filename: str):
	vertex, faces = [], []
	with open(filename) as f:
		for line in f:
			if line.startswith('v '):
				vertex.append([float(i) for i in line.split()[1:]] + [1])
			elif line.startswith('f'):
				faces_ = line.split()[1:]
				faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
	return convert_object(vertex)
