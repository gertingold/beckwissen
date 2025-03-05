from math import sqrt
import numpy as np
from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.85)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()
c.stroke(path.line(0, -1.2, 0, 1.5), [deco.earrow])
c.stroke(path.line(0, 0, 4, 0), [deco.earrow])
c.text(-0.2, 1.5, "Feldstärke", [text.halign.right, trafo.rotate(90)])
c.text(4, 0.2, "Zeit", [text.halign.right])

rng = np.random.default_rng()
nmax = 500
r = 0.005
factor_x = 0.5
sig_a = 0.0005
sig_b = 0.1
sig = sqrt(sig_a*sig_b)
x, y = np.ogrid[0:7.2:1j*nmax, -1.5:1.5:1j*nmax]
w = np.exp(-y**2/sig)
randomnumbers = rng.random((nmax, nmax))
validindices = np.nonzero(randomnumbers < w)
for ix, iy in zip(*validindices):
    c.fill(path.circle(x[ix, 0]*factor_x, y[0, iy], r))

c.writePDFfile()
