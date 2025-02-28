import numpy as np
from pyx import canvas, deco, path, style, text, trafo

text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()
c.stroke(path.path(path.moveto(6.4, 0),
                   path.lineto(0, 0),
                   path.lineto(0, 4.5)),
         [deco.barrow, deco.earrow])
c.text(6.4, -0.2, "Freqenz/Temperatur", [text.halign.right, text.valign.top])
c.text(-0.2, 4.5, "spektrale Intensität", [trafo.rotate(90), text.halign.right])

factor_x = 6.4/13.5
factor_y = 4/1.5
x1 = np.linspace(0.001, 12, 300)
y1 = x1**3/(np.exp(x1)-1)
x2 = np.linspace(0, 1.245, 100)
y2 = x2**2
p = path.path(path.moveto(x1[0], y1[0]))
for x, y in zip(x1[1:], y1[1:]):
    p.append(path.lineto(x*factor_x, y*factor_y))
c.stroke(p)
p = path.path(path.moveto(x2[0], y2[0]))
for x, y in zip(x2[1:], y2[1:]):
    p.append(path.lineto(x*factor_x, y*factor_y))
c.stroke(p, [style.linestyle.dashed])
c.writePDFfile()
