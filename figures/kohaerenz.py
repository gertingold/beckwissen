from itertools import cycle
from math import cos, radians, sin
from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.9)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")

alpha = radians(25)
darkgrey = color.grey(0.2)
lightgrey = color.grey(0.8)
r = 0.3

c = canvas.canvas()
c.stroke(path.line(0, 0, 1, 0))
c.stroke(path.circle(1, 0, r), [deco.filled([color.grey(1)])])
c.stroke(path.line(1.5, 0, 2.9, 0), [deco.earrow])
c.text(1.6, 0.2, "Atom 1")
for sign, colour in zip((-1, 1), (lightgrey, darkgrey)):
    x0 = 3.1
    c.stroke(path.line(x0, 0, x0+cos(alpha), sign*sin(alpha)))
    c.stroke(path.circle(x0+cos(alpha), sign*sin(alpha), r), [deco.filled([colour])])
c.stroke(path.line(4.6, 0, 6, 0), [deco.earrow])
c.text(4.7, 0.2, "Atom 2")

for fak in (-2, 0, 2):
    x0 = 6.2
    c.stroke(path.line(x0, 0, x0+cos(fak*alpha), sin(fak*alpha)))
c.stroke(path.circle(x0+cos(2*alpha), sin(2*alpha), r), [deco.filled([darkgrey])])
c.stroke(path.circle(x0+cos(2*alpha), -sin(2*alpha), r), [deco.filled([lightgrey])])
clippath = path.circle(0, 0, r)
c1 = canvas.canvas([canvas.clip(clippath)])
step = 0.1
for n, colour in zip(range(6), cycle((lightgrey, darkgrey))):
    x = -0.3+n*step
    c1.fill(path.rect(x, -r, step, 2*r), [colour])
shift = trafo.translate(7.2, 0)
c.insert(c1, [shift])
c.stroke(clippath, [shift])
c.writePDFfile()
