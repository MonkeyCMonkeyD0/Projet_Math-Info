from tools.cnds_initials.Initial import Initial

class Initials:
	""" La classe Initials : pour la gestion des conditions initiales, c’est un conteneur. """

	def __init__(self, Lx = [], Ly = [], style = "b-"):
		self._list_initial = []
		for x in Lx:
			for y in Ly:
				self._list_initial.append(Initial(coord = (x, y), style = style))

	def __str__(self):
		msg = " List of Initials :\n"
		for init in self.list_initial:
			msg += init.__str__() + "\n"
		return msg

	# --- Getters & Setters
	@property
	def list_initial(self):
		return self._list_initial

	@list_initial.setter
	def list_initial(self, new_list):
		self._list_initial = new_list

	@property
	def list_initial_at(self, num):
		return self._list_initial[num]

	@list_initial.setter
	def list_initial_at(self, num, new_initial):
		self._list_initial[i] = new_initial

	# --- Public functions
	def append(self, new_initial):
		self._list_initial.append(new_initial)

	def append(self, coord, style = "b-"):
		self._list_initial.append(Initial(coord = coord, style = style))

	@classmethod
	def build_from_axis(cls, axis):
		listcnd = Initials()
		nb = axis.nbpts
		axis.nbpts = 5
		inter = axis.interval()
		for xx in inter:
			for yy in inter:
				listcnd.append(coord = (xx, yy))
		axis.nbpts = nb
		return listcnd
		