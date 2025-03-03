import numpy as np
from pyx import canvas, color, deco, path, style, text, trafo, unit

def mode(height, n, w):
    c.stroke(path.line(0, height, w, height), [style.linewidth.THin])
    x = np.linspace(0, w, 300)
    y = 0.3*np.sin(np.pi*n*x/w)
    p = path.path(path.moveto(x[0], y[0]+height))
    for xp, yp in zip(x[1:], y[1:]):
        p.append(path.lineto(xp, yp+height))
    c.stroke(p)

unit.set(wscale=1.3, xscale=0.9)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")

d = 0.1
h = 5.5
w = 3
c = canvas.canvas()
c.stroke(path.line(w+0.4, 0, w+0.4, h), [deco.earrow])
c.text(w+0.7, h, "Energie", [text.halign.right, text.valign.top, trafo.rotate(90)])
for n in range(4):
    height = 0.8+1.3*n
    c.stroke(path.line(w+0.3, height, w+0.5, height))
    mode(height, n+1, w)

c.fill(path.rect(-d, 0, d, h), [color.grey(0.7)])
c.stroke(path.line(0, 0, 0, h), [style.linewidth.Thin])
c.fill(path.rect(w, 0, d, h), [color.grey(0.7)])
c.stroke(path.line(w, 0, w, h), [style.linewidth.Thin])

offset = w+3
c.fill(path.rect(offset-d, 0, d, h), [color.grey(0.7)])
c.stroke(path.line(offset, 0, offset, h), [style.linewidth.Thin])
c.fill(path.rect(offset+w, 0, d, h), [color.grey(0.7)])
c.stroke(path.line(offset+w, 0, offset+w, h), [style.linewidth.Thin])

for n in range(-2, 15):
    height = 0.8+1.3*n/4
    c.stroke(path.line(w+3-d, height, w+3-d-0.7, height), [deco.barrow.small, style.linewidth.thick])
    c.stroke(path.line(2*w+3+d, height, 2*w+3+d+0.7, height), [deco.barrow.small, style.linewidth.thick])
    if n % 4:
        c.stroke(path.line(w+3, height, w+3+0.3, height), [deco.barrow.Small])
        c.stroke(path.line(2*w+3, height, 2*w+3-0.3, height), [deco.barrow.Small])
    else:
        c.stroke(path.line(w+3, height, w+3+1, height), [deco.barrow, style.linewidth.Thick])
        c.stroke(path.line(2*w+3, height, 2*w+3-1, height), [deco.barrow, style.linewidth.Thick])
c.writePDFfile()
