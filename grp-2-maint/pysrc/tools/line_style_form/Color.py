class Color:
	""" La classe Color : pour la gestion de la couleur d’une trajectoire. """

	def __init__(self):
		self._colors = {
			"blue": "b",
			"red": "r",
			"black": "k",
			"cyan": "c",
			"green": "g",
			"magenta": "m",
			"yellow": "y"
		}

	# --- Public functions
	def blue(self):
		return self._colors["blue"]

	def red(self):
		return self._colors["red"]

	def black(self):
		return self._colors["black"]

	def cyan(self):
		return self._colors["cyan"]

	def green(self):
		return self._colors["green"]

	def magenta(self):
		return self._colors["magenta"]

	def yellow(self):
		return self._colors["yellow"]
