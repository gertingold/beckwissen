import numpy as np
from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.9)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
r = 6.7
alpha = np.pi/6
c_alpha = np.cos(alpha)
s_alpha = np.sin(alpha)
freq = 2
ampx = 0.5
ampy = ampx
c = canvas.canvas()
c.stroke(path.line(0, 0, r*c_alpha, r*s_alpha), [deco.earrow])
x = np.linspace(0, 4*np.pi/freq, 41)
y = ampy*np.sin(freq*x)
for xp, yp in zip(x, y):
    c.stroke(path.line(xp*c_alpha, xp*s_alpha,
                       xp*c_alpha, xp*s_alpha + yp))
    c.stroke(path.line(xp*c_alpha, xp*s_alpha,
                       xp*c_alpha + yp, xp*s_alpha))
x = np.linspace(0, 4*np.pi/freq, 401)
y = ampy*np.sin(freq*x)
p = path.path(path.moveto(x[0]*c_alpha, x[0]*s_alpha))
for xp, yp in zip(x[1:], y[1:]):
    p.append(path.lineto(xp*c_alpha,  xp*s_alpha + yp))
c.stroke(p)
p = path.path(path.moveto(x[0]*c_alpha, x[0]*s_alpha))
for xp, yp in zip(x[1:], y[1:]):
    p.append(path.lineto(xp*c_alpha + yp,  xp*s_alpha))
c.stroke(p)

c.text(3.5, 1.6, 'Magnetfeld', [text.valign.top])
c.text(3.2, 2.5, 'elektrisches Feld', [text.halign.right])
c.writePDFfile()
