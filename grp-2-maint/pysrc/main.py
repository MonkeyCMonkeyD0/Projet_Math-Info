from tools.axis.Axis import Axis
from tools.cnds_initials.Initials import Initials
from tools.line_style_form.Color import Color
from tools.line_style_form.Form import Form
from tools.line_style_form.LineStyle import LineStyle
from tools.phase_diag.PhaseDiag import PhaseDiag

from mdl.model2 import Model2


def main():

	alpha = 1
	k = 1
	l = 1
	args = {"alpha": alpha, "k": k, "l": l}

	# -- Le modele
	mdl = Model2(title = "Model 2", args = args)

	# -- Les axes
	xaxis = Axis(label = "x", inf = 0, sup = 1.5, nbpts = 10)
	yaxis = Axis(label = "y", inf = 0, sup = 1.5, nbpts = 10)
	taxis = Axis(inf = -10, sup = 50, nbpts = 1000)

	# -- Couleurs et formes
	col = Color()
	frm = Form()
	red_solid = LineStyle(color = col.red())
	blue_dashdot = LineStyle(color = col.blue(), form = frm.dash_dot())

	# -- Conditions initiales
	# cnds = Initials(Lx = [2.0], Ly = [1.0, 2.0], style = red_solid)
	# cnds.append(coord = (1.5, 0.5), style = blue_dashdot)
	# cnds.append(coord = (2.5, 3), style = blue_dashdot)

	# -- Portrait des phases
	phases = PhaseDiag(title = mdl.title)
	phases.portrait(modl = mdl, xaxis = xaxis, yaxis = yaxis, taxis = taxis, exportpng = True)	#listcnd = cnds, 

if __name__ == '__main__':
	main()