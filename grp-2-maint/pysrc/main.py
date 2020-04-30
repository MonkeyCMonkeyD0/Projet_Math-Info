from tools.axis.Axis import Axis
from tools.cnds_initials.Initials import Initials
from tools.line_style_form.Color import Color
from tools.line_style_form.Form import Form
from tools.line_style_form.LineStyle import LineStyle
from tools.phase_diag.PhaseDiag import PhaseDiag

from mdl.model2 import Model2


def main():

	alpha = 0.5
	k = 100
	l = 100

	# -- Le modele
	args = {"alpha": alpha, "k": k, "l": l}
	mdl = Model2(title = "Model 2", args = args)

	# -- Les axes
	xaxis = Axis(label = "x", inf = 0, sup = 20, nbpts = 10)
	yaxis = Axis(label = "y", inf = 0, sup = 20, nbpts = 10)
	taxis = Axis(inf = -10, sup = 10, nbpts = 100)

	# -- Couleurs et formes
	col = Color()
	frm = Form()
	red_solid = LineStyle(color = col.red())
	blue_dashdot = LineStyle(color = col.blue(), form = frm.dash_dot())

	# -- Conditions initiales
	cnds = Initials(Lx = [0], Ly = [0], style = blue_dashdot)
	cnds.append(coord = (0, l), style = blue_dashdot)
	cnds.append(coord = (k, 0), style = blue_dashdot)

	# -- Portrait des phases
	phases = PhaseDiag(title = mdl.title)
	phases.portrait(modl = mdl, listcnd = cnds, xaxis = xaxis, yaxis = yaxis, taxis = taxis, exportpng = True)	

if __name__ == '__main__':
	main()