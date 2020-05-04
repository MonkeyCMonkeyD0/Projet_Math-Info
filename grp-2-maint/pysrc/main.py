from tools.axis.Axis import Axis
from tools.cnds_initials.Initials import Initials
from tools.line_style_form.Color import Color
from tools.line_style_form.Form import Form
from tools.line_style_form.LineStyle import LineStyle
from tools.phase_diag.PhaseDiag import PhaseDiag
from mdl.ModelSelectionNaturelle import ModelSelectionNaturelle

import numpy as np


def main():

	k = 60
	l = 60
	a = 0.5

	# -- Le modele
	args = {"alpha": a, "k": k, "l": l}
	mdl = ModelSelectionNaturelle(title = "Modèle Selection Naturelle", args = args)

	# -- Les axes
	xaxis = Axis(label = "x", inf = 0, sup = 100, nbpts = 50)
	yaxis = Axis(label = "y", inf = 0, sup = 100, nbpts = 50)
	taxis = Axis(inf = 0, sup = 100000, nbpts = 10000000)

	# -- Couleurs et formes
	col = Color()
	frm = Form()
	red_solid = LineStyle(color = col.red())
	blue_dashdot = LineStyle(color = col.blue(), form = frm.dash_dot())
	black_dash = LineStyle(color = col.black(), form = frm.dashed())
	
	# -- Conditions initiales
	cnds = Initials(Lx = [10], Ly = [120], style = black_dash)
	cnds.append(coord = (20, 200), style = blue_dashdot)
	cnds.append(coord = (50, 100), style = red_solid)
	
	# x = (1 + np.sqrt(1 + 4*a*(a*l-k)))/(2*a)
	# y = k/a - (1 + np.sqrt(1 + 4*a*(a*l-k)))/(2*a*a)
	# print(x,y)
	# cnds.append(coord = (x, y), style = black_dash)

	# x = (1 - np.sqrt(1 + 4*a*(a*l-k)))/(2*a)
	# y = k/a - (1 - np.sqrt(1 + 4*a*(a*l-k)))/(2*a*a)
	# print(x,y)
	# cnds.append(coord = (x, y), style = black_dash)

	# x = l/(k + np.sqrt(k*k - l))
	# y = l - x*x
	# print(x,y)
	# cnds.append(coord = (x, y), style = black_dash)

	# -- Portrait des phases
	phases=PhaseDiag(title = mdl.title)
	phases.portrait(modl = mdl, xaxis = xaxis, yaxis = yaxis, taxis = taxis, listcnd = cnds, exportpng = True) 

if __name__ == '__main__':
	main()