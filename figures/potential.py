import numpy as np
from pyx import canvas, deco, path, text, trafo, unit

unit.set(wscale=1.3, xscale=0.85)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()
c.stroke(path.path(path.moveto(6.4, 0),
                   path.lineto(0, 0),
                   path.lineto(0, 4)), [deco.barrow, deco.earrow])
c.text(6.4, -0.2, "Ort", [text.halign.right, text.valign.top])
c.text(-0.2, 4, "Potential", [text.halign.right, trafo.rotate(90)])

x = np.linspace(0, 12, 500)
y = 0.03*(x-5.7)**2*(x-2)*(x-10)+3
indices = np.argwhere(y < 4.8)
x = x[indices]
y = y[indices]
factor_x = 6.4/13.5
factor_y = 4/5
p = path.path(path.moveto(x[0]*factor_x, y[0]*factor_y))
for xp, yp in zip(x[1:], y[1:]):
    p.append(path.lineto(xp*factor_x, yp*factor_y))
c.stroke(p)
for nr, (x, label, align) in enumerate(zip((2, 5.7, 10),
                                           ('A', 'B', 'C'),
                                           (text.halign.left, text.halign.center, text.halign.right))):
    c.fill(path.circle(x*factor_x, 3*factor_y, 0.06))
    c.text(x*factor_x+(1-nr)*0.1, 3*factor_y+0.12, label, [align])
c.writePDFfile()
