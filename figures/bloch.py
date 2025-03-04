from math import sqrt
from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.9)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")

r = 2
s = 0.8
yscale = 0.4
c = canvas.canvas()
p0 = path.circle(0, 0, r)
c.stroke(p0)
c.stroke(path.line(-r-1.1, 0, -r-0.1, 0))
c.stroke(path.line(r+0.1, 0, r+1.1, 0), [deco.earrow])
p1 = path.path(path.arc(0, 0, r, 180, 0)).transformed(trafo.scale(1, yscale))
c.stroke(p1)
c.stroke(path.path(path.arc(0, 0, r, 0, 180)), [trafo.scale(1, yscale), style.linestyle.dashed])
c.text(0, r+0.1, 'A', [text.halign.center])
p2 = path.path(path.arc(0, 0, r, 90, 270)).transformed(trafo.scale(yscale, 1))
c.stroke(p2)
(b1,), (b2,) = p1.intersect(p2)
c.stroke(p2.split(b2)[0], [deco.earrow.large, style.linewidth.Thick])
xb, yb = p1.at(b1)
c.text(xb-0.1, yb-0.1, 'B', [text.halign.right, text.valign.top])
p3 = path.path(path.arc(0, 0, r, 180, 300)).transformed(trafo.scale(0.3, sqrt(1-s*s)).translated(s*r, 0))
(c1,), (c3,) = p1.intersect(p3)
c.stroke(p1.split((b1, c1))[1], [deco.earrow.large, style.linewidth.Thick])
xc, yc = p1.at(c1)
c.text(xc, yc+0.1, 'C', [text.halign.center])
(d0,), (d3,) = p0.intersect(p3)
c.stroke(p3.split((c3, d3))[1], [deco.earrow.large, style.linewidth.Thick])
xd, yd = p3.at(d3)
c.text(xd+0.1, yd-0.05, 'D', [text.valign.middle])
c.writePDFfile()
