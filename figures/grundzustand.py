import numpy as np
from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.9)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()
c.stroke(path.line(0, 2, 4.5, 2), [deco.earrow])
c.text(4.5, 1.8, 'Ort', [text.halign.right, text.valign.top])
c.stroke(path.line(2, 0, 2, 4.5), [deco.earrow])
c.text(2.2, 4.5, 'Impuls', [text.valign.top])

rng = np.random.default_rng()
data = rng.normal(scale=0.4, size=(60000, 2))
for x, y in zip(data[:, 0], data[:, 1]):
    c.fill(path.circle(x+2, y+2, 0.004))

c.writePDFfile()
