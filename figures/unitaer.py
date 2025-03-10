from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.85)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \usepackage{amsmath}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()

for y in (-0.7, 0.7):
    c.stroke(path.line(-1.5, y, 1.5, y))
c.fill(path.rect(-1, -1, 2, 2), [deco.stroked([color.grey(0)]), color.grey(1)])
c.text(0, 0, r'\Large U$_\text{f}$', [text.halign.center, text.valign.middle])
c.text(-1.6, 0.7, 'x', [text.halign.right, text.valign.middle])
c.text(-1.6, -0.7, 'y', [text.halign.right, text.valign.middle])
c.text(1.6, 0.7, 'x', [text.valign.middle])
c.text(1.6, -0.7, 'y$\oplus$f(x)', [text.valign.middle])
c.text(-2.2, 0.8, '\large b')

xoff = -5
c.text(xoff-1.2, 0.8, '\large a')
c.stroke(path.line(xoff-1, 0, xoff+1, 0))
c.text(xoff-1.1, 0, 'x', [text.halign.right, text.valign.middle])
c.text(xoff+1.1, 0, 'f(x)', [text.valign.middle])
c.fill(path.rect(xoff-0.5, -0.5, 1, 1), [color.grey(1), deco.stroked([color.grey(0)])])
c.text(xoff, 0, '\Large f', [text.halign.center, text.valign.middle])

xoff =-2.7 
yoff = -3
for y in (-0.7, 0.7):
    c.stroke(path.line(xoff-2.5, yoff+y, xoff+2.5, yoff+y))
    c.fill(path.rect(xoff-2.1, yoff+y-0.3, 0.6, 0.6), [color.grey(1), deco.stroked([color.grey(0)])])
    c.text(xoff-1.8, yoff+y, 'H', [text.halign.center, text.valign.middle])
c.text(xoff-2.6, yoff+0.7, '|0⟩', [text.halign.right, text.valign.middle])
c.text(xoff-2.6, yoff-0.7, '|1⟩', [text.halign.right, text.valign.middle])
c.fill(path.rect(xoff-1, yoff-1, 2, 2), [color.grey(1), deco.stroked([color.grey(0)])]) 
c.fill(path.rect(xoff+1.5, yoff+0.7-0.3, 0.6, 0.6), [color.grey(1), deco.stroked([color.grey(0)])])
c.stroke(path.path(path.moveto(xoff+2.5, yoff+0.7-0.25),
                   path.lineto(xoff+2.5, yoff+0.7+0.25),
                   path.arcn(xoff+2.5, yoff+0.7, 0.25, 90, 270),
                   path.closepath()), [deco.filled([color.grey(0.7)])])
c.text(xoff+2.9, yoff+0.8, '\small |0⟩ → konstant')
c.text(xoff+2.9, yoff+0.6, '\small |1⟩ → ausgeglichen', [text.valign.top])
c.text(xoff+1.8, yoff+0.7, 'H', [text.halign.center, text.valign.middle])
c.text(xoff, yoff, r'\Large U$_\text{f}$', [text.halign.center, text.valign.middle])
c.text(xoff-3.5, yoff+0.9, '\large c')

c.writePDFfile()
