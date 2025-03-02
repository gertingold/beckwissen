import numpy as np
from scipy import special
from pyx import canvas, color, deco, path, style, text, trafo, unit

def orbital(n, m, offset):
    theta = np.linspace(0, 2*np.pi, 500)
    r = np.abs(special.sph_harm(m, n, 0, theta))
    x = r*np.sin(theta)
    y = r*np.cos(theta)
    p = path.path(path.moveto(x[0], y[0]))
    for xp, yp in zip(x[1:], y[1:]):
        p.append(path.lineto(xp, yp))
    c.stroke(p, [trafo.translate(offset, 0)])

unit.set(wscale=1.1, xscale=0.9)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()
orbital(0, 0, 0)
c.text(0, -1.3, 's', [text.halign.center])
orbital(1, 0, 1.5)
c.text(1.5, -1.3, 'p', [text.halign.center])
orbital(2, 0, 3)
orbital(2, 1, 4)
c.text(3.5, -1.3, 'd', [text.halign.center])
orbital(3, 0, 5.5)
orbital(3, 1, 6.5)
c.text(6, -1.3, 'f', [text.halign.center])

c.writePDFfile()
