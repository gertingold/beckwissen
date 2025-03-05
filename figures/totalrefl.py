from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.85)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()
boxcolor = color.grey(0.92)
for nr, label in zip(range(3), ('a', 'b', 'c')):
    c.fill(path.rect(3*nr, 0, 2.5, 1.5), [boxcolor])
    c.text(3*nr, -0.4, label)
c.fill(path.rect(6, 1.7, 2.5, 1.5), [boxcolor])

p1 = path.path(path.moveto(0.5, 0),
               path.lineto(1.25, 1.5))
c.stroke(p1.split(0.55*p1.end())[0], [deco.earrow])
p2 = path.path(path.moveto(1.25, 1.5),
               path.lineto(2.5, 1.5+0.925))
c.stroke(p2.split(0.55*p2.end())[0], [deco.earrow])
c.stroke(p1.join(p2))
c.stroke(path.path(path.moveto(1.25, 1.5),
                   path.lineto(0, 1.5-0.925)),
         [style.linestyle.dashed])

for offset in (3, 6):
    p1 = path.path(path.moveto(offset, 1.5-1.049),
                   path.lineto(offset+1.25, 1.5))
    c.stroke(p1.split(0.55*p1.end())[0], [deco.earrow])
    p2 = path.path(path.moveto(offset+1.25, 1.5),
                   path.lineto(offset+2.5, 1.5-1.049))
    c.stroke(p2.split(0.55*p2.end())[0], [deco.earrow])
    c.stroke(p1.join(p2))

transcolor = color.grey(0.5)
p1 = path.path(path.moveto(7.25, 1.7),
               path.rlineto(1.25, 1.049))
c.stroke(p1.split(0.55*p1.end())[0], [deco.earrow, transcolor])
c.stroke(p1, [transcolor])

c.writePDFfile()
