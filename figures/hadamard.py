from math import sqrt
from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.85)
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
c.stroke(path.line(-r-1, 0, -r-0.1, 0))
c.stroke(path.line(r+0.1, 0, r+1, 0), [deco.earrow])
p1 = path.path(path.arc(0, 0, r, 180, 0)).transformed(trafo.scale(1, yscale))
p3 = path.path(path.arc(0, 0, r, 0, 180)).transformed(trafo.scale(1, yscale))
c.stroke(p3, [style.linewidth.Thin])
c.text(0, r+0.2, '|0⟩', [text.halign.center])
c.text(0, -r-0.2, '|1⟩', [text.halign.center, text.valign.top])
p2 = path.path(path.arc(0, 0, r, 90, 270)).transformed(trafo.scale(yscale, 1))
c.stroke(p2, [style.linewidth.Thin])
(b1,), (b2,) = p1.intersect(p2)
xb, yb = p1.at(b1)
c.stroke(path.line(xb-0.05, yb-0.025, xb-1.5, yb-0.75), [style.linewidth.thin, deco.barrow.small])
c.text(xb-1.6, yb-0.8, '|0⟩+|1⟩', [text.halign.right, text.valign.middle])
c.stroke(p2.split(b2)[0], [deco.earrow.large, style.linewidth.Thick])
p4 = path.path(path.arc(0, 0, r, 270, 90)).transformed(trafo.scale(yscale, 1))
c.stroke(p4, [style.linewidth.Thin])
(c3,), (c4,) = p3.intersect(p4)
xc, yc = p3.at(c3)
c.stroke(path.line(xc+0.05, yc+0.025, xc+1.5, yc+0.75), [style.linewidth.thin, deco.barrow.small])
t = c.text(xc+1.6, yc+0.8, r'|0⟩\PyXMarker{left}\hphantom{+}\PyXMarker{right}|1⟩', [text.valign.middle])
tl = t.marker('left')
tr = t.marker('right')
kern = 0.0155
yshift = 0.073
c.stroke(path.line(tl[0]+kern, tl[1]+yshift, tr[0]-kern, tr[1]+yshift), [style.linewidth(style._defaultlinewidth*0.9)])
c.stroke(p4.split(c4)[0], [deco.earrow.large, style.linewidth.Thick])
(c1,), (c4,) = p1.intersect(p4)
c.stroke(p1.split((c1-0.1, c1+0.1))[1], [color.grey(1), style.linewidth.THick])
c.stroke(p1)
c.writePDFfile()
