from pyx import canvas, color, deco, deformer, path, style, trafo, unit

unit.set(wscale=1.3)

c = canvas.canvas([trafo.scale(1, 0.8)])
for y0 in (0, 4.8):
    c.fill(path.rect(2, y0, 1.5, 0.2))
for y0, h in ((1, 1), (2.15, 0.7), (3, 1)):
    c.fill(path.rect(2.7, y0, 0.1, h), [color.grey(0.6)])
c.stroke(path.rect(7, 0, -0.1, 5), [style.linewidth.thin])
p = path.path(path.moveto(0, 2.925),
              path.lineto(2.75, 2.925),
              path.lineto(6.9, 4))
c.stroke(p)
param = p.arclentoparam(1.5)
c.stroke(p.split(param)[0], [deco.earrow])
param = p.arclentoparam(4.5)
c.stroke(p.split(param)[0], [deco.earrow])
p = path.path(path.moveto(0, 2.075),
              path.lineto(2.75, 2.075),
              path.lineto(6.9, 4))
c.stroke(p)
param = p.arclentoparam(1.5)
c.stroke(p.split(param)[0], [deco.earrow])
param = p.arclentoparam(4.75)
c.stroke(p.split(param)[0], [deco.earrow])
c.stroke(path.line(2.75, 1, 2.75, 0.2),
         [deformer.cycloid(radius=0.2, halfloops=5, skipfirst=0.07, skiplast=0.07, turnangle=30),
          deformer.smoothed(0.05)])
c.stroke(path.line(2.75, 4.8, 2.75, 4),
         [deformer.cycloid(radius=0.2, halfloops=5, skipfirst=0.07, skiplast=0.07, turnangle=30),
          deformer.smoothed(0.05)])
c.writePDFfile()
