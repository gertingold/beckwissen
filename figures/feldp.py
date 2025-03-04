from math import sqrt
import numpy as np
from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.9)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()
c.stroke(path.path(path.moveto(4.5, 0),
                   path.lineto(0, 0),
                   path.lineto(0, 4.5)), [deco.barrow, deco.earrow])
c.text(4.5, -0.2, "elektrisches Feld", [text.halign.right, text.valign.top])
c.stroke(path.path(path.arc(0, 0, 2*sqrt(2), 10, 80)), [deco.barrow])
c.stroke(path.line(2, 2, 2, 0), [style.linestyle.dashed])

rng = np.random.default_rng()
data = rng.multivariate_normal(mean=[0, 0], cov=[[0.04, 0], [0, 0.04]], size=(20000,))
for x, y in zip(data[:, 0], data[:, 1]):
    c.fill(path.circle(x+2, y+2, 0.003))

c.writePDFfile()
