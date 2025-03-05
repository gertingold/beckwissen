import numpy as np
from pyx import canvas, color, deco, graph, path, style, text, trafo, unit

def convert_x(x, lenx=6.4):
    return x*lenx/2

def convert_y(y, leny=4):
    return (y+3)*4/23

unit.set(wscale=1.3, xscale=0.85)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
a = (17.958, 1.03999, 4.86912, -0.631042)
b = (17.9355, 0.822374, 3.87234, -0.802552)

d33p = [(0.187281383, 9.40366967),
        (0.249191303, 6.93366263),
        (0.374945829, 3.33450951),
        (0.49876567, 1.00564573),
        (0.750274722, 0.229357797),
        (1.49899782, 0.582215946)]

d55p = [(0.133110202, 5.4388219),
        (0.165999847, 5.92946893),
        (0.198889493, 4.30420064),
        (0.266603468, 3.1082485),
        (0.334317444, 0.869671414),
        (0.531655315, -1.46090199),
        (0.798641847, -1.7062255),
        (1.59960144, -0.387611604)]

c = canvas.canvas()
graphrect = path.rect(0, 0, 6.4, 4)
c.stroke(graphrect)
c.stroke(path.line(0, convert_y(0), 6.4, convert_y(0)), [style.linestyle.dotted])
x = np.linspace(0, 2, 100)
c1 = canvas.canvas([canvas.clip(graphrect)])
for coeffs, attrs in zip((a, b), (style.linewidth.Thick, style.linewidth.normal)):
    data = coeffs[0]*np.exp(-(1-np.exp(-coeffs[1]*x))*2*coeffs[2]*np.sin(coeffs[3])**2)*np.cos((1-np.exp(-coeffs[1]*x))*coeffs[2]*np.sin(2*coeffs[3]))
    p2 = path.path(path.moveto(convert_x(x[0]), convert_y(data[0])))
    for xp, yp in zip(x[1:], data[1:]):
        p2.append(path.lineto(convert_x(xp), convert_y(yp)))
    c1.stroke(p2, [attrs])
c.insert(c1)

for x, y in d33p:
    xp = convert_x(x)
    yp = convert_y(y)
    graph.style._squaresymbol(c, unit.topt(xp), unit.topt(yp), unit.topt(0.15), [deco.stroked(), deco.filled([color.grey(1)])])

for x, y in d55p:
    xp = convert_x(x)
    yp = convert_y(y)
    graph.style._circlesymbol(c, unit.topt(xp), unit.topt(yp), unit.topt(0.125), [deco.stroked(), deco.filled([color.grey(1)])])

c.stroke(path.line(0, convert_y(0), -0.1, convert_y(0)))
c.text(-0.2, convert_y(0), '0', [text.halign.right, text.valign.middle])
c.stroke(path.line(0, 0, 0, -0.1))
c.text(0, -0.2, '0', [text.halign.center, text.valign.top])
c.text(3.2, -0.3, 'Zeit', [text.halign.center, text.valign.top])
c.text(-0.4, 2, 'Korrelation', [text.halign.center, trafo.rotate(90)])
c.writePDFfile()
