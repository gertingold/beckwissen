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
p = path.line(-0.45, 0.75, 1.5, 1.5)
c.stroke(p)
x, y = p.at(p.arclentoparam(0.2))
c.stroke(path.line(x, y-0.23, x, y+0.27),
         [deco.earrow.Small, style.linewidth(style._defaultlinewidth*0.9)])
c.text(-0.45, 1.9, r'a', [text.size.Large])

xshift = 3.6
c.fill(path.circle(0, 0, r), [circletrafo, trafo.translate(xshift+1.5, 1.5), circlegrey])
c.stroke(path.line(0, -r, 0, r),
         [deco.earrow, style.linewidth.thick, color.grey(1), circletrafo, trafo.translate(xshift+1.5, 1.5)])
p = path.line(xshift-0.45, 0.75, xshift+1.5, 1.5)
c.stroke(p)
x, y = p.at(p.arclentoparam(0.2))
c.stroke(path.line(x-0.23, y, x+0.27, y),
         [deco.earrow.Small, style.linewidth(style._defaultlinewidth*0.9)])
p = path.line(xshift+1.5, 1.5, xshift+0.24, 0.8)
c.stroke(p, [deco.earrow.small])
x, y = p.at(p.arclentoparam(p.arclen()-0.3))
c.stroke(path.line(-0.23, 0, 0.27, 0),
         [trafo.translate(x, y), deco.earrow.Small, style.linewidth(style._defaultlinewidth*0.9)])
c.text(xshift-0.45, 1.9, r'b', [text.size.Large])

xshift = 1.4
yshift = -2.0
p = path.line(xshift+1.5, yshift+1.5, xshift+2.8, yshift+2.0)
c.stroke(p, [deco.earrow.small, raygrey])
x, y = p.at(p.arclentoparam(p.arclen()-0.4))
c.stroke(path.line(0, -0.23, 0, 0.27),
         [trafo.translate(x, y), raygrey, deco.earrow.Small,
          style.linewidth(style._defaultlinewidth*0.9)])
c.fill(path.circle(0, 0, r), [circletrafo, trafo.translate(xshift+1.5, yshift+1.5), circlegrey])
c.stroke(path.line(0, -r, 0, r),
         [deco.earrow, style.linewidth.thick, color.grey(1), circletrafo,
          trafo.translate(xshift+1.5, yshift+1.5)])
p = path.line(xshift-0.45, yshift+0.75, xshift+1.5, yshift+1.5)
c.stroke(p)
x, y = p.at(p.arclentoparam(0.2))
c.stroke(path.line(0, -0.23, 0, 0.27),
         [trafo.rotate(-45).translated(x, y), deco.earrow.Small, style.linewidth(style._defaultlinewidth*0.9)])
p = path.line(xshift+1.5, yshift+1.5, xshift+0.24, yshift+0.8)
c.stroke(p, [deco.earrow.small, raygrey])
x, y = p.at(p.arclentoparam(p.arclen()-0.3))
c.stroke(path.line(0, -0.23, 0, 0.27),
         [trafo.rotate(-90).translated(x, y), raygrey, deco.earrow.Small,
          style.linewidth(style._defaultlinewidth*0.9)])
c.text(xshift-0.45, yshift+1.9, r'c', [text.size.Large])

c.writePDFfile()
