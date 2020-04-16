from mdl.AutonomSys import AutonomSys

class SysNLine(AutonomSys):
	""" La classe SysNLine : pour la gestion d'un modèle non linéaire en exemple. """

	@staticmethod
	def system(z, t, **args):
		x, y = z[:2]
		dxdt = x
		dydt = x**2 + y**2 - 1
		return [ dxdt , dydt ]
