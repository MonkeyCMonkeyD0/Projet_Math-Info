from functools import partial


class AutonomSys:
	""" La classe mère (ou base) AutonomSys : pour la gestion des modèles. """

	def __init__(self, title, args = {}):
		self._args = args
		self._title = title

	def __str__(self):
		msg = " System = {} :".format(self.title)
		for key, arg in self.args:
			msg += " {} = {}".format(key, arg)
		return msg

	@staticmethod
	def system(z, t, args):
		raise NotImplementedError("Override this methode to set up your system first.")

	# --- Getters & Setters
	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, new_title):
		self._title = new_title

	@property
	def args(self):
		return self._args

	@args.setter
	def args(self, args):
		self._args = args

	# --- Private functions
	def _rhs(self, z, t):
		return self.system(z = z, t = t, args = self.args)

	# --- Public functions
	def rhs(self):
		funct = partial(self._rhs)
		funct.__doc__ = "Return the system from class {}.".format(type(self).__name__)
		return funct

	def field(self, x, y):
		return self.system(z = [x, y], t = 0, args = self.args)
