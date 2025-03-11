import math
import numpy as np
from pyx import canvas, color, deco, graph, path, style, text, trafo, unit

def segment(xvals, yvals, zvals):
    dist = math.hypot(*projector(xvals[0], yvals[0], zvals[0]))
    max1 = 0
    max2 = 0
    increasing = False
    for nr, (xp, yp, zp) in enumerate(zip(xvals[1:], yvals[1:], zvals[1:])):
        newdist = math.hypot(*projector(xp, yp, zp))
        if newdist > dist:
            increasing = True
        else:
            if increasing:
                if max1:
                    max2 = nr-1
                    increasing = False
                else:
                    max1 = nr
                    increasing = False
        dist = newdist
    p1 = path.path(path.moveto(*projector(xvals[max2], yvals[max2], zvals[max2])))
    for pos in zip(xvals[max2+1:], yvals[max2+1:], zvals[max2+1:]):
        p1.append(path.lineto(*projector(*pos)))
    for pos in zip(xvals[:max1+1], yvals[:max1+1], zvals[:max1+1]):
        p1.append(path.lineto(*projector(*pos)))
    p2 = path.path(path.moveto(*projector(xvals[max1], yvals[max1], zvals[max1])))
    for pos in zip(xvals[max1+1:max2+1], yvals[max1+1:max2+1], zvals[max1+1:max2+1]):
        p2.append(path.lineto(*projector(*pos)))
    return p1, p2

unit.set(wscale=1.3, xscale=0.85)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")

r = 2
phi = 20
c = canvas.canvas()
c.fill(path.circle(0, 0, r), [color.grey(0.9)])
projector = graph.graphxyz.parallel(phi, 20).point
phi = np.linspace(0, 2*np.pi, 1000)
x = r*np.cos(phi)
y = r*np.sin(phi)
z = np.zeros_like(x)
p1, p2 = segment(x, y, z)
p3, p4 = segment(y, z, x)
p5, p6 = segment(z, y, x)
c.stroke(p2, [color.grey(1), style.linewidth.thin])
c.stroke(p4, [color.grey(1), style.linewidth.thin])
c.stroke(p6, [color.grey(1), style.linewidth.thin])
p = path.path(path.moveto(*projector(0, 0, -r)))
for phi in np.linspace(0, np.pi, 200):
    alpha = np.sqrt(0.5)
    cp = np.cos(phi)
    sp = np.sin(phi)
    v = r*np.array([-(1-cp)/2, alpha*sp, -(1+cp)/2])
    p.append(path.lineto(*projector(*v)))
c.stroke(p, [style.linewidth.thick, deco.earrow])
c.stroke(p1, [color.grey(0.5), style.linewidth.thin])
c.stroke(p3, [color.grey(0.5), style.linewidth.thin])
c.stroke(p5, [color.grey(0.5), style.linewidth.thin])
c.stroke(path.line(*projector(-r*np.sqrt(0.5), 0, -r*np.sqrt(0.5)),
                   *projector(r*np.sqrt(0.5), 0, r*np.sqrt(0.5))))
p = path.path(path.moveto(*projector(0, 0, r)))
for phi in np.linspace(0, np.pi, 200):
    alpha = np.sqrt(0.5)
    cp = np.cos(phi)
    sp = np.sin(phi)
    v = r*np.array([(1-cp)/2, -alpha*sp, (1+cp)/2])
    p.append(path.lineto(*projector(*v)))
c.stroke(p, [style.linewidth.thick, deco.earrow])
c.stroke(path.circle(*projector(r*np.sqrt(0.5), 0, r*np.sqrt(0.5)), 0.04),
         [style.linewidth.Thin, deco.filled([color.grey(1)])])
c.stroke(path.line(*projector(r*np.sqrt(0.5), 0, r*np.sqrt(0.5)),
                   *projector(1.5*r*np.sqrt(0.5), 0, 1.5*r*np.sqrt(0.5))),
         [deco.earrow])

x, y = projector(0, 0, r)
c.stroke(path.line(x-0.01, y+0.05, x-0.3, y+0.4), [deco.barrow.Small, style.linewidth.Thin])
c.text(x-0.3, y+0.5, '|0⟩', [text.halign.right, text.valign.middle])
x, y = projector(0, 0, -r)
c.stroke(path.line(x+0.03, y-0.05, x+0.35, y-0.35), [deco.barrow.Small, style.linewidth.Thin])
c.text(x+0.4, y-0.4, '|1⟩', [text.valign.middle])
x, y = projector(r, 0, 0)
c.stroke(path.line(x-0.03, y-0.04, x-1.2, y-1.2), [deco.barrow.Small, style.linewidth.Thin])
c.text(x-1.25, y-1.3, '|0⟩+|1⟩', [text.halign.right, text.valign.middle])
x, y = projector(-r, 0, 0)
c.stroke(path.line(x+0.03, y+0.04, x+1.2, y+1.2), [deco.barrow.Small, style.linewidth.Thin])
c.text(x+1.25, y+1.25, '|0⟩-|1⟩', [text.valign.middle])

c.writePDFfile()
