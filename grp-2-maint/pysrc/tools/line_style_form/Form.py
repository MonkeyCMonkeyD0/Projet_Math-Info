class Form:
	""" La classe Form : pour la gestion de la forme d’une ligne. """

	def __init__(self):
		self._forms = {
			"solid" : "-",
			"dashed" : "--",
			"dotted" : ":",
			"dash_dot" : "-.",
			"invisible" : ""
		}

	# --- Public functions
	def solid(self):
		return self._forms["solid"]

	def dashed(self):
		return self._forms["dashed"]

	def dotted(self):
		return self._forms["dotted"]

	def dash_dot(self):
		return self._forms["dash_dot"]

	def invisble(self):
		return self._forms["invisble"]
