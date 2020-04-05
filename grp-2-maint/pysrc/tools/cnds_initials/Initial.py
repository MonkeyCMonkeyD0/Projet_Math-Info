class Initial:
	""" La classe Initial : pour la gestion d’une condition initiale. """

	def __init__(self, coord, style = "k-"):
		self._coord = coord[:2]
		self._style = style

	def __str__(self):
		msg = " Initial : x(0) = {}, y(0) = {} printed in {}"
		msg = msg.format(self.coord[0], self.coord[1], self.style)
		return msg

	# --- Getters & Setters
	@property
	def coord(self):
		return self._coord

	@coord.setter
	def coord(self, coord):
		self._coord = coord

	@property
	def style(self):
		if isinstance(self._style, str):
			return self._style
		return self._style.line_style()

	@style.setter
	def style(self, style):
		self._style = style
