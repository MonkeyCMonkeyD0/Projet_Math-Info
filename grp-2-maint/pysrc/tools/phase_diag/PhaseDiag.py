import matplotlib.pyplot as plt
from scipy.integrate import odeint

from tools.cnds_initials.Initials import Initials
from tools.field.Field import Field


class PhaseDiag:
	""" La classe PhaseDiag : pour la gestion du portrait des phases d’un système autonome. """

	def __init__(self, title = "Portrait des phases", figsize = (10, 6)):
		self._title = title
		self._figsize = figsize

	def __str__(self):
		msg = " PhaseDiag = {} : largeur = {} longueur = {}"
		msg = msg.format(self.title, self.figsize[0], self.figsize[1])
		return msg

	# --- Getters & Setters
	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, new_title):
		self._title = new_title

	@property
	def figsize(self):
		return self._figsize

	@figsize.setter
	def figsize(self, *new_figsize):
		self._figsize = new_figsize

	# --- Public functions
	def portrait(self, modl, xaxis, yaxis, taxis, listcnd = [], exportpng = False, showfield = True):
		# -- Preparer graphique
		fig, phases = plt.subplots(figsize = self.figsize)

		# -- Parametrage graphique globaux
		plt.xlim(xaxis.inf, xaxis.sup)
		plt.ylim(yaxis.inf, yaxis.sup)

		# -- Parametrage repere
		phases.grid(True)
		plot_title = self.title + " avec :"
		for key, arg in modl.args.items():
			plot_title += " {} = {},".format(key, arg)
		phases.set_title(plot_title)
		phases.set(xlabel = xaxis.label, ylabel = yaxis.label)

		# -- Champ des gradients
		if showfield:
			field = Field()
			field.plot(modl = modl, xaxis = xaxis, yaxis = yaxis)

		# -- Calcul des trajectoires
		tdisc_passe = taxis.interval_passe()
		tdisc_futur = taxis.interval_futur()

		if not listcnd:
			listcnd = Initials.build_from_axis(axis = xaxis)

		cndszero = listcnd.list_initial
		for cnd in cndszero:
			cnd0 = cnd.coord
			trj = odeint(func = modl.rhs(), y0 = cnd0, t = tdisc_passe, mxhnil = 1)
			phases.plot(trj[:,0], trj[:,1], cnd.style)
			trj = odeint(func = modl.rhs(), y0 = cnd0, t = tdisc_futur, mxhnil = 1)
			phases.plot(trj[:,0], trj[:,1], cnd.style)
			#phases.plot(tdisc_futur, trj[:,0], cnd.style)
			del trj
		
		plt.show()

		if exportpng:
			figname = "img/" + self.title + ".png"
			figname = figname.replace(" ", "_")
			print("File saved as", figname, "in pysrc/")
			fig.savefig(fname = figname)
