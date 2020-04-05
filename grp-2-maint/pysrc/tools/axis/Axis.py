from numpy import linspace

class Axis:
	""" La classe Axis : pour la gestion des axes. """

	def __init__(self, inf, sup, label = "", nbpts = 50):
		self._label = label
		self._inf = inf
		self._sup = sup
		self._nbpts = nbpts

	def __str__(self):
		msg = " Axis = {} : inf = {}, sup = {} avec {} points"
		msg = msg.format(self.label, self.inf, self.sup, self.nbpts)
		return msg

	# --- Getters & Setters
	@property
	def label(self):
		return self._label

	@label.setter
	def label(self,label):
		self._label = label

	@property
	def inf(self):
		return self._inf

	@inf.setter
	def inf(self,inf):
		self._inf = inf

	@property
	def sup(self):
		return self._sup

	@sup.setter
	def sup(self,sup):
		self._sup = sup

	@property
	def nbpts(self):
		return self._nbpts

	@nbpts.setter
	def nbpts(self,nbpts):
		self._nbpts = nbpts

	# --- Public functions
	def interval(self):
		return linspace(start = self.inf, stop = self.sup, num = self.nbpts)

	def interval_passe(self):
		return linspace(start = 0, stop = self.inf, num = self.nbpts)

	def interval_futur(self):
		return linspace(start = 0, stop = self.sup, num = self.nbpts)
