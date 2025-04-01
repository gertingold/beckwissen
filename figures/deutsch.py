from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.85)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()
c.fill(path.rect(-0.7, -1.35, 5.6, 0.35), [color.grey(0.9)])
c.fill(path.rect(-0.7, -2.15, 5.6, 0.35), [color.grey(0.9)])
y = 0.2
c.text(0, y, 'x', [text.halign.center])
c.text(0.4, y, 'y', [text.halign.center]) 
c.text(3.0, y, 'y$\oplus$f(x)', [text.halign.center]) 
y = -0.4
c.text(2.0, y, r'f(0)=1, f(1)=1', [text.halign.center])
c.text(4.0, y, r'f(0)=0, f(1)=1', [text.halign.center])
y = -0.9
c.text(-0.5, y+0.05, r'\footnotesize$+$', [text.halign.center])
c.text(0, y, '0', [text.halign.center])
c.text(0.4, y, '0', [text.halign.center]) 
c.text(2.0, y, '1', [text.halign.center])
c.text(4.0, y, '0', [text.halign.center])
y = -1.3
c.text(-0.5, y+0.05, r'\footnotesize$-$', [text.halign.center])
c.text(0, y, '0', [text.halign.center])
c.text(0.4, y, '1', [text.halign.center]) 
c.text(2.0, y, '0', [text.halign.center])
c.text(4.0, y, '1', [text.halign.center])
y = -1.7
c.text(-0.5, y+0.05, r'\footnotesize$+$', [text.halign.center])
c.text(0, y, '1', [text.halign.center])
c.text(0.4, y, '0', [text.halign.center]) 
c.text(2.0, y, '1', [text.halign.center])
c.text(4.0, y, '1', [text.halign.center])
y = -2.1
c.text(-0.5, y+0.05, r'\footnotesize$-$', [text.halign.center])
c.text(0, y, '1', [text.halign.center])
c.text(0.4, y, '1', [text.halign.center]) 
c.text(2.0, y, '0', [text.halign.center])
c.text(4.0, y, '0', [text.halign.center])
c.writePDFfile()
