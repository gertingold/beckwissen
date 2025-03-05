import numpy as np
from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.85)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()
c.fill(path.rect(0, 0, 2, 0.5), [color.grey(0.7)])
c.stroke(path.line(0, 0, 2, 0))
c.stroke(path.line(1, 0, 1.7, -2.5))
c.fill(path.circle(1.7, -2.5, 0.15))
c.text(0.1, 1, 'a', [text.size.Large])

shift = trafo.translate(3, -3)
c.stroke(path.line(0, 0, 6, 0), [deco.earrow, shift])
c.stroke(path.line(3, 0, 3, 4), [deco.earrow, shift])

x = np.linspace(-2.8, 2.8, 200)
y = 0.65*x*x
xshift = 3
factor_y = 2/3
p = path.path(path.moveto(x[0]+xshift, y[0]*factor_y))
for xp, yp in zip(x[1:], y[1:]):
    p.append(path.lineto(xp+xshift, yp*factor_y))
c.stroke(p, [shift])
c.text(6, -0.2, "Auslenkung", [shift, text.halign.right, text.valign.top])
c.text(3.2, 4, "Potential", [shift, text.valign.top])
c.text(3.1, 1, 'b', [text.size.Large])

c.writePDFfile()
