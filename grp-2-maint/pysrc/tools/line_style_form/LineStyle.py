class LineStyle:
	""" La classe LineStyle : pour la gestion du style graphique d’une trajectoire. """

	def __init__(self, color = "k", form = "-"):
		self._color = color
		self._form = form

	def __str__(self):
		msg = " LineStyle : color = {}, form = {}"
		msg = msg.format(self.color, self.form)
		return msg

	# --- Getters & Setters
	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, color):
		self._color = color

	@property
	def form(self):
		return self._form

	@form.setter
	def form(self, form):
		self._form = form

	# --- Public functions
	def line_style(self):
		return self.color + self.form
