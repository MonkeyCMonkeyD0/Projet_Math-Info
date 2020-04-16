from modls.AutonomSys import AutonomSys

class LotkaVolterra_2(AutonomSys):
	""" La classe LotkaVolterra : pour la gestion du modèle Lotka-Volterra. """

	@staticmethod
	def system(z, t, **args):
		x, y = z[:2]
		dxdt = x * ((x - args["epsilon"]) * (1 - x / args["kappa"]) / (x + args["epsilon"]) - y)
		dydt = y * (x - 1)
		return [ dxdt , dydt ]