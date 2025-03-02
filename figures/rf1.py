import numpy as np
from pyx import canvas, color, deco, path, style, text, trafo, unit

data = [(0, 0.420844), (0.250965, 0.626649), (0.501931, 0.668865), (0.752896, 0.721636),
        (1.00386, 0.746702), (1.25483, 0.78628), (1.50579, 0.721636), (1.75676, 0.639842),
        (1.99807, 0.51715), (2.25869, 0.476253), (2.5, 0.287599), (2.74131, 0.257256),
        (3.00193, 0.203166), (3.24324, 0.167546), (3.49421, 0.167546), (3.74517, 0.242744),
        (3.99614, 0.33905), (4.2471, 0.418206), (4.49807, 0.585752), (4.74903, 0.646438),
        (5, 0.71372), (5.25097, 0.80343), (5.50193, 0.790237), (5.7529, 0.693931),
        (6.00386, 0.663588), (6.25483, 0.550132), (6.49614, 0.496042), (6.75676, 0.365435),
        (6.98842, 0.217678), (7.24903, 0.245383), (7.50965, 0.17942), (7.74131, 0.212401),
        (7.99228, 0.313984), (8.24324, 0.41029), (8.49421, 0.473615), (8.74517, 0.572559),
        (8.99614, 0.686016), (9.2471, 0.734828), (9.49807, 0.78496), (9.74903, 0.734828),
        (10, 0.75066)]

unit.set(wscale=1.3, xscale=0.9)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")

c = canvas.canvas()
x = np.linspace(0, 10, 200)
y = (391.5-(98+321)/2+(321-98)/2*np.cos(4*np.pi*(518/10*x+75-130)/445))/379
factor_x = 0.64
factor_y = 4
p = path.path(path.moveto(x[0]*factor_x, y[0]*factor_y))
for xp, yp in zip(x[1:], y[1:]):
    p.append(path.lineto(xp*factor_x, yp*factor_y))
c.stroke(p, [color.grey(0.7)])
c.stroke(path.rect(0, 0, 6.4, 4))
d = 0.1
for x, y in data:
    c.stroke(path.rect(x*factor_x-d/2, y*factor_y-d/2, d, d),
             [style.linewidth(style._defaultlinewidth*0.8)])

c.text(3.2, -0.2, "Frequenzdifferenz", [text.halign.center, text.valign.top])
for yval, label in ((0, '0'), (4, '1')):
    c.stroke(path.line(0, yval, -0.1, yval))
    c.text(-0.2, yval, label, [text.halign.right, text.valign.middle])
c.text(-0.6, 2, "Anteil im unteren Zustand", [text.halign.center, trafo.rotate(90)])
c.writePDFfile()
