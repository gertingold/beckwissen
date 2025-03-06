from math import sqrt
from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.85)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")

r = 0.5
circletrafo = trafo.scale(0.8, 1)
circlegrey = color.grey(0.5)
raygrey = color.grey(0.7)

c = canvas.canvas()

p = path.line(1.5, 1.5, 2.8, 2.0)
c.stroke(p, [deco.earrow.small])
x, y = p.at(p.arclentoparam(p.arclen()-0.4))
c.stroke(path.line(0, -0.23, 0, 0.27),
         [trafo.translate(x, y), deco.earrow.Small, style.linewidth(style._defaultlinewidth*0.9)])
c.fill(path.circle(0, 0, r), [circletrafo, trafo.translate(1.5, 1.5), circlegrey])
c.stroke(path.line(1.5, 1.5-r, 1.5, 1.5+r), [deco.earrow, style.linewidth.thick, color.grey(1)])
p = path.line(0.2, 1, 1.5, 1.5)
c.stroke(p)
x, y = p.at(p.arclentoparam(0.2))
c.stroke(path.line(x, y-0.23, x, y+0.27),
         [deco.earrow.Small, style.linewidth(style._defaultlinewidth*0.9)])
c.text(0.2, 2.2, r'a')

p = path.line(4.5, 1.5, 5.8, 2.0)
c.stroke(p, [deco.earrow.small, raygrey])
x, y = p.at(p.arclentoparam(p.arclen()-0.4))
c.stroke(path.line(0, -0.23, 0, 0.27),
         [trafo.rotate(-45).translated(x, y), raygrey, deco.earrow.Small,
          style.linewidth(style._defaultlinewidth*0.9)])
c.fill(path.circle(0, 0, r), [circletrafo, trafo.translate(4.5, 1.5), circlegrey])
r05 = r*sqrt(0.5)
c.stroke(path.line(-r05, -r05, r05, r05),
         [deco.earrow, style.linewidth.thick, color.grey(1), circletrafo, trafo.translate(4.5, 1.5)])
p = path.line(3.2, 1, 4.5, 1.5)
c.stroke(p)
x, y = p.at(p.arclentoparam(0.2))
c.stroke(path.line(x, y-0.23, x, y+0.27),
         [deco.earrow.Small, style.linewidth(style._defaultlinewidth*0.9)])
p = path.line(4.5, 1.5, 3.6, 1.0)
c.stroke(p, [deco.earrow.small, raygrey])
x, y = p.at(p.arclentoparam(p.arclen()-0.4))
c.stroke(path.line(0, -0.23, 0, 0.27),
         [trafo.rotate(-135).translated(x, y), raygrey, deco.earrow.Small,
          style.linewidth(style._defaultlinewidth*0.9)])
c.text(3.2, 2.2, r'b')

c.fill(path.circle(0, 0, r), [circletrafo, trafo.translate(7.5, 1.5), circlegrey])
c.stroke(path.line(-r, 0, r, 0),
         [deco.earrow, style.linewidth.thick, color.grey(1), circletrafo, trafo.translate(7.5, 1.5)])
p = path.line(6.2, 1, 7.5, 1.5)
c.stroke(p)
x, y = p.at(p.arclentoparam(0.2))
c.stroke(path.line(x, y-0.23, x, y+0.27),
         [deco.earrow.Small, style.linewidth(style._defaultlinewidth*0.9)])
p = path.line(7.5, 1.5, 6.6, 1.0)
c.stroke(p, [deco.earrow.small])
x, y = p.at(p.arclentoparam(p.arclen()-0.4))
c.stroke(path.line(0, -0.23, 0, 0.27),
         [trafo.translate(x, y), deco.earrow.Small, style.linewidth(style._defaultlinewidth*0.9)])
c.text(6.2, 2.2, r'c')

c.writePDFfile()
