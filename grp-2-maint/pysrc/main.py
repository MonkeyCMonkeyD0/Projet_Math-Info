from tools.axis.Axis import Axis
from tools.cnds_initials.Initials import Initials
from tools.line_style_form.Color import Color
from tools.line_style_form.Form import Form
from tools.line_style_form.LineStyle import LineStyle
from tools.phase_diag.PhaseDiag import PhaseDiag
import numpy as np
from mdl.model2 import Model2


def main():

	k = 100
	l = 1000
	# a = (k+np.sqrt(k*k-l))/(2*l) + 0.1
	a = k/l

	# -- Le modele
	args = {"alpha": a, "k": k, "l": l}
	mdl = Model2(title = "Model 2", args = args)

	# -- Les axes
	xaxis = Axis(label = "x", inf = -100, sup = 1000, nbpts = 50)
	yaxis = Axis(label = "y", inf = -100, sup = 1000, nbpts = 50)
	taxis = Axis(inf = -100000, sup = 100000, nbpts = 10000000)

	# -- Couleurs et formes
	col = Color()
	frm = Form()
	red_solid = LineStyle(color = col.red())
	blue_dashdot = LineStyle(color = col.blue(), form = frm.dash_dot())
	black_dash = LineStyle(color = col.black(), form = frm.dashed())
	
	# -- Conditions initiales
	cnds = []
	cnds = Initials(Lx = [0], Ly = [0], style = black_dash)
	# cnds.append(coord = (0, l), style = blue_dashdot)
	# cnds.append(coord = (k, 0), style = blue_dashdot)

	x = (1 + np.sqrt(1 + 4*a*(a*l-k)))/(2*a)
	y = k/a - (1 + np.sqrt(1 + 4*a*(a*l-k)))/(2*a*a)
	print(x,y)
	cnds.append(coord = (x, y), style = black_dash)

	x = (1 - np.sqrt(1 + 4*a*(a*l-k)))/(2*a)
	y = k/a - (1 - np.sqrt(1 + 4*a*(a*l-k)))/(2*a*a)
	print(x,y)
	cnds.append(coord = (x, y), style = black_dash)

	# x = l/(k + np.sqrt(k*k - l))
	# y = l - x*x
	# print(x,y)
	# cnds.append(coord = (x, y), style = black_dash)

	# -- Portrait des phases
	phases = PhaseDiag(title = mdl.title)
	phases.portrait(modl = mdl, xaxis = xaxis, yaxis = yaxis, taxis = taxis, listcnd = cnds, exportpng = True) 

if __name__ == '__main__':
	main()