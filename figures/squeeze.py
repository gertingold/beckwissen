from math import sqrt
import numpy as np
from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.9)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()
label = 'a'
for yoff in (3, 0):
    for xoff in (0, 4.5):
        c.stroke(path.line(xoff, yoff, xoff+4, yoff), [deco.earrow])
        c.text(xoff+4, yoff+0.2, "Zeit", [text.halign.right])
        c.stroke(path.line(xoff, yoff-1.2, xoff, yoff+1.5), [deco.earrow])
        if xoff == 0:
            c.text(xoff-0.2, yoff+1.5, "Feldstärke", [text.halign.right, trafo.rotate(90)])
        c.text(xoff+3.9, yoff-1.2, label, [text.halign.right, text.size.Large])
        label = chr(ord(label)+1)

a = 0.8
sig_a = 0.0005
sig_b = 0.1
r = 0.005

xoff = 0
yoff = 3
factor_x = 0.5
x = np.linspace(0, 2*np.pi, 500)
y = a*np.sin(x)
p = path.path(path.moveto(xoff+x[0]*factor_x, yoff+y[0]))
for xp, yp in zip(x[1:], y[1:]):
    p.append(path.lineto(xoff+xp*factor_x, yoff+yp))
c.stroke(p)

rng = np.random.default_rng()

nmax = 500
xoff = 4.5
yoff = 3
factor_x = 0.5
sig = sqrt(sig_a*sig_b)
x0 = 0.5*np.pi
x, y = np.ogrid[0:2*np.pi:1j*nmax, -1.5:1.5:1j*nmax]
fak = sig*np.sin(x+x0)**2 + sig*np.cos(x+x0)**2
w = np.exp(-(y-a*np.sin(x))**2/fak)/np.sqrt(fak)*sqrt(sig)
randomnumbers = rng.random((nmax, nmax))
validindices = np.nonzero(randomnumbers < w)
for ix, iy in zip(*validindices):
    c.fill(path.circle(xoff+x[ix, 0]*factor_x, yoff+y[0, iy], r))

nmax = 1000
xoff = 0
yoff = 0
factor_x = 0.5
x0 = 0
x, y = np.ogrid[0:2*np.pi:1j*nmax, -1.5:1.5:1j*nmax]
fak = sig_a*np.sin(x+x0)**2 + sig_b*np.cos(x+x0)**2
w = np.exp(-(y-a*np.sin(x))**2/fak)/np.sqrt(fak)*sqrt(sig_a)
randomnumbers = rng.random((nmax, nmax))
validindices = np.nonzero(randomnumbers < w)
for ix, iy in zip(*validindices):
    c.fill(path.circle(xoff+x[ix, 0]*factor_x, yoff+y[0, iy], r))

xoff = 4.5
yoff = 0
factor_x = 0.5
x0 = 0.5*np.pi
x, y = np.ogrid[0:2*np.pi:1j*nmax, -1.5:1.5:1j*nmax]
fak = sig_a*np.sin(x+x0)**2 + sig_b*np.cos(x+x0)**2
w = np.exp(-(y-a*np.sin(x))**2/fak)/np.sqrt(fak)*sqrt(sig_a)
randomnumbers = rng.random((nmax, nmax))
validindices = np.nonzero(randomnumbers < w)
for ix, iy in zip(*validindices):
    c.fill(path.circle(xoff+x[ix, 0]*factor_x, yoff+y[0, iy], r))

c.writePDFfile()
