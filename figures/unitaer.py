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
c.writePDFfile()
