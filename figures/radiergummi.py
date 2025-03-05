from math import sqrt
import numpy as np
from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.85)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()
c.stroke(path.line(0, 0, 2, 0), [deco.earrow, style.linestyle.dashed])
c.stroke(path.line(0, 0, 0, 2), [deco.earrow, style.linestyle.dashed])
c.stroke(path.path(path.moveto(sqrt(2), sqrt(2)),
                   path.lineto(0, 0),
                   path.lineto(sqrt(2), -sqrt(2))),
         [deco.barrow, deco.earrow, style.linejoin.round])
c.text(2, 0.2, 'Weg 1', [text.halign.right])
c.text(-0.1, 2.1, 'Weg 2')

for sign in (-1, 1):
    c.stroke(path.path(path.moveto(0.1+sqrt(2), sign*(0.3-sqrt(2))),
                       path.curveto(5.4, sign*(0.3-sqrt(2)), 0.4, -1.4*sign, 3.6, -1.4*sign)),
             [deco.earrow])

for y0 in (0.8, -2):
    c.stroke(path.path(path.moveto(7.4, y0),
                       path.lineto(3.9, y0),
                       path.lineto(3.9, y0+1.7)),
             [deco.barrow, deco.earrow])
    c.stroke(path.line(3.9, y0, 3.8, y0))
    c.text(3.7, y0, '0', [text.halign.right, text.valign.middle])
    c.stroke(path.line(3.9, y0+1.2, 3.8, y0+1.2))
    c.text(3.7, y0+1.2, '1', [text.halign.right, text.valign.middle])

x = np.linspace(0, 3.1, 100)
y = 0.6*(1+np.sin(2.9*x))
xshift = 3.9
yshift = -2
p = path.path(path.moveto(xshift+x[0], yshift+y[0]))
for xp, yp in zip(x[1:], y[1:]):
    p.append(path.lineto(xshift+xp, yshift+yp))
c.stroke(p)

y = 0.6*(1-np.sin(2.9*x))
xshift = 3.9
yshift = 0.8
p = path.path(path.moveto(xshift+x[0], yshift+y[0]))
for xp, yp in zip(x[1:], y[1:]):
    p.append(path.lineto(xshift+xp, yshift+yp))
c.stroke(p)

c.writePDFfile()
