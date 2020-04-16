from mdl.AutonomSys import AutonomSys

class SysLine(AutonomSys):
	""" La classe SysLine : pour la gestion d'un modèle linéaire en exemple. """

	@staticmethod
	def system(z, t, args):
		x, y = z[:2]
		dxdt = args["a11"] * x + args["a12"] * y
		dydt = args["a21"] * x + args["a22"] * y
		return [ dxdt , dydt ]
