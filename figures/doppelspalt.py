import numpy as np
from pyx import canvas, color, deco, path, style, trafo, unit

unit.set(wscale=1.3)

c = canvas.canvas()

for y in (0, 1.3, 2.5, 3.7, 5):
    c.stroke(path.line(2.2, 2.5, 8, y), [deco.earrow])

stepsize = 0.01
omega = 16
x = np.arange(0, 2.2+stepsize/2, stepsize)
y = (np.cos(omega*(x-2.2))+1)/2
for xp, yp in zip (x, y):
    c.fill(path.rect(xp, 0, stepsize, 5), [color.grey(yp)])

ya = 1.5
yb = 3.5
x, y = np.mgrid[2.2:7.2+stepsize/2:stepsize, 0:5:stepsize]
amp = 0.5+0.25*(np.cos(omega*np.sqrt((x-2.199)**2+(y-ya)**2))
                + np.cos(omega*np.sqrt((x-2.199)**2+(y-yb)**2)))
ix, iy = x.shape
for ixp in range(ix):
    for iyp in range(iy):
        c.fill(path.rect(x[ixp, iyp], y[ixp, iyp], stepsize, stepsize), [color.grey(amp[ixp, iyp])])

c.fill(path.rect(2, 0, 0.2, 1.45), [color.grey(1)])
c.stroke(path.path(path.moveto(2, 0),
                   path.lineto(2, 1.45),
                   path.lineto(2.2, 1.45),
                   path.lineto(2.2, 0)), [style.linewidth.thin])
c.fill(path.rect(2, 1.55, 0.2, 1.9),
       [color.grey(1), deco.stroked([style.linewidth.thin, color.grey(0)])])
c.fill(path.rect(2, 3.55, 0.2, 1.45), [color.grey(1)])
c.stroke(path.path(path.moveto(2, 5),
                   path.lineto(2, 3.55),
                   path.lineto(2.2, 3.55),
                   path.lineto(2.2, 5)), [style.linewidth.thin])
c.writePDFfile()
