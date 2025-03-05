from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.85)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()
c.stroke(path.rect(0.55, 1.2, 0.8, 0.8))
c.stroke(path.rect(3.15, 1.2, 0.8, 0.8))
c.fill(path.rect(0.25, 1.45, 4, 0.3), [color.grey(1)])

p = path.path(path.moveto(0.88, 2),
              path.lineto(0.88, 2.67),
              path.lineto(3.62, 2.67),
              path.lineto(3.62, 2))
c.stroke(p)
p = path.path(path.moveto(1.02, 2),
              path.lineto(1.02, 2.53),
              path.lineto(3.48, 2.53),
              path.lineto(3.48, 2))
c.stroke(p)
c.stroke(path.rect(1.95, 2.3, 0.6, 0.6), [deco.filled([color.grey(0.7)])])

c.stroke(path.rect(5.65, 1.2, 1.5, 0.8))
c.fill(path.rect(6.05, 1.1, 0.7, 1), [deco.filled([color.grey(1)])])
c.stroke(path.line(7.15, 1.67, 7.7, 1.67)) 
c.stroke(path.line(7.15, 1.53, 7.7, 1.53)) 
c.stroke(path.rect(7.7, 1.3, 0.6, 0.6), [deco.filled([color.grey(0.7)])])

c.stroke(path.line(0, 1.6, 4.8, 1.6), [style.linewidth.Thick, deco.earrow.large])
p = path.path(path.moveto(6.2, 0.1),
              path.lineto(6.2, 3.6),
              path.arcn(6.4, 3.6, 0.2, 180, 0),
              path.lineto(6.6, 3.6),
              path.lineto(6.6, 0.3))
c.stroke(p, [style.linewidth.Thick, deco.earrow.large])

c.text(0.3, 1.7, 'A', [text.halign.center])
c.text(1.6, 1.7, 'B', [text.halign.center])
c.text(2.9, 1.7, 'C', [text.halign.center])

c.text(5.95, 1.1, 'A', [text.halign.center, text.valign.top])
c.text(5.95, 2.1, 'B', [text.halign.center])
c.text(6.85, 2.1, 'C', [text.halign.center])
c.text(6.85, 1.1, 'D', [text.halign.center, text.valign.top])

c.text(0.1, 3.6, 'a')
c.text(5.5, 3.6, 'b')

c.writePDFfile()
