from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.85)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()
textdone = False
for sign in (-1, 1):
    p = path.path(path.moveto(sign*0.9, 5.5),
                  path.lineto(sign*0.9, 3),
                  path.curveto(sign*0.9, 2, sign*0.9, 1.5, 0, 0))
    c.stroke(p, [style.linewidth.Thick, deco.earrow])
    param1 = p.arclentoparam(0.4)
    c.stroke(p.split(param1)[0], [style.linewidth.Thick, deco.earrow])
    for x, y in p.at(p.arclentoparam([1+0.5*n for n in range(-1, 4)])):
        c.stroke(path.line(-1.2, y, 1.2, y), [style.linewidth.Thick])
        if not textdone:
            c.text(1.4, y, "Elektronenwelle", [text.valign.middle])
            textdone = True
    for param in p.arclentoparam([1+0.5*n for n in range(4, 9)]):
        x, y = p.at(param)
        for angle in (90, 270):
            c.stroke(p.tangent(param, 0.3),
                     [trafo.translate(-x, -y).rotated(angle).translated(x, y),
                      style.linewidth.Thick])
    c.stroke(path.circle(0, 2, 0.3),
             [style.linewidth.THin, deco.filled([color.grey(0.5)])])
c.stroke(path.rect(-2, -0.08, 4, 0.08),
         [style.linewidth.THin, deco.filled([color.grey(0.8)])])

c.text(0, 5.7, "von der Elektronenquelle", [text.halign.center])
c.text(2.2, -0.08, "Schirm")
line = path.line(0.4, 0, 1.5, 0).transformed(trafo.rotate(-15).translated(0, 2))
x, y = line.atend()
c.stroke(line,
         [deco.barrow.small, style.linewidth.thin])
c.text(x+0.12, y-0.03, "positiv geladener Draht", [text.valign.middle])
c.writePDFfile()
