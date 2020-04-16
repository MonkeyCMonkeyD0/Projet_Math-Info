from mdl.AutonomSys import AutonomSys

class Model2(AutonomSys):
	""" La classe SysNLine : pour la gestion d'un modèle non linéaire en exemple. """

	@staticmethod
	def system(z, t, args):
		x, y = z[:2]
		dxdt = x * (1 - (x + args["alpha"] * y) / args["k"])
		dydt = y * (1 - (y + x**2) / args["l"])
		return [ dxdt , dydt ]