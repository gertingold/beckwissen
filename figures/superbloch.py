from math import sqrt
import numpy as np
from pyx import canvas, color, deco, path, style, trafo, unit

def muster(a, x0, y0):
    stepsize = 0.01
    fak = 0.31
    omega1 = 16
    omega2 = omega1/2
    x, y = np.mgrid[0:2+stepsize/2:stepsize, 0:2+stepsize/2:stepsize]
    col = a*np.cos(omega1*x)+(1-a)*np.cos(omega2*y)
    col = fak*col+0.5
    for ix in range(x.shape[0]):
        for iy in range(x.shape[1]):
            c.fill(path.rect(x[ix, iy], y[ix, iy], stepsize, stepsize),
                    [trafo.scale(0.5, 0.5).translated(x0, y0), color.grey(col[ix, iy])])

unit.set(wscale=1.3)
c = canvas.canvas()
c.stroke(path.circle(0, 0, 1), [style.linewidth.thin])
c.stroke(path.path(path.arc(0, 0, 1, 180, 0)), [trafo.scale(1, 0.4), style.linewidth.thin])
c.stroke(path.path(path.arc(0, 0, 1, 0, 180)),
         [trafo.scale(1, 0.4), style.linestyle.dashed, style.linewidth.thin])
c.fill(path.circle(0, 1, 0.04))
c.stroke(path.line(-0.25, 1.45, -0.05, 1.1), [deco.earrow.Small, style.linewidth.Thin])
c.fill(path.circle(0, -1, 0.04))
c.stroke(path.line(-0.25, -1.45, -0.05, -1.1), [deco.earrow.Small, style.linewidth.Thin])
c.fill(path.circle(-0.5, -0.4*sqrt(0.75), 0.04))
c.stroke(path.line(-1.45, -0.75, -0.58, -0.4*sqrt(0.75)-0.04), [deco.earrow.Small, style.linewidth.Thin])
c.fill(path.circle(0.4, 0.55, 0.04))
c.stroke(path.line(1.2, 1.25, 0.48, 0.63), [deco.earrow.Small, style.linewidth.Thin])
c.fill(path.circle(0.5, -0.7, 0.04))
c.stroke(path.line(1.2, -1.25, 0.57, -0.76), [deco.earrow.Small, style.linewidth.Thin])

muster(0.5, -2.5, -1.25)
muster(1, -1.25, -2.5)
muster(0, -1.25, 1.5)
muster(0.7, 1.25, -1.75)
muster(0.3, 1.25, 0.75)

c.writePDFfile()



# begin translate 2.5 8
# a=0
# for x = 0 to 2 step stepsize
#  for y = 0 to 2 step stepsize
#    amove x y
#    col=a*cos(o1*x)+(1-a)*cos(o2*y)
#    col=fak*col+0.5
#    box stepsize stepsize fill (col) nobox
#  next y
# next x
# end translate
# begin translate 7.5 1.5
# a=0.7
# for x = 0 to 2 step stepsize
#  for y = 0 to 2 step stepsize
#    amove x y
#    col=a*cos(o1*x)+(1-a)*cos(o2*y)
#    col=fak*col+0.5
#    box stepsize stepsize fill (col) nobox
#  next y
# next x
# end translate
# begin translate 7.5 6.5
# a=0.3
# for x = 0 to 2 step stepsize
#  for y = 0 to 2 step stepsize
#    amove x y
#    col=a*cos(o1*x)+(1-a)*cos(o2*y)
#    col=fak*col+0.5
#    box stepsize stepsize fill (col) nobox
#  next y
# next x
# end translate
# end scale
# 
# set lwidth 0.01
# begin translate 2.5 2.5
# amove 0 1
# circle 0.04 fill black
# amove 0 -1 
# circle 0.04 fill black
# amove 0 0
# circle 1
# 
# v=0.4
# amove -1 0
# set lstyle 3
# for n = -100 to 100 
#  x=n/100
#  aline x v*sqrt(1-x*x)
# next n
# set lstyle 1
# amove -1 0
# for n = -100 to 100 
#  x=n/100
#  aline x -v*sqrt(1-x*x)
# next n
# x=-0.5
# amove x -v*sqrt(1-x*x)
# circle 0.04 fill black
# amove 0.4 0.55
# circle 0.04 fill black
# amove 0.5 -0.7
# circle 0.04 fill black
# 
# set hei 0.4
# amove 2.25-2.5 -2.5+1.05
# aline -0.05 -1.1 arrow end
# amove 2.25-2.5 -2.5+3.95
# aline -0.05 1.1 arrow end
# amove -2.5+1.05 -2.5+1.75
# aline -0.58 -0.4*sqrt(1-0.5*0.5)-0.04 arrow end
# amove -2.5+3.7 -2.5+3.75
# aline 0.45 0.60 arrow end
# amove -2.5+3.7 -2.5+1.25
# aline 0.55 -0.75 arrow end
# end translate
# end scale
