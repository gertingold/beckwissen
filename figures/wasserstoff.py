from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.9)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \usepackage{sansmathfonts}
                  \usepackage{amsmath}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()
rh = 8.5
c.fill(path.rect(0.2+rh, 1.1, 0.8, 1.9), [color.grey(0.7)])
for n in range(20):
    x = 0.2+rh*(1-1/(n+1)**2)
    c.stroke(path.line(x, 1.1, x, 3), [style.linewidth(style._defaultlinewidth*0.8)])
c.stroke(path.line(0.2+rh, 1.1, 0.2+rh, 3))
for n in range(3, 7):
    c.stroke(path.line(0.2+rh*(1-1/n**2), 1.3+0.5*(n-3),
                       0.2+0.75*rh, 1.3+0.5*(n-3)), [deco.earrow])
c.text(0.75*rh+0.1, 1.3, r"H$_\alpha$", [text.halign.right, text.valign.middle])
c.stroke(path.line(0, 0.3, 9.5, 0.3), [deco.earrow])
c.text(9.5, 0.1, "Energie", [text.halign.right, text.valign.top])
c.stroke(path.line(0.2+rh, 0.2, 0.2+rh, 0.4))
c.stroke(path.line(0.2+rh, 0.8, 0.2+rh, 1))
c.text(0.2+rh, 0.6, '0', [text.halign.center, text.valign.middle])
c.writePDFfile()
