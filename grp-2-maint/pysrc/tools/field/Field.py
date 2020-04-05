import pylab as pl
import numpy as np


class Field:
	""" La classe Field : pour la gestion du champ des gradients. """

	def __init__(self, color = "g"):
		self._color = color

	def __str__(self):
		msg = " Field : color = {}"
		msg = msg.format(self.color)
		return msg

	# --- Getters & Setters
	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, color):
		self._color = color

	# --- Public functions
	def plot(self, modl, xaxis, yaxis):
		xgrid, ygrid = np.mgrid[xaxis.inf:xaxis.sup:xaxis.nbpts*1j, yaxis.inf:yaxis.sup:yaxis.nbpts*1j]
		xfield, yfield = modl.field(x = xgrid, y = ygrid)
		return pl.quiver(xgrid, ygrid, xfield, yfield, color = self.color)
