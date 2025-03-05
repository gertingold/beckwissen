from math import sqrt
import numpy as np
from pyx import canvas, color, deco, path, style, trafo, unit

def muster(a, x0, y0):
    stepsize = 0.01
    fak = 0.31
    omega1 = 16
    omega2 = omega1/2
    x, y = np.mgrid[0:2+stepsize/2:stepsize, 0:2+stepsize/2:stepsize]
    col = a*np.cos(omega1*x)+(1-a)*np.cos(omega2*y)
    col = fak*col+0.5
    for ix in range(x.shape[0]):
        for iy in range(x.shape[1]):
            c.fill(path.rect(x[ix, iy], y[ix, iy], stepsize, stepsize),
                    [trafo.scale(0.5, 0.5).translated(x0, y0), color.grey(col[ix, iy])])

unit.set(wscale=1.3)
c = canvas.canvas()
c.stroke(path.circle(0, 0, 1), [style.linewidth.thin])
c.stroke(path.path(path.arc(0, 0, 1, 180, 0)), [trafo.scale(1, 0.4), style.linewidth.thin])
c.stroke(path.path(path.arc(0, 0, 1, 0, 180)),
         [trafo.scale(1, 0.4), style.linestyle.dashed, style.linewidth.thin])
c.fill(path.circle(0, 1, 0.04))
c.stroke(path.line(-0.25, 1.45, 0, 1), [style.linewidth.Thin])
c.fill(path.circle(0, -1, 0.04))
c.stroke(path.line(-0.25, -1.45, 0, -1), [style.linewidth.Thin])
c.fill(path.circle(-0.5, -0.4*sqrt(0.75), 0.04))
c.stroke(path.line(-1.45, -0.75, -0.5, -0.4*sqrt(0.75)), [style.linewidth.Thin])
c.fill(path.circle(0.4, 0.55, 0.04))
c.stroke(path.line(1.2, 1.25, 0.4, 0.55), [style.linewidth.Thin])
c.fill(path.circle(0.5, -0.7, 0.04))
c.stroke(path.line(1.2, -1.25, 0.5, -0.7), [style.linewidth.Thin])

muster(0.5, -2.5, -1.25)
muster(1, -1.25, -2.5)
muster(0, -1.25, 1.5)
muster(0.7, 1.25, -1.75)
muster(0.3, 1.25, 0.75)

c.writePDFfile()
