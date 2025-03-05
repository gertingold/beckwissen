import numpy as np
from pyx import canvas, color, deco, path, style, trafo, unit

unit.set(wscale=1.3, xscale=0.85)

ya = 2.3
yb = 2.7
c = canvas.canvas()

stepsize = 0.01
omega = 16
x = np.arange(0, 2.2, stepsize)
y = (np.cos(omega*(x-2.15))+1)/2
for xp, yp in zip (x, y):
    c.fill(path.rect(xp, 0, stepsize, 5), [color.grey(yp)])

nmax = 500
x, y = np.mgrid[2.2:7.2+stepsize/2:stepsize, 0:5:stepsize]
amp = 0
for n in range(nmax):
    yc = ya+(yb-ya)/nmax*(n+0.5)
    ampterm = np.cos(-np.pi/4+omega*np.sqrt((x-2.1)**2+(y-yc)**2))*(yb-ya)/nmax
    ampterm = ampterm/np.sqrt(np.sqrt((x-2.1)**2+(y-yc)**2))
    ampterm = ampterm*((x-2.1)/np.sqrt((x-2.1)**2+(y-yc)**2)+1)
    amp = amp + ampterm
amp = (amp-np.min(amp))/(np.max(amp)-np.min(amp))
ix, iy = x.shape
for ixp in range(ix):
    for iyp in range(iy):
        c.fill(path.rect(x[ixp, iyp], y[ixp, iyp], stepsize, stepsize), [color.grey(amp[ixp, iyp])])

c.fill(path.rect(2, 0, 0.2, ya), [color.grey(1)])
c.stroke(path.path(path.moveto(2, 0),
                   path.lineto(2, ya),
                   path.lineto(2.2, ya),
                   path.lineto(2.2, 0)),
         [style.linewidth.thin])
c.fill(path.rect(2, yb, 0.2, 5-yb), [color.grey(1)])
c.stroke(path.path(path.moveto(2, 5),
                   path.lineto(2, yb),
                   path.lineto(2.2, yb),
                   path.lineto(2.2, 5)),
         [style.linewidth.thin])
c.writePDFfile()
