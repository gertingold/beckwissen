from math import sqrt
import numpy as np
from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(wscale=1.3, xscale=0.9)
text.set(text.LatexRunner, texenc="utf-8")
text.preamble(r"""\usepackage{helvet}
                  \usepackage[T1]{fontenc}
                  \renewcommand\familydefault{\sfdefault}""")
c = canvas.canvas()
c.stroke(path.line(0, -1.2, 0, 1.5), [deco.earrow])
c.stroke(path.line(0, 0, 4, 0), [deco.earrow])
c.text(-0.2, 1.5, "Feldstärke", [text.halign.right, trafo.rotate(90)])
c.text(4, 0.2, "Zeit", [text.halign.right])

rng = np.random.default_rng()
nmax = 500
r = 0.005
factor_x = 0.5
sig_a = 0.0005
sig_b = 0.1
sig = sqrt(sig_a*sig_b)
x, y = np.ogrid[0:7.2:1j*nmax, -1.5:1.5:1j*nmax]
w = np.exp(-y**2/sig)
randomnumbers = rng.random((nmax, nmax))
validindices = np.nonzero(randomnumbers < w)
for ix, iy in zip(*validindices):
    c.fill(path.circle(x[ix, 0]*factor_x, y[0, iy], r))

c.writePDFfile()



# size 4.5 2.7
# 
# siga=0.005
# sigb=0.1
# a=0.8
# x0=0
# delta=0.1
# 
# begin translate 0.5 -0.3
# xoff=0.
# yoff=1.5
# xs=0.5
#  amove   0.  1.45864662
#  circle 0.002 fill black
#  amove   0.  1.54887218
#  circle 0.002 fill black
#  amove   0.  1.57142857
#  circle 0.002 fill black
#  amove   0.0085213035  1.45864662
#  circle 0.002 fill black
#  amove   0.0085213035  1.4962406
#  circle 0.002 fill black
#  amove   0.017042607  1.46616541
#  circle 0.002 fill black
#  amove   0.017042607  1.54135338
#  circle 0.002 fill black
#  amove   0.0255639105  1.41353383
#  circle 0.002 fill black
#  amove   0.0255639105  1.44360902
#  circle 0.002 fill black
#  amove   0.0255639105  1.47368421
#  circle 0.002 fill black
#  amove   0.0255639105  1.48120301
#  circle 0.002 fill black
#  amove   0.0255639105  1.5037594
#  circle 0.002 fill black
#  amove   0.0255639105  1.53383459
#  circle 0.002 fill black
#  amove   0.034085214  1.4887218
#  circle 0.002 fill black
#  amove   0.034085214  1.5037594
#  circle 0.002 fill black
#  amove   0.034085214  1.5112782
#  circle 0.002 fill black
#  amove   0.034085214  1.53383459
#  circle 0.002 fill black
#  amove   0.034085214  1.56390977
#  circle 0.002 fill black
#  amove   0.0426065175  1.39097744
#  circle 0.002 fill black
#  amove   0.0426065175  1.44360902
#  circle 0.002 fill black
#  amove   0.0426065175  1.47368421
#  circle 0.002 fill black
#  amove   0.0426065175  1.5037594
#  circle 0.002 fill black
#  amove   0.051127821  1.38345865
#  circle 0.002 fill black
#  amove   0.051127821  1.40601504
#  circle 0.002 fill black
#  amove   0.051127821  1.44360902
#  circle 0.002 fill black
#  amove   0.051127821  1.45112782
#  circle 0.002 fill black
#  amove   0.051127821  1.46616541
#  circle 0.002 fill black
#  amove   0.051127821  1.51879699
#  circle 0.002 fill black
#  amove   0.051127821  1.53383459
#  circle 0.002 fill black
#  amove   0.051127821  1.60150376
#  circle 0.002 fill black
#  amove   0.0596491245  1.5037594
#  circle 0.002 fill black
#  amove   0.0596491245  1.5112782
#  circle 0.002 fill black
#  amove   0.0596491245  1.52631579
#  circle 0.002 fill black
#  amove   0.0596491245  1.53383459
#  circle 0.002 fill black
#  amove   0.068170428  1.45864662
#  circle 0.002 fill black
#  amove   0.068170428  1.51879699
#  circle 0.002 fill black
#  amove   0.068170428  1.61654135
#  circle 0.002 fill black
#  amove   0.0766917315  1.36842105
#  circle 0.002 fill black
#  amove   0.0766917315  1.42105263
#  circle 0.002 fill black
#  amove   0.0766917315  1.43609023
#  circle 0.002 fill black
#  amove   0.0766917315  1.45864662
#  circle 0.002 fill black
#  amove   0.0766917315  1.48120301
#  circle 0.002 fill black
#  amove   0.0766917315  1.58646617
#  circle 0.002 fill black
#  amove   0.0766917315  1.59398496
#  circle 0.002 fill black
#  amove   0.085213035  1.44360902
#  circle 0.002 fill black
#  amove   0.085213035  1.45864662
#  circle 0.002 fill black
#  amove   0.085213035  1.5037594
#  circle 0.002 fill black
#  amove   0.085213035  1.5112782
#  circle 0.002 fill black
#  amove   0.085213035  1.51879699
#  circle 0.002 fill black
#  amove   0.085213035  1.56390977
#  circle 0.002 fill black
#  amove   0.085213035  1.58646617
#  circle 0.002 fill black
#  amove   0.0937343385  1.4962406
#  circle 0.002 fill black
#  amove   0.0937343385  1.56390977
#  circle 0.002 fill black
#  amove   0.102255642  1.38345865
#  circle 0.002 fill black
#  amove   0.102255642  1.44360902
#  circle 0.002 fill black
#  amove   0.102255642  1.48120301
#  circle 0.002 fill black
#  amove   0.102255642  1.4887218
#  circle 0.002 fill black
#  amove   0.102255642  1.4962406
#  circle 0.002 fill black
#  amove   0.102255642  1.5112782
#  circle 0.002 fill black
#  amove   0.102255642  1.51879699
#  circle 0.002 fill black
#  amove   0.102255642  1.54135338
#  circle 0.002 fill black
#  amove   0.102255642  1.54887218
#  circle 0.002 fill black
#  amove   0.102255642  1.60150376
#  circle 0.002 fill black
#  amove   0.110776945  1.31578947
#  circle 0.002 fill black
#  amove   0.110776945  1.38345865
#  circle 0.002 fill black
#  amove   0.110776945  1.45112782
#  circle 0.002 fill black
#  amove   0.110776945  1.47368421
#  circle 0.002 fill black
#  amove   0.110776945  1.4887218
#  circle 0.002 fill black
#  amove   0.110776945  1.5037594
#  circle 0.002 fill black
#  amove   0.110776945  1.52631579
#  circle 0.002 fill black
#  amove   0.110776945  1.54887218
#  circle 0.002 fill black
#  amove   0.110776945  1.56390977
#  circle 0.002 fill black
#  amove   0.119298249  1.41353383
#  circle 0.002 fill black
#  amove   0.119298249  1.43609023
#  circle 0.002 fill black
#  amove   0.119298249  1.4962406
#  circle 0.002 fill black
#  amove   0.119298249  1.5037594
#  circle 0.002 fill black
#  amove   0.119298249  1.51879699
#  circle 0.002 fill black
#  amove   0.119298249  1.54135338
#  circle 0.002 fill black
#  amove   0.119298249  1.62406015
#  circle 0.002 fill black
#  amove   0.127819552  1.33834586
#  circle 0.002 fill black
#  amove   0.127819552  1.41353383
#  circle 0.002 fill black
#  amove   0.127819552  1.5037594
#  circle 0.002 fill black
#  amove   0.127819552  1.52631579
#  circle 0.002 fill black
#  amove   0.127819552  1.54135338
#  circle 0.002 fill black
#  amove   0.136340856  1.39097744
#  circle 0.002 fill black
#  amove   0.136340856  1.43609023
#  circle 0.002 fill black
#  amove   0.136340856  1.51879699
#  circle 0.002 fill black
#  amove   0.144862159  1.45864662
#  circle 0.002 fill black
#  amove   0.144862159  1.48120301
#  circle 0.002 fill black
#  amove   0.144862159  1.5037594
#  circle 0.002 fill black
#  amove   0.144862159  1.57142857
#  circle 0.002 fill black
#  amove   0.144862159  1.59398496
#  circle 0.002 fill black
#  amove   0.153383463  1.40601504
#  circle 0.002 fill black
#  amove   0.153383463  1.45112782
#  circle 0.002 fill black
#  amove   0.153383463  1.45864662
#  circle 0.002 fill black
#  amove   0.153383463  1.46616541
#  circle 0.002 fill black
#  amove   0.153383463  1.5112782
#  circle 0.002 fill black
#  amove   0.153383463  1.57894737
#  circle 0.002 fill black
#  amove   0.153383463  1.62406015
#  circle 0.002 fill black
#  amove   0.153383463  1.63157895
#  circle 0.002 fill black
#  amove   0.153383463  1.65413534
#  circle 0.002 fill black
#  amove   0.161904766  1.5037594
#  circle 0.002 fill black
#  amove   0.161904766  1.60150376
#  circle 0.002 fill black
#  amove   0.17042607  1.42105263
#  circle 0.002 fill black
#  amove   0.17042607  1.51879699
#  circle 0.002 fill black
#  amove   0.17042607  1.54887218
#  circle 0.002 fill black
#  amove   0.178947373  1.35338346
#  circle 0.002 fill black
#  amove   0.178947373  1.36842105
#  circle 0.002 fill black
#  amove   0.178947373  1.46616541
#  circle 0.002 fill black
#  amove   0.178947373  1.48120301
#  circle 0.002 fill black
#  amove   0.178947373  1.51879699
#  circle 0.002 fill black
#  amove   0.178947373  1.52631579
#  circle 0.002 fill black
#  amove   0.187468677  1.42857143
#  circle 0.002 fill black
#  amove   0.187468677  1.45864662
#  circle 0.002 fill black
#  amove   0.187468677  1.48120301
#  circle 0.002 fill black
#  amove   0.187468677  1.5037594
#  circle 0.002 fill black
#  amove   0.187468677  1.56390977
#  circle 0.002 fill black
#  amove   0.187468677  1.57142857
#  circle 0.002 fill black
#  amove   0.19598998  1.41353383
#  circle 0.002 fill black
#  amove   0.19598998  1.44360902
#  circle 0.002 fill black
#  amove   0.19598998  1.45112782
#  circle 0.002 fill black
#  amove   0.19598998  1.45864662
#  circle 0.002 fill black
#  amove   0.19598998  1.52631579
#  circle 0.002 fill black
#  amove   0.204511284  1.43609023
#  circle 0.002 fill black
#  amove   0.204511284  1.46616541
#  circle 0.002 fill black
#  amove   0.204511284  1.47368421
#  circle 0.002 fill black
#  amove   0.204511284  1.56390977
#  circle 0.002 fill black
#  amove   0.213032587  1.41353383
#  circle 0.002 fill black
#  amove   0.213032587  1.45112782
#  circle 0.002 fill black
#  amove   0.213032587  1.45864662
#  circle 0.002 fill black
#  amove   0.213032587  1.5037594
#  circle 0.002 fill black
#  amove   0.213032587  1.5112782
#  circle 0.002 fill black
#  amove   0.213032587  1.59398496
#  circle 0.002 fill black
#  amove   0.221553891  1.36842105
#  circle 0.002 fill black
#  amove   0.221553891  1.42105263
#  circle 0.002 fill black
#  amove   0.221553891  1.45864662
#  circle 0.002 fill black
#  amove   0.221553891  1.48120301
#  circle 0.002 fill black
#  amove   0.221553891  1.54135338
#  circle 0.002 fill black
#  amove   0.221553891  1.57894737
#  circle 0.002 fill black
#  amove   0.230075194  1.53383459
#  circle 0.002 fill black
#  amove   0.230075194  1.54135338
#  circle 0.002 fill black
#  amove   0.230075194  1.55639098
#  circle 0.002 fill black
#  amove   0.238596498  1.47368421
#  circle 0.002 fill black
#  amove   0.238596498  1.48120301
#  circle 0.002 fill black
#  amove   0.238596498  1.53383459
#  circle 0.002 fill black
#  amove   0.238596498  1.55639098
#  circle 0.002 fill black
#  amove   0.238596498  1.57142857
#  circle 0.002 fill black
#  amove   0.238596498  1.63157895
#  circle 0.002 fill black
#  amove   0.247117801  1.42105263
#  circle 0.002 fill black
#  amove   0.247117801  1.45864662
#  circle 0.002 fill black
#  amove   0.247117801  1.46616541
#  circle 0.002 fill black
#  amove   0.247117801  1.47368421
#  circle 0.002 fill black
#  amove   0.247117801  1.4887218
#  circle 0.002 fill black
#  amove   0.247117801  1.4962406
#  circle 0.002 fill black
#  amove   0.247117801  1.52631579
#  circle 0.002 fill black
#  amove   0.247117801  1.54887218
#  circle 0.002 fill black
#  amove   0.247117801  1.55639098
#  circle 0.002 fill black
#  amove   0.247117801  1.56390977
#  circle 0.002 fill black
#  amove   0.255639105  1.45864662
#  circle 0.002 fill black
#  amove   0.255639105  1.46616541
#  circle 0.002 fill black
#  amove   0.255639105  1.4962406
#  circle 0.002 fill black
#  amove   0.255639105  1.54135338
#  circle 0.002 fill black
#  amove   0.255639105  1.54887218
#  circle 0.002 fill black
#  amove   0.255639105  1.61654135
#  circle 0.002 fill black
#  amove   0.264160408  1.45112782
#  circle 0.002 fill black
#  amove   0.264160408  1.46616541
#  circle 0.002 fill black
#  amove   0.264160408  1.47368421
#  circle 0.002 fill black
#  amove   0.272681712  1.34586466
#  circle 0.002 fill black
#  amove   0.272681712  1.41353383
#  circle 0.002 fill black
#  amove   0.272681712  1.45112782
#  circle 0.002 fill black
#  amove   0.272681712  1.47368421
#  circle 0.002 fill black
#  amove   0.272681712  1.56390977
#  circle 0.002 fill black
#  amove   0.281203015  1.43609023
#  circle 0.002 fill black
#  amove   0.281203015  1.44360902
#  circle 0.002 fill black
#  amove   0.281203015  1.5037594
#  circle 0.002 fill black
#  amove   0.281203015  1.51879699
#  circle 0.002 fill black
#  amove   0.289724319  1.40601504
#  circle 0.002 fill black
#  amove   0.289724319  1.44360902
#  circle 0.002 fill black
#  amove   0.289724319  1.47368421
#  circle 0.002 fill black
#  amove   0.289724319  1.4962406
#  circle 0.002 fill black
#  amove   0.289724319  1.5037594
#  circle 0.002 fill black
#  amove   0.289724319  1.54887218
#  circle 0.002 fill black
#  amove   0.298245622  1.40601504
#  circle 0.002 fill black
#  amove   0.298245622  1.41353383
#  circle 0.002 fill black
#  amove   0.298245622  1.43609023
#  circle 0.002 fill black
#  amove   0.298245622  1.4887218
#  circle 0.002 fill black
#  amove   0.298245622  1.52631579
#  circle 0.002 fill black
#  amove   0.298245622  1.53383459
#  circle 0.002 fill black
#  amove   0.306766926  1.44360902
#  circle 0.002 fill black
#  amove   0.306766926  1.46616541
#  circle 0.002 fill black
#  amove   0.306766926  1.47368421
#  circle 0.002 fill black
#  amove   0.306766926  1.48120301
#  circle 0.002 fill black
#  amove   0.306766926  1.5112782
#  circle 0.002 fill black
#  amove   0.306766926  1.54887218
#  circle 0.002 fill black
#  amove   0.315288229  1.45864662
#  circle 0.002 fill black
#  amove   0.315288229  1.4962406
#  circle 0.002 fill black
#  amove   0.315288229  1.51879699
#  circle 0.002 fill black
#  amove   0.323809533  1.45112782
#  circle 0.002 fill black
#  amove   0.323809533  1.46616541
#  circle 0.002 fill black
#  amove   0.323809533  1.48120301
#  circle 0.002 fill black
#  amove   0.323809533  1.4887218
#  circle 0.002 fill black
#  amove   0.323809533  1.51879699
#  circle 0.002 fill black
#  amove   0.323809533  1.57894737
#  circle 0.002 fill black
#  amove   0.323809533  1.62406015
#  circle 0.002 fill black
#  amove   0.332330836  1.53383459
#  circle 0.002 fill black
#  amove   0.332330836  1.56390977
#  circle 0.002 fill black
#  amove   0.34085214  1.47368421
#  circle 0.002 fill black
#  amove   0.34085214  1.52631579
#  circle 0.002 fill black
#  amove   0.34085214  1.59398496
#  circle 0.002 fill black
#  amove   0.349373443  1.39849624
#  circle 0.002 fill black
#  amove   0.349373443  1.47368421
#  circle 0.002 fill black
#  amove   0.349373443  1.4887218
#  circle 0.002 fill black
#  amove   0.349373443  1.51879699
#  circle 0.002 fill black
#  amove   0.349373443  1.53383459
#  circle 0.002 fill black
#  amove   0.349373443  1.54135338
#  circle 0.002 fill black
#  amove   0.349373443  1.57142857
#  circle 0.002 fill black
#  amove   0.357894747  1.45112782
#  circle 0.002 fill black
#  amove   0.357894747  1.48120301
#  circle 0.002 fill black
#  amove   0.357894747  1.52631579
#  circle 0.002 fill black
#  amove   0.357894747  1.56390977
#  circle 0.002 fill black
#  amove   0.357894747  1.60902256
#  circle 0.002 fill black
#  amove   0.36641605  1.46616541
#  circle 0.002 fill black
#  amove   0.36641605  1.48120301
#  circle 0.002 fill black
#  amove   0.36641605  1.4962406
#  circle 0.002 fill black
#  amove   0.36641605  1.5112782
#  circle 0.002 fill black
#  amove   0.36641605  1.51879699
#  circle 0.002 fill black
#  amove   0.36641605  1.57142857
#  circle 0.002 fill black
#  amove   0.36641605  1.67669173
#  circle 0.002 fill black
#  amove   0.374937354  1.4887218
#  circle 0.002 fill black
#  amove   0.374937354  1.52631579
#  circle 0.002 fill black
#  amove   0.374937354  1.53383459
#  circle 0.002 fill black
#  amove   0.374937354  1.54135338
#  circle 0.002 fill black
#  amove   0.383458657  1.41353383
#  circle 0.002 fill black
#  amove   0.383458657  1.45112782
#  circle 0.002 fill black
#  amove   0.383458657  1.52631579
#  circle 0.002 fill black
#  amove   0.383458657  1.54135338
#  circle 0.002 fill black
#  amove   0.383458657  1.55639098
#  circle 0.002 fill black
#  amove   0.383458657  1.63909774
#  circle 0.002 fill black
#  amove   0.391979961  1.44360902
#  circle 0.002 fill black
#  amove   0.391979961  1.45112782
#  circle 0.002 fill black
#  amove   0.391979961  1.4887218
#  circle 0.002 fill black
#  amove   0.391979961  1.56390977
#  circle 0.002 fill black
#  amove   0.391979961  1.59398496
#  circle 0.002 fill black
#  amove   0.400501264  1.46616541
#  circle 0.002 fill black
#  amove   0.400501264  1.4887218
#  circle 0.002 fill black
#  amove   0.400501264  1.5112782
#  circle 0.002 fill black
#  amove   0.400501264  1.53383459
#  circle 0.002 fill black
#  amove   0.400501264  1.54887218
#  circle 0.002 fill black
#  amove   0.400501264  1.55639098
#  circle 0.002 fill black
#  amove   0.400501264  1.59398496
#  circle 0.002 fill black
#  amove   0.400501264  1.60902256
#  circle 0.002 fill black
#  amove   0.409022568  1.39097744
#  circle 0.002 fill black
#  amove   0.409022568  1.42857143
#  circle 0.002 fill black
#  amove   0.409022568  1.44360902
#  circle 0.002 fill black
#  amove   0.409022568  1.46616541
#  circle 0.002 fill black
#  amove   0.409022568  1.47368421
#  circle 0.002 fill black
#  amove   0.409022568  1.48120301
#  circle 0.002 fill black
#  amove   0.409022568  1.53383459
#  circle 0.002 fill black
#  amove   0.409022568  1.58646617
#  circle 0.002 fill black
#  amove   0.409022568  1.63909774
#  circle 0.002 fill black
#  amove   0.417543871  1.43609023
#  circle 0.002 fill black
#  amove   0.417543871  1.45112782
#  circle 0.002 fill black
#  amove   0.417543871  1.45864662
#  circle 0.002 fill black
#  amove   0.417543871  1.4962406
#  circle 0.002 fill black
#  amove   0.417543871  1.53383459
#  circle 0.002 fill black
#  amove   0.417543871  1.54887218
#  circle 0.002 fill black
#  amove   0.417543871  1.55639098
#  circle 0.002 fill black
#  amove   0.417543871  1.56390977
#  circle 0.002 fill black
#  amove   0.426065175  1.39097744
#  circle 0.002 fill black
#  amove   0.426065175  1.42857143
#  circle 0.002 fill black
#  amove   0.426065175  1.5112782
#  circle 0.002 fill black
#  amove   0.426065175  1.52631579
#  circle 0.002 fill black
#  amove   0.426065175  1.57142857
#  circle 0.002 fill black
#  amove   0.434586478  1.41353383
#  circle 0.002 fill black
#  amove   0.434586478  1.44360902
#  circle 0.002 fill black
#  amove   0.434586478  1.52631579
#  circle 0.002 fill black
#  amove   0.434586478  1.63157895
#  circle 0.002 fill black
#  amove   0.443107782  1.42857143
#  circle 0.002 fill black
#  amove   0.443107782  1.4962406
#  circle 0.002 fill black
#  amove   0.443107782  1.5112782
#  circle 0.002 fill black
#  amove   0.443107782  1.55639098
#  circle 0.002 fill black
#  amove   0.443107782  1.58646617
#  circle 0.002 fill black
#  amove   0.451629085  1.43609023
#  circle 0.002 fill black
#  amove   0.451629085  1.44360902
#  circle 0.002 fill black
#  amove   0.451629085  1.52631579
#  circle 0.002 fill black
#  amove   0.460150389  1.42857143
#  circle 0.002 fill black
#  amove   0.460150389  1.45112782
#  circle 0.002 fill black
#  amove   0.460150389  1.47368421
#  circle 0.002 fill black
#  amove   0.460150389  1.61654135
#  circle 0.002 fill black
#  amove   0.468671692  1.39849624
#  circle 0.002 fill black
#  amove   0.468671692  1.44360902
#  circle 0.002 fill black
#  amove   0.468671692  1.45112782
#  circle 0.002 fill black
#  amove   0.468671692  1.5037594
#  circle 0.002 fill black
#  amove   0.468671692  1.51879699
#  circle 0.002 fill black
#  amove   0.468671692  1.54135338
#  circle 0.002 fill black
#  amove   0.477192996  1.39849624
#  circle 0.002 fill black
#  amove   0.477192996  1.42105263
#  circle 0.002 fill black
#  amove   0.477192996  1.48120301
#  circle 0.002 fill black
#  amove   0.477192996  1.4887218
#  circle 0.002 fill black
#  amove   0.477192996  1.5037594
#  circle 0.002 fill black
#  amove   0.485714299  1.43609023
#  circle 0.002 fill black
#  amove   0.485714299  1.45864662
#  circle 0.002 fill black
#  amove   0.485714299  1.51879699
#  circle 0.002 fill black
#  amove   0.494235603  1.36842105
#  circle 0.002 fill black
#  amove   0.494235603  1.4887218
#  circle 0.002 fill black
#  amove   0.494235603  1.4962406
#  circle 0.002 fill black
#  amove   0.494235603  1.5112782
#  circle 0.002 fill black
#  amove   0.494235603  1.54887218
#  circle 0.002 fill black
#  amove   0.502756906  1.42105263
#  circle 0.002 fill black
#  amove   0.502756906  1.44360902
#  circle 0.002 fill black
#  amove   0.502756906  1.4962406
#  circle 0.002 fill black
#  amove   0.502756906  1.53383459
#  circle 0.002 fill black
#  amove   0.51127821  1.43609023
#  circle 0.002 fill black
#  amove   0.51127821  1.5037594
#  circle 0.002 fill black
#  amove   0.51127821  1.55639098
#  circle 0.002 fill black
#  amove   0.51127821  1.59398496
#  circle 0.002 fill black
#  amove   0.51127821  1.63909774
#  circle 0.002 fill black
#  amove   0.519799513  1.36842105
#  circle 0.002 fill black
#  amove   0.519799513  1.38345865
#  circle 0.002 fill black
#  amove   0.519799513  1.39097744
#  circle 0.002 fill black
#  amove   0.519799513  1.40601504
#  circle 0.002 fill black
#  amove   0.519799513  1.5037594
#  circle 0.002 fill black
#  amove   0.519799513  1.52631579
#  circle 0.002 fill black
#  amove   0.528320817  1.47368421
#  circle 0.002 fill black
#  amove   0.528320817  1.4887218
#  circle 0.002 fill black
#  amove   0.528320817  1.52631579
#  circle 0.002 fill black
#  amove   0.528320817  1.56390977
#  circle 0.002 fill black
#  amove   0.528320817  1.62406015
#  circle 0.002 fill black
#  amove   0.53684212  1.38345865
#  circle 0.002 fill black
#  amove   0.53684212  1.39849624
#  circle 0.002 fill black
#  amove   0.53684212  1.45112782
#  circle 0.002 fill black
#  amove   0.53684212  1.45864662
#  circle 0.002 fill black
#  amove   0.53684212  1.47368421
#  circle 0.002 fill black
#  amove   0.53684212  1.56390977
#  circle 0.002 fill black
#  amove   0.53684212  1.59398496
#  circle 0.002 fill black
#  amove   0.545363424  1.40601504
#  circle 0.002 fill black
#  amove   0.545363424  1.4887218
#  circle 0.002 fill black
#  amove   0.545363424  1.5112782
#  circle 0.002 fill black
#  amove   0.545363424  1.57894737
#  circle 0.002 fill black
#  amove   0.553884727  1.39849624
#  circle 0.002 fill black
#  amove   0.553884727  1.43609023
#  circle 0.002 fill black
#  amove   0.553884727  1.47368421
#  circle 0.002 fill black
#  amove   0.553884727  1.53383459
#  circle 0.002 fill black
#  amove   0.553884727  1.58646617
#  circle 0.002 fill black
#  amove   0.562406031  1.45112782
#  circle 0.002 fill black
#  amove   0.562406031  1.46616541
#  circle 0.002 fill black
#  amove   0.562406031  1.4962406
#  circle 0.002 fill black
#  amove   0.562406031  1.5037594
#  circle 0.002 fill black
#  amove   0.562406031  1.5112782
#  circle 0.002 fill black
#  amove   0.562406031  1.52631579
#  circle 0.002 fill black
#  amove   0.562406031  1.56390977
#  circle 0.002 fill black
#  amove   0.562406031  1.63909774
#  circle 0.002 fill black
#  amove   0.570927334  1.42857143
#  circle 0.002 fill black
#  amove   0.570927334  1.45112782
#  circle 0.002 fill black
#  amove   0.570927334  1.46616541
#  circle 0.002 fill black
#  amove   0.570927334  1.47368421
#  circle 0.002 fill black
#  amove   0.570927334  1.5112782
#  circle 0.002 fill black
#  amove   0.570927334  1.54135338
#  circle 0.002 fill black
#  amove   0.570927334  1.55639098
#  circle 0.002 fill black
#  amove   0.570927334  1.57142857
#  circle 0.002 fill black
#  amove   0.570927334  1.57894737
#  circle 0.002 fill black
#  amove   0.579448638  1.42857143
#  circle 0.002 fill black
#  amove   0.579448638  1.47368421
#  circle 0.002 fill black
#  amove   0.579448638  1.48120301
#  circle 0.002 fill black
#  amove   0.579448638  1.4962406
#  circle 0.002 fill black
#  amove   0.579448638  1.5037594
#  circle 0.002 fill black
#  amove   0.579448638  1.54135338
#  circle 0.002 fill black
#  amove   0.579448638  1.54887218
#  circle 0.002 fill black
#  amove   0.579448638  1.60902256
#  circle 0.002 fill black
#  amove   0.587969941  1.45864662
#  circle 0.002 fill black
#  amove   0.587969941  1.47368421
#  circle 0.002 fill black
#  amove   0.587969941  1.4962406
#  circle 0.002 fill black
#  amove   0.587969941  1.52631579
#  circle 0.002 fill black
#  amove   0.596491245  1.46616541
#  circle 0.002 fill black
#  amove   0.596491245  1.4887218
#  circle 0.002 fill black
#  amove   0.596491245  1.4962406
#  circle 0.002 fill black
#  amove   0.596491245  1.5037594
#  circle 0.002 fill black
#  amove   0.596491245  1.51879699
#  circle 0.002 fill black
#  amove   0.596491245  1.55639098
#  circle 0.002 fill black
#  amove   0.605012548  1.46616541
#  circle 0.002 fill black
#  amove   0.605012548  1.54887218
#  circle 0.002 fill black
#  amove   0.613533852  1.45112782
#  circle 0.002 fill black
#  amove   0.613533852  1.4962406
#  circle 0.002 fill black
#  amove   0.613533852  1.5037594
#  circle 0.002 fill black
#  amove   0.613533852  1.53383459
#  circle 0.002 fill black
#  amove   0.613533852  1.54135338
#  circle 0.002 fill black
#  amove   0.622055155  1.40601504
#  circle 0.002 fill black
#  amove   0.622055155  1.45864662
#  circle 0.002 fill black
#  amove   0.622055155  1.46616541
#  circle 0.002 fill black
#  amove   0.622055155  1.48120301
#  circle 0.002 fill black
#  amove   0.622055155  1.4962406
#  circle 0.002 fill black
#  amove   0.622055155  1.5112782
#  circle 0.002 fill black
#  amove   0.622055155  1.54135338
#  circle 0.002 fill black
#  amove   0.622055155  1.54887218
#  circle 0.002 fill black
#  amove   0.622055155  1.57142857
#  circle 0.002 fill black
#  amove   0.622055155  1.58646617
#  circle 0.002 fill black
#  amove   0.622055155  1.59398496
#  circle 0.002 fill black
#  amove   0.630576459  1.42105263
#  circle 0.002 fill black
#  amove   0.630576459  1.45112782
#  circle 0.002 fill black
#  amove   0.630576459  1.5037594
#  circle 0.002 fill black
#  amove   0.630576459  1.5112782
#  circle 0.002 fill black
#  amove   0.630576459  1.53383459
#  circle 0.002 fill black
#  amove   0.630576459  1.56390977
#  circle 0.002 fill black
#  amove   0.630576459  1.59398496
#  circle 0.002 fill black
#  amove   0.630576459  1.61654135
#  circle 0.002 fill black
#  amove   0.639097762  1.44360902
#  circle 0.002 fill black
#  amove   0.639097762  1.51879699
#  circle 0.002 fill black
#  amove   0.639097762  1.53383459
#  circle 0.002 fill black
#  amove   0.639097762  1.57894737
#  circle 0.002 fill black
#  amove   0.647619066  1.39097744
#  circle 0.002 fill black
#  amove   0.647619066  1.41353383
#  circle 0.002 fill black
#  amove   0.647619066  1.42857143
#  circle 0.002 fill black
#  amove   0.647619066  1.46616541
#  circle 0.002 fill black
#  amove   0.647619066  1.52631579
#  circle 0.002 fill black
#  amove   0.647619066  1.54887218
#  circle 0.002 fill black
#  amove   0.656140369  1.4962406
#  circle 0.002 fill black
#  amove   0.656140369  1.5037594
#  circle 0.002 fill black
#  amove   0.656140369  1.53383459
#  circle 0.002 fill black
#  amove   0.656140369  1.56390977
#  circle 0.002 fill black
#  amove   0.664661673  1.42857143
#  circle 0.002 fill black
#  amove   0.664661673  1.43609023
#  circle 0.002 fill black
#  amove   0.664661673  1.48120301
#  circle 0.002 fill black
#  amove   0.664661673  1.4962406
#  circle 0.002 fill black
#  amove   0.664661673  1.5037594
#  circle 0.002 fill black
#  amove   0.664661673  1.54887218
#  circle 0.002 fill black
#  amove   0.664661673  1.57894737
#  circle 0.002 fill black
#  amove   0.673182976  1.44360902
#  circle 0.002 fill black
#  amove   0.673182976  1.47368421
#  circle 0.002 fill black
#  amove   0.673182976  1.48120301
#  circle 0.002 fill black
#  amove   0.673182976  1.4887218
#  circle 0.002 fill black
#  amove   0.673182976  1.4962406
#  circle 0.002 fill black
#  amove   0.673182976  1.57142857
#  circle 0.002 fill black
#  amove   0.68170428  1.4887218
#  circle 0.002 fill black
#  amove   0.68170428  1.51879699
#  circle 0.002 fill black
#  amove   0.68170428  1.54135338
#  circle 0.002 fill black
#  amove   0.68170428  1.60150376
#  circle 0.002 fill black
#  amove   0.690225583  1.35338346
#  circle 0.002 fill black
#  amove   0.690225583  1.45112782
#  circle 0.002 fill black
#  amove   0.690225583  1.46616541
#  circle 0.002 fill black
#  amove   0.690225583  1.47368421
#  circle 0.002 fill black
#  amove   0.690225583  1.61654135
#  circle 0.002 fill black
#  amove   0.698746887  1.48120301
#  circle 0.002 fill black
#  amove   0.698746887  1.54135338
#  circle 0.002 fill black
#  amove   0.698746887  1.55639098
#  circle 0.002 fill black
#  amove   0.70726819  1.46616541
#  circle 0.002 fill black
#  amove   0.70726819  1.4962406
#  circle 0.002 fill black
#  amove   0.70726819  1.54887218
#  circle 0.002 fill black
#  amove   0.70726819  1.58646617
#  circle 0.002 fill black
#  amove   0.715789494  1.45864662
#  circle 0.002 fill black
#  amove   0.715789494  1.46616541
#  circle 0.002 fill black
#  amove   0.715789494  1.53383459
#  circle 0.002 fill black
#  amove   0.715789494  1.54887218
#  circle 0.002 fill black
#  amove   0.724310797  1.41353383
#  circle 0.002 fill black
#  amove   0.724310797  1.4962406
#  circle 0.002 fill black
#  amove   0.724310797  1.5112782
#  circle 0.002 fill black
#  amove   0.724310797  1.52631579
#  circle 0.002 fill black
#  amove   0.724310797  1.53383459
#  circle 0.002 fill black
#  amove   0.724310797  1.54135338
#  circle 0.002 fill black
#  amove   0.724310797  1.60902256
#  circle 0.002 fill black
#  amove   0.732832101  1.42857143
#  circle 0.002 fill black
#  amove   0.732832101  1.43609023
#  circle 0.002 fill black
#  amove   0.732832101  1.44360902
#  circle 0.002 fill black
#  amove   0.732832101  1.46616541
#  circle 0.002 fill black
#  amove   0.732832101  1.4887218
#  circle 0.002 fill black
#  amove   0.732832101  1.53383459
#  circle 0.002 fill black
#  amove   0.741353404  1.33082707
#  circle 0.002 fill black
#  amove   0.741353404  1.42105263
#  circle 0.002 fill black
#  amove   0.741353404  1.44360902
#  circle 0.002 fill black
#  amove   0.741353404  1.4887218
#  circle 0.002 fill black
#  amove   0.741353404  1.4962406
#  circle 0.002 fill black
#  amove   0.741353404  1.5037594
#  circle 0.002 fill black
#  amove   0.741353404  1.51879699
#  circle 0.002 fill black
#  amove   0.741353404  1.54887218
#  circle 0.002 fill black
#  amove   0.749874708  1.42105263
#  circle 0.002 fill black
#  amove   0.749874708  1.5112782
#  circle 0.002 fill black
#  amove   0.749874708  1.55639098
#  circle 0.002 fill black
#  amove   0.758396011  1.40601504
#  circle 0.002 fill black
#  amove   0.758396011  1.45112782
#  circle 0.002 fill black
#  amove   0.758396011  1.4887218
#  circle 0.002 fill black
#  amove   0.758396011  1.5037594
#  circle 0.002 fill black
#  amove   0.758396011  1.5112782
#  circle 0.002 fill black
#  amove   0.758396011  1.52631579
#  circle 0.002 fill black
#  amove   0.758396011  1.53383459
#  circle 0.002 fill black
#  amove   0.758396011  1.59398496
#  circle 0.002 fill black
#  amove   0.758396011  1.60902256
#  circle 0.002 fill black
#  amove   0.766917315  1.45864662
#  circle 0.002 fill black
#  amove   0.766917315  1.4887218
#  circle 0.002 fill black
#  amove   0.766917315  1.60150376
#  circle 0.002 fill black
#  amove   0.766917315  1.63157895
#  circle 0.002 fill black
#  amove   0.775438618  1.33082707
#  circle 0.002 fill black
#  amove   0.775438618  1.44360902
#  circle 0.002 fill black
#  amove   0.775438618  1.45864662
#  circle 0.002 fill black
#  amove   0.775438618  1.47368421
#  circle 0.002 fill black
#  amove   0.775438618  1.4962406
#  circle 0.002 fill black
#  amove   0.775438618  1.5112782
#  circle 0.002 fill black
#  amove   0.775438618  1.51879699
#  circle 0.002 fill black
#  amove   0.775438618  1.54135338
#  circle 0.002 fill black
#  amove   0.775438618  1.54887218
#  circle 0.002 fill black
#  amove   0.775438618  1.56390977
#  circle 0.002 fill black
#  amove   0.775438618  1.58646617
#  circle 0.002 fill black
#  amove   0.783959922  1.39849624
#  circle 0.002 fill black
#  amove   0.783959922  1.51879699
#  circle 0.002 fill black
#  amove   0.783959922  1.52631579
#  circle 0.002 fill black
#  amove   0.783959922  1.53383459
#  circle 0.002 fill black
#  amove   0.792481225  1.41353383
#  circle 0.002 fill black
#  amove   0.792481225  1.42857143
#  circle 0.002 fill black
#  amove   0.792481225  1.45112782
#  circle 0.002 fill black
#  amove   0.792481225  1.48120301
#  circle 0.002 fill black
#  amove   0.792481225  1.4962406
#  circle 0.002 fill black
#  amove   0.792481225  1.5112782
#  circle 0.002 fill black
#  amove   0.792481225  1.52631579
#  circle 0.002 fill black
#  amove   0.792481225  1.60902256
#  circle 0.002 fill black
#  amove   0.801002529  1.5112782
#  circle 0.002 fill black
#  amove   0.809523832  1.44360902
#  circle 0.002 fill black
#  amove   0.809523832  1.45112782
#  circle 0.002 fill black
#  amove   0.809523832  1.46616541
#  circle 0.002 fill black
#  amove   0.809523832  1.47368421
#  circle 0.002 fill black
#  amove   0.809523832  1.4962406
#  circle 0.002 fill black
#  amove   0.809523832  1.51879699
#  circle 0.002 fill black
#  amove   0.809523832  1.53383459
#  circle 0.002 fill black
#  amove   0.809523832  1.55639098
#  circle 0.002 fill black
#  amove   0.809523832  1.57894737
#  circle 0.002 fill black
#  amove   0.809523832  1.60902256
#  circle 0.002 fill black
#  amove   0.818045136  1.40601504
#  circle 0.002 fill black
#  amove   0.818045136  1.41353383
#  circle 0.002 fill black
#  amove   0.818045136  1.44360902
#  circle 0.002 fill black
#  amove   0.818045136  1.45864662
#  circle 0.002 fill black
#  amove   0.818045136  1.47368421
#  circle 0.002 fill black
#  amove   0.818045136  1.54135338
#  circle 0.002 fill black
#  amove   0.818045136  1.56390977
#  circle 0.002 fill black
#  amove   0.818045136  1.58646617
#  circle 0.002 fill black
#  amove   0.826566439  1.45112782
#  circle 0.002 fill black
#  amove   0.826566439  1.4962406
#  circle 0.002 fill black
#  amove   0.826566439  1.51879699
#  circle 0.002 fill black
#  amove   0.826566439  1.54135338
#  circle 0.002 fill black
#  amove   0.835087743  1.39097744
#  circle 0.002 fill black
#  amove   0.835087743  1.45112782
#  circle 0.002 fill black
#  amove   0.835087743  1.48120301
#  circle 0.002 fill black
#  amove   0.835087743  1.4962406
#  circle 0.002 fill black
#  amove   0.835087743  1.57894737
#  circle 0.002 fill black
#  amove   0.843609046  1.40601504
#  circle 0.002 fill black
#  amove   0.843609046  1.44360902
#  circle 0.002 fill black
#  amove   0.843609046  1.4887218
#  circle 0.002 fill black
#  amove   0.843609046  1.4962406
#  circle 0.002 fill black
#  amove   0.843609046  1.5037594
#  circle 0.002 fill black
#  amove   0.843609046  1.52631579
#  circle 0.002 fill black
#  amove   0.843609046  1.53383459
#  circle 0.002 fill black
#  amove   0.843609046  1.62406015
#  circle 0.002 fill black
#  amove   0.843609046  1.65413534
#  circle 0.002 fill black
#  amove   0.85213035  1.56390977
#  circle 0.002 fill black
#  amove   0.860651653  1.37593985
#  circle 0.002 fill black
#  amove   0.860651653  1.48120301
#  circle 0.002 fill black
#  amove   0.860651653  1.5037594
#  circle 0.002 fill black
#  amove   0.860651653  1.5112782
#  circle 0.002 fill black
#  amove   0.860651653  1.52631579
#  circle 0.002 fill black
#  amove   0.860651653  1.54887218
#  circle 0.002 fill black
#  amove   0.860651653  1.57894737
#  circle 0.002 fill black
#  amove   0.869172957  1.40601504
#  circle 0.002 fill black
#  amove   0.869172957  1.43609023
#  circle 0.002 fill black
#  amove   0.869172957  1.44360902
#  circle 0.002 fill black
#  amove   0.869172957  1.46616541
#  circle 0.002 fill black
#  amove   0.869172957  1.5037594
#  circle 0.002 fill black
#  amove   0.869172957  1.55639098
#  circle 0.002 fill black
#  amove   0.869172957  1.56390977
#  circle 0.002 fill black
#  amove   0.87769426  1.44360902
#  circle 0.002 fill black
#  amove   0.87769426  1.45112782
#  circle 0.002 fill black
#  amove   0.87769426  1.46616541
#  circle 0.002 fill black
#  amove   0.87769426  1.52631579
#  circle 0.002 fill black
#  amove   0.87769426  1.53383459
#  circle 0.002 fill black
#  amove   0.87769426  1.54887218
#  circle 0.002 fill black
#  amove   0.87769426  1.58646617
#  circle 0.002 fill black
#  amove   0.87769426  1.67669173
#  circle 0.002 fill black
#  amove   0.886215564  1.45112782
#  circle 0.002 fill black
#  amove   0.886215564  1.4962406
#  circle 0.002 fill black
#  amove   0.886215564  1.53383459
#  circle 0.002 fill black
#  amove   0.894736867  1.44360902
#  circle 0.002 fill black
#  amove   0.894736867  1.45864662
#  circle 0.002 fill black
#  amove   0.894736867  1.48120301
#  circle 0.002 fill black
#  amove   0.894736867  1.4887218
#  circle 0.002 fill black
#  amove   0.894736867  1.5037594
#  circle 0.002 fill black
#  amove   0.894736867  1.52631579
#  circle 0.002 fill black
#  amove   0.903258171  1.42857143
#  circle 0.002 fill black
#  amove   0.903258171  1.4887218
#  circle 0.002 fill black
#  amove   0.903258171  1.5037594
#  circle 0.002 fill black
#  amove   0.903258171  1.5112782
#  circle 0.002 fill black
#  amove   0.903258171  1.54135338
#  circle 0.002 fill black
#  amove   0.903258171  1.57894737
#  circle 0.002 fill black
#  amove   0.903258171  1.58646617
#  circle 0.002 fill black
#  amove   0.903258171  1.60902256
#  circle 0.002 fill black
#  amove   0.911779474  1.39849624
#  circle 0.002 fill black
#  amove   0.911779474  1.45112782
#  circle 0.002 fill black
#  amove   0.911779474  1.5037594
#  circle 0.002 fill black
#  amove   0.911779474  1.5112782
#  circle 0.002 fill black
#  amove   0.911779474  1.51879699
#  circle 0.002 fill black
#  amove   0.911779474  1.55639098
#  circle 0.002 fill black
#  amove   0.911779474  1.61654135
#  circle 0.002 fill black
#  amove   0.920300778  1.42857143
#  circle 0.002 fill black
#  amove   0.920300778  1.45864662
#  circle 0.002 fill black
#  amove   0.920300778  1.46616541
#  circle 0.002 fill black
#  amove   0.920300778  1.48120301
#  circle 0.002 fill black
#  amove   0.920300778  1.52631579
#  circle 0.002 fill black
#  amove   0.920300778  1.54135338
#  circle 0.002 fill black
#  amove   0.928822081  1.44360902
#  circle 0.002 fill black
#  amove   0.928822081  1.47368421
#  circle 0.002 fill black
#  amove   0.928822081  1.4962406
#  circle 0.002 fill black
#  amove   0.928822081  1.52631579
#  circle 0.002 fill black
#  amove   0.928822081  1.54887218
#  circle 0.002 fill black
#  amove   0.928822081  1.55639098
#  circle 0.002 fill black
#  amove   0.937343385  1.42857143
#  circle 0.002 fill black
#  amove   0.937343385  1.46616541
#  circle 0.002 fill black
#  amove   0.937343385  1.4887218
#  circle 0.002 fill black
#  amove   0.937343385  1.5112782
#  circle 0.002 fill black
#  amove   0.937343385  1.51879699
#  circle 0.002 fill black
#  amove   0.937343385  1.53383459
#  circle 0.002 fill black
#  amove   0.937343385  1.54135338
#  circle 0.002 fill black
#  amove   0.945864688  1.42857143
#  circle 0.002 fill black
#  amove   0.945864688  1.44360902
#  circle 0.002 fill black
#  amove   0.945864688  1.52631579
#  circle 0.002 fill black
#  amove   0.945864688  1.53383459
#  circle 0.002 fill black
#  amove   0.945864688  1.54135338
#  circle 0.002 fill black
#  amove   0.954385992  1.40601504
#  circle 0.002 fill black
#  amove   0.962907295  1.37593985
#  circle 0.002 fill black
#  amove   0.962907295  1.47368421
#  circle 0.002 fill black
#  amove   0.962907295  1.48120301
#  circle 0.002 fill black
#  amove   0.962907295  1.4962406
#  circle 0.002 fill black
#  amove   0.962907295  1.52631579
#  circle 0.002 fill black
#  amove   0.962907295  1.54887218
#  circle 0.002 fill black
#  amove   0.962907295  1.57142857
#  circle 0.002 fill black
#  amove   0.971428599  1.41353383
#  circle 0.002 fill black
#  amove   0.971428599  1.45112782
#  circle 0.002 fill black
#  amove   0.971428599  1.45864662
#  circle 0.002 fill black
#  amove   0.971428599  1.4962406
#  circle 0.002 fill black
#  amove   0.971428599  1.54135338
#  circle 0.002 fill black
#  amove   0.979949902  1.46616541
#  circle 0.002 fill black
#  amove   0.979949902  1.4887218
#  circle 0.002 fill black
#  amove   0.979949902  1.4962406
#  circle 0.002 fill black
#  amove   0.979949902  1.5037594
#  circle 0.002 fill black
#  amove   0.979949902  1.56390977
#  circle 0.002 fill black
#  amove   0.988471206  1.45112782
#  circle 0.002 fill black
#  amove   0.988471206  1.4887218
#  circle 0.002 fill black
#  amove   0.988471206  1.5112782
#  circle 0.002 fill black
#  amove   0.988471206  1.53383459
#  circle 0.002 fill black
#  amove   0.988471206  1.56390977
#  circle 0.002 fill black
#  amove   0.996992509  1.33834586
#  circle 0.002 fill black
#  amove   0.996992509  1.43609023
#  circle 0.002 fill black
#  amove   0.996992509  1.57894737
#  circle 0.002 fill black
#  amove   0.996992509  1.61654135
#  circle 0.002 fill black
#  amove   0.996992509  1.65413534
#  circle 0.002 fill black
#  amove   1.00551381  1.44360902
#  circle 0.002 fill black
#  amove   1.00551381  1.45112782
#  circle 0.002 fill black
#  amove   1.00551381  1.45864662
#  circle 0.002 fill black
#  amove   1.00551381  1.47368421
#  circle 0.002 fill black
#  amove   1.00551381  1.48120301
#  circle 0.002 fill black
#  amove   1.00551381  1.5112782
#  circle 0.002 fill black
#  amove   1.00551381  1.53383459
#  circle 0.002 fill black
#  amove   1.00551381  1.57142857
#  circle 0.002 fill black
#  amove   1.01403512  1.41353383
#  circle 0.002 fill black
#  amove   1.01403512  1.46616541
#  circle 0.002 fill black
#  amove   1.01403512  1.53383459
#  circle 0.002 fill black
#  amove   1.01403512  1.54887218
#  circle 0.002 fill black
#  amove   1.01403512  1.57142857
#  circle 0.002 fill black
#  amove   1.02255642  1.44360902
#  circle 0.002 fill black
#  amove   1.02255642  1.47368421
#  circle 0.002 fill black
#  amove   1.02255642  1.48120301
#  circle 0.002 fill black
#  amove   1.02255642  1.54135338
#  circle 0.002 fill black
#  amove   1.02255642  1.60150376
#  circle 0.002 fill black
#  amove   1.02255642  1.63909774
#  circle 0.002 fill black
#  amove   1.03107772  1.42105263
#  circle 0.002 fill black
#  amove   1.03107772  1.45864662
#  circle 0.002 fill black
#  amove   1.03107772  1.47368421
#  circle 0.002 fill black
#  amove   1.03107772  1.48120301
#  circle 0.002 fill black
#  amove   1.03107772  1.57894737
#  circle 0.002 fill black
#  amove   1.03107772  1.62406015
#  circle 0.002 fill black
#  amove   1.03959903  1.39097744
#  circle 0.002 fill black
#  amove   1.03959903  1.48120301
#  circle 0.002 fill black
#  amove   1.03959903  1.53383459
#  circle 0.002 fill black
#  amove   1.03959903  1.58646617
#  circle 0.002 fill black
#  amove   1.04812033  1.52631579
#  circle 0.002 fill black
#  amove   1.05664163  1.41353383
#  circle 0.002 fill black
#  amove   1.05664163  1.42857143
#  circle 0.002 fill black
#  amove   1.05664163  1.46616541
#  circle 0.002 fill black
#  amove   1.05664163  1.55639098
#  circle 0.002 fill black
#  amove   1.06516294  1.46616541
#  circle 0.002 fill black
#  amove   1.06516294  1.4887218
#  circle 0.002 fill black
#  amove   1.06516294  1.4962406
#  circle 0.002 fill black
#  amove   1.06516294  1.5037594
#  circle 0.002 fill black
#  amove   1.06516294  1.51879699
#  circle 0.002 fill black
#  amove   1.06516294  1.60902256
#  circle 0.002 fill black
#  amove   1.07368424  1.44360902
#  circle 0.002 fill black
#  amove   1.07368424  1.48120301
#  circle 0.002 fill black
#  amove   1.07368424  1.4962406
#  circle 0.002 fill black
#  amove   1.07368424  1.5037594
#  circle 0.002 fill black
#  amove   1.07368424  1.53383459
#  circle 0.002 fill black
#  amove   1.07368424  1.54135338
#  circle 0.002 fill black
#  amove   1.07368424  1.57142857
#  circle 0.002 fill black
#  amove   1.08220554  1.42857143
#  circle 0.002 fill black
#  amove   1.08220554  1.47368421
#  circle 0.002 fill black
#  amove   1.08220554  1.51879699
#  circle 0.002 fill black
#  amove   1.08220554  1.53383459
#  circle 0.002 fill black
#  amove   1.08220554  1.54135338
#  circle 0.002 fill black
#  amove   1.09072685  1.43609023
#  circle 0.002 fill black
#  amove   1.09072685  1.47368421
#  circle 0.002 fill black
#  amove   1.09072685  1.4887218
#  circle 0.002 fill black
#  amove   1.09072685  1.5112782
#  circle 0.002 fill black
#  amove   1.09072685  1.51879699
#  circle 0.002 fill black
#  amove   1.09072685  1.56390977
#  circle 0.002 fill black
#  amove   1.09924815  1.41353383
#  circle 0.002 fill black
#  amove   1.09924815  1.45112782
#  circle 0.002 fill black
#  amove   1.09924815  1.48120301
#  circle 0.002 fill black
#  amove   1.09924815  1.4887218
#  circle 0.002 fill black
#  amove   1.09924815  1.4962406
#  circle 0.002 fill black
#  amove   1.09924815  1.52631579
#  circle 0.002 fill black
#  amove   1.09924815  1.54135338
#  circle 0.002 fill black
#  amove   1.10776945  1.43609023
#  circle 0.002 fill black
#  amove   1.10776945  1.47368421
#  circle 0.002 fill black
#  amove   1.10776945  1.4887218
#  circle 0.002 fill black
#  amove   1.10776945  1.4962406
#  circle 0.002 fill black
#  amove   1.10776945  1.5037594
#  circle 0.002 fill black
#  amove   1.10776945  1.5112782
#  circle 0.002 fill black
#  amove   1.10776945  1.54135338
#  circle 0.002 fill black
#  amove   1.10776945  1.54887218
#  circle 0.002 fill black
#  amove   1.11629076  1.48120301
#  circle 0.002 fill black
#  amove   1.11629076  1.5037594
#  circle 0.002 fill black
#  amove   1.11629076  1.51879699
#  circle 0.002 fill black
#  amove   1.12481206  1.45112782
#  circle 0.002 fill black
#  amove   1.12481206  1.48120301
#  circle 0.002 fill black
#  amove   1.12481206  1.51879699
#  circle 0.002 fill black
#  amove   1.12481206  1.54135338
#  circle 0.002 fill black
#  amove   1.12481206  1.56390977
#  circle 0.002 fill black
#  amove   1.13333337  1.43609023
#  circle 0.002 fill black
#  amove   1.13333337  1.46616541
#  circle 0.002 fill black
#  amove   1.13333337  1.52631579
#  circle 0.002 fill black
#  amove   1.13333337  1.54887218
#  circle 0.002 fill black
#  amove   1.13333337  1.56390977
#  circle 0.002 fill black
#  amove   1.14185467  1.46616541
#  circle 0.002 fill black
#  amove   1.14185467  1.4887218
#  circle 0.002 fill black
#  amove   1.14185467  1.5037594
#  circle 0.002 fill black
#  amove   1.14185467  1.52631579
#  circle 0.002 fill black
#  amove   1.14185467  1.54135338
#  circle 0.002 fill black
#  amove   1.14185467  1.61654135
#  circle 0.002 fill black
#  amove   1.15037597  1.36090226
#  circle 0.002 fill black
#  amove   1.15037597  1.41353383
#  circle 0.002 fill black
#  amove   1.15037597  1.43609023
#  circle 0.002 fill black
#  amove   1.15037597  1.51879699
#  circle 0.002 fill black
#  amove   1.15037597  1.53383459
#  circle 0.002 fill black
#  amove   1.15889728  1.5112782
#  circle 0.002 fill black
#  amove   1.15889728  1.51879699
#  circle 0.002 fill black
#  amove   1.15889728  1.52631579
#  circle 0.002 fill black
#  amove   1.15889728  1.54135338
#  circle 0.002 fill black
#  amove   1.15889728  1.57894737
#  circle 0.002 fill black
#  amove   1.16741858  1.42105263
#  circle 0.002 fill black
#  amove   1.16741858  1.43609023
#  circle 0.002 fill black
#  amove   1.16741858  1.47368421
#  circle 0.002 fill black
#  amove   1.16741858  1.4887218
#  circle 0.002 fill black
#  amove   1.16741858  1.56390977
#  circle 0.002 fill black
#  amove   1.17593988  1.4887218
#  circle 0.002 fill black
#  amove   1.17593988  1.4962406
#  circle 0.002 fill black
#  amove   1.17593988  1.5112782
#  circle 0.002 fill black
#  amove   1.17593988  1.53383459
#  circle 0.002 fill black
#  amove   1.17593988  1.54887218
#  circle 0.002 fill black
#  amove   1.17593988  1.59398496
#  circle 0.002 fill black
#  amove   1.18446119  1.35338346
#  circle 0.002 fill black
#  amove   1.18446119  1.41353383
#  circle 0.002 fill black
#  amove   1.18446119  1.43609023
#  circle 0.002 fill black
#  amove   1.18446119  1.4887218
#  circle 0.002 fill black
#  amove   1.18446119  1.52631579
#  circle 0.002 fill black
#  amove   1.18446119  1.54135338
#  circle 0.002 fill black
#  amove   1.18446119  1.55639098
#  circle 0.002 fill black
#  amove   1.19298249  1.43609023
#  circle 0.002 fill black
#  amove   1.19298249  1.5037594
#  circle 0.002 fill black
#  amove   1.19298249  1.57894737
#  circle 0.002 fill black
#  amove   1.20150379  1.42857143
#  circle 0.002 fill black
#  amove   1.20150379  1.45864662
#  circle 0.002 fill black
#  amove   1.20150379  1.46616541
#  circle 0.002 fill black
#  amove   1.20150379  1.48120301
#  circle 0.002 fill black
#  amove   1.20150379  1.4962406
#  circle 0.002 fill black
#  amove   1.20150379  1.53383459
#  circle 0.002 fill black
#  amove   1.20150379  1.54135338
#  circle 0.002 fill black
#  amove   1.2100251  1.47368421
#  circle 0.002 fill black
#  amove   1.2100251  1.48120301
#  circle 0.002 fill black
#  amove   1.2100251  1.4887218
#  circle 0.002 fill black
#  amove   1.2100251  1.5037594
#  circle 0.002 fill black
#  amove   1.2100251  1.54887218
#  circle 0.002 fill black
#  amove   1.2100251  1.57894737
#  circle 0.002 fill black
#  amove   1.2100251  1.58646617
#  circle 0.002 fill black
#  amove   1.2100251  1.62406015
#  circle 0.002 fill black
#  amove   1.2185464  1.46616541
#  circle 0.002 fill black
#  amove   1.2270677  1.42105263
#  circle 0.002 fill black
#  amove   1.2270677  1.42857143
#  circle 0.002 fill black
#  amove   1.2270677  1.47368421
#  circle 0.002 fill black
#  amove   1.2270677  1.48120301
#  circle 0.002 fill black
#  amove   1.2270677  1.5037594
#  circle 0.002 fill black
#  amove   1.2270677  1.53383459
#  circle 0.002 fill black
#  amove   1.2270677  1.54135338
#  circle 0.002 fill black
#  amove   1.2270677  1.54887218
#  circle 0.002 fill black
#  amove   1.23558901  1.4887218
#  circle 0.002 fill black
#  amove   1.23558901  1.5037594
#  circle 0.002 fill black
#  amove   1.23558901  1.51879699
#  circle 0.002 fill black
#  amove   1.23558901  1.52631579
#  circle 0.002 fill black
#  amove   1.23558901  1.54135338
#  circle 0.002 fill black
#  amove   1.24411031  1.42857143
#  circle 0.002 fill black
#  amove   1.24411031  1.45112782
#  circle 0.002 fill black
#  amove   1.24411031  1.47368421
#  circle 0.002 fill black
#  amove   1.24411031  1.52631579
#  circle 0.002 fill black
#  amove   1.25263161  1.42105263
#  circle 0.002 fill black
#  amove   1.25263161  1.42857143
#  circle 0.002 fill black
#  amove   1.25263161  1.43609023
#  circle 0.002 fill black
#  amove   1.25263161  1.44360902
#  circle 0.002 fill black
#  amove   1.25263161  1.48120301
#  circle 0.002 fill black
#  amove   1.25263161  1.5112782
#  circle 0.002 fill black
#  amove   1.25263161  1.51879699
#  circle 0.002 fill black
#  amove   1.25263161  1.52631579
#  circle 0.002 fill black
#  amove   1.25263161  1.54135338
#  circle 0.002 fill black
#  amove   1.25263161  1.61654135
#  circle 0.002 fill black
#  amove   1.26115292  1.45112782
#  circle 0.002 fill black
#  amove   1.26115292  1.46616541
#  circle 0.002 fill black
#  amove   1.26115292  1.48120301
#  circle 0.002 fill black
#  amove   1.26115292  1.5037594
#  circle 0.002 fill black
#  amove   1.26115292  1.51879699
#  circle 0.002 fill black
#  amove   1.26115292  1.54135338
#  circle 0.002 fill black
#  amove   1.26115292  1.57142857
#  circle 0.002 fill black
#  amove   1.26967422  1.45864662
#  circle 0.002 fill black
#  amove   1.26967422  1.46616541
#  circle 0.002 fill black
#  amove   1.26967422  1.52631579
#  circle 0.002 fill black
#  amove   1.27819552  1.43609023
#  circle 0.002 fill black
#  amove   1.27819552  1.46616541
#  circle 0.002 fill black
#  amove   1.27819552  1.57894737
#  circle 0.002 fill black
#  amove   1.28671683  1.36842105
#  circle 0.002 fill black
#  amove   1.28671683  1.45112782
#  circle 0.002 fill black
#  amove   1.28671683  1.47368421
#  circle 0.002 fill black
#  amove   1.28671683  1.4887218
#  circle 0.002 fill black
#  amove   1.28671683  1.5112782
#  circle 0.002 fill black
#  amove   1.29523813  1.46616541
#  circle 0.002 fill black
#  amove   1.29523813  1.47368421
#  circle 0.002 fill black
#  amove   1.29523813  1.5037594
#  circle 0.002 fill black
#  amove   1.29523813  1.51879699
#  circle 0.002 fill black
#  amove   1.29523813  1.52631579
#  circle 0.002 fill black
#  amove   1.29523813  1.53383459
#  circle 0.002 fill black
#  amove   1.29523813  1.54887218
#  circle 0.002 fill black
#  amove   1.29523813  1.59398496
#  circle 0.002 fill black
#  amove   1.30375944  1.45864662
#  circle 0.002 fill black
#  amove   1.30375944  1.46616541
#  circle 0.002 fill black
#  amove   1.30375944  1.4962406
#  circle 0.002 fill black
#  amove   1.30375944  1.51879699
#  circle 0.002 fill black
#  amove   1.30375944  1.54135338
#  circle 0.002 fill black
#  amove   1.30375944  1.57894737
#  circle 0.002 fill black
#  amove   1.31228074  1.42857143
#  circle 0.002 fill black
#  amove   1.31228074  1.5037594
#  circle 0.002 fill black
#  amove   1.31228074  1.59398496
#  circle 0.002 fill black
#  amove   1.31228074  1.63909774
#  circle 0.002 fill black
#  amove   1.32080204  1.4887218
#  circle 0.002 fill black
#  amove   1.32080204  1.4962406
#  circle 0.002 fill black
#  amove   1.32080204  1.5037594
#  circle 0.002 fill black
#  amove   1.32080204  1.56390977
#  circle 0.002 fill black
#  amove   1.32932335  1.39849624
#  circle 0.002 fill black
#  amove   1.32932335  1.42105263
#  circle 0.002 fill black
#  amove   1.32932335  1.48120301
#  circle 0.002 fill black
#  amove   1.32932335  1.4887218
#  circle 0.002 fill black
#  amove   1.32932335  1.4962406
#  circle 0.002 fill black
#  amove   1.32932335  1.5037594
#  circle 0.002 fill black
#  amove   1.32932335  1.51879699
#  circle 0.002 fill black
#  amove   1.32932335  1.54135338
#  circle 0.002 fill black
#  amove   1.33784465  1.40601504
#  circle 0.002 fill black
#  amove   1.33784465  1.47368421
#  circle 0.002 fill black
#  amove   1.33784465  1.48120301
#  circle 0.002 fill black
#  amove   1.33784465  1.52631579
#  circle 0.002 fill black
#  amove   1.34636595  1.42857143
#  circle 0.002 fill black
#  amove   1.34636595  1.5037594
#  circle 0.002 fill black
#  amove   1.34636595  1.5112782
#  circle 0.002 fill black
#  amove   1.34636595  1.52631579
#  circle 0.002 fill black
#  amove   1.34636595  1.57142857
#  circle 0.002 fill black
#  amove   1.35488726  1.43609023
#  circle 0.002 fill black
#  amove   1.35488726  1.46616541
#  circle 0.002 fill black
#  amove   1.35488726  1.48120301
#  circle 0.002 fill black
#  amove   1.35488726  1.4887218
#  circle 0.002 fill black
#  amove   1.35488726  1.5037594
#  circle 0.002 fill black
#  amove   1.35488726  1.54135338
#  circle 0.002 fill black
#  amove   1.35488726  1.56390977
#  circle 0.002 fill black
#  amove   1.36340856  1.40601504
#  circle 0.002 fill black
#  amove   1.36340856  1.42105263
#  circle 0.002 fill black
#  amove   1.36340856  1.45864662
#  circle 0.002 fill black
#  amove   1.36340856  1.48120301
#  circle 0.002 fill black
#  amove   1.36340856  1.60150376
#  circle 0.002 fill black
#  amove   1.37192986  1.40601504
#  circle 0.002 fill black
#  amove   1.37192986  1.42857143
#  circle 0.002 fill black
#  amove   1.37192986  1.43609023
#  circle 0.002 fill black
#  amove   1.37192986  1.47368421
#  circle 0.002 fill black
#  amove   1.37192986  1.51879699
#  circle 0.002 fill black
#  amove   1.37192986  1.58646617
#  circle 0.002 fill black
#  amove   1.38045117  1.54135338
#  circle 0.002 fill black
#  amove   1.38045117  1.56390977
#  circle 0.002 fill black
#  amove   1.38045117  1.66165414
#  circle 0.002 fill black
#  amove   1.38897247  1.39097744
#  circle 0.002 fill black
#  amove   1.38897247  1.43609023
#  circle 0.002 fill black
#  amove   1.38897247  1.44360902
#  circle 0.002 fill black
#  amove   1.38897247  1.47368421
#  circle 0.002 fill black
#  amove   1.38897247  1.5037594
#  circle 0.002 fill black
#  amove   1.38897247  1.54135338
#  circle 0.002 fill black
#  amove   1.38897247  1.56390977
#  circle 0.002 fill black
#  amove   1.38897247  1.60150376
#  circle 0.002 fill black
#  amove   1.39749377  1.43609023
#  circle 0.002 fill black
#  amove   1.39749377  1.44360902
#  circle 0.002 fill black
#  amove   1.39749377  1.46616541
#  circle 0.002 fill black
#  amove   1.39749377  1.5112782
#  circle 0.002 fill black
#  amove   1.39749377  1.51879699
#  circle 0.002 fill black
#  amove   1.39749377  1.53383459
#  circle 0.002 fill black
#  amove   1.39749377  1.56390977
#  circle 0.002 fill black
#  amove   1.39749377  1.57142857
#  circle 0.002 fill black
#  amove   1.40601508  1.48120301
#  circle 0.002 fill black
#  amove   1.40601508  1.54135338
#  circle 0.002 fill black
#  amove   1.40601508  1.54887218
#  circle 0.002 fill black
#  amove   1.41453638  1.4962406
#  circle 0.002 fill black
#  amove   1.41453638  1.52631579
#  circle 0.002 fill black
#  amove   1.41453638  1.63157895
#  circle 0.002 fill black
#  amove   1.42305768  1.5037594
#  circle 0.002 fill black
#  amove   1.42305768  1.52631579
#  circle 0.002 fill black
#  amove   1.42305768  1.53383459
#  circle 0.002 fill black
#  amove   1.42305768  1.57142857
#  circle 0.002 fill black
#  amove   1.42305768  1.61654135
#  circle 0.002 fill black
#  amove   1.43157899  1.4887218
#  circle 0.002 fill black
#  amove   1.43157899  1.4962406
#  circle 0.002 fill black
#  amove   1.43157899  1.57142857
#  circle 0.002 fill black
#  amove   1.44010029  1.43609023
#  circle 0.002 fill black
#  amove   1.44010029  1.4962406
#  circle 0.002 fill black
#  amove   1.44010029  1.5037594
#  circle 0.002 fill black
#  amove   1.44010029  1.5112782
#  circle 0.002 fill black
#  amove   1.44010029  1.52631579
#  circle 0.002 fill black
#  amove   1.44010029  1.54887218
#  circle 0.002 fill black
#  amove   1.44010029  1.55639098
#  circle 0.002 fill black
#  amove   1.44862159  1.30827068
#  circle 0.002 fill black
#  amove   1.44862159  1.45112782
#  circle 0.002 fill black
#  amove   1.44862159  1.45864662
#  circle 0.002 fill black
#  amove   1.44862159  1.5112782
#  circle 0.002 fill black
#  amove   1.44862159  1.53383459
#  circle 0.002 fill black
#  amove   1.44862159  1.55639098
#  circle 0.002 fill black
#  amove   1.4571429  1.39849624
#  circle 0.002 fill black
#  amove   1.4571429  1.45112782
#  circle 0.002 fill black
#  amove   1.4571429  1.54135338
#  circle 0.002 fill black
#  amove   1.4571429  1.55639098
#  circle 0.002 fill black
#  amove   1.4656642  1.45112782
#  circle 0.002 fill black
#  amove   1.4656642  1.5112782
#  circle 0.002 fill black
#  amove   1.4656642  1.57142857
#  circle 0.002 fill black
#  amove   1.47418551  1.45864662
#  circle 0.002 fill black
#  amove   1.47418551  1.4887218
#  circle 0.002 fill black
#  amove   1.47418551  1.54887218
#  circle 0.002 fill black
#  amove   1.48270681  1.43609023
#  circle 0.002 fill black
#  amove   1.48270681  1.47368421
#  circle 0.002 fill black
#  amove   1.48270681  1.5037594
#  circle 0.002 fill black
#  amove   1.48270681  1.5112782
#  circle 0.002 fill black
#  amove   1.48270681  1.56390977
#  circle 0.002 fill black
#  amove   1.49122811  1.44360902
#  circle 0.002 fill black
#  amove   1.49122811  1.48120301
#  circle 0.002 fill black
#  amove   1.49122811  1.4962406
#  circle 0.002 fill black
#  amove   1.49974942  1.47368421
#  circle 0.002 fill black
#  amove   1.49974942  1.4962406
#  circle 0.002 fill black
#  amove   1.49974942  1.5112782
#  circle 0.002 fill black
#  amove   1.49974942  1.57894737
#  circle 0.002 fill black
#  amove   1.50827072  1.5037594
#  circle 0.002 fill black
#  amove   1.51679202  1.46616541
#  circle 0.002 fill black
#  amove   1.51679202  1.4887218
#  circle 0.002 fill black
#  amove   1.51679202  1.52631579
#  circle 0.002 fill black
#  amove   1.51679202  1.53383459
#  circle 0.002 fill black
#  amove   1.51679202  1.58646617
#  circle 0.002 fill black
#  amove   1.51679202  1.59398496
#  circle 0.002 fill black
#  amove   1.52531333  1.36090226
#  circle 0.002 fill black
#  amove   1.52531333  1.38345865
#  circle 0.002 fill black
#  amove   1.52531333  1.41353383
#  circle 0.002 fill black
#  amove   1.52531333  1.51879699
#  circle 0.002 fill black
#  amove   1.52531333  1.53383459
#  circle 0.002 fill black
#  amove   1.52531333  1.54135338
#  circle 0.002 fill black
#  amove   1.52531333  1.57894737
#  circle 0.002 fill black
#  amove   1.53383463  1.42105263
#  circle 0.002 fill black
#  amove   1.53383463  1.46616541
#  circle 0.002 fill black
#  amove   1.53383463  1.59398496
#  circle 0.002 fill black
#  amove   1.54235593  1.45864662
#  circle 0.002 fill black
#  amove   1.54235593  1.5037594
#  circle 0.002 fill black
#  amove   1.54235593  1.5112782
#  circle 0.002 fill black
#  amove   1.54235593  1.51879699
#  circle 0.002 fill black
#  amove   1.54235593  1.52631579
#  circle 0.002 fill black
#  amove   1.54235593  1.64661654
#  circle 0.002 fill black
#  amove   1.55087724  1.43609023
#  circle 0.002 fill black
#  amove   1.55087724  1.45112782
#  circle 0.002 fill black
#  amove   1.55087724  1.56390977
#  circle 0.002 fill black
#  amove   1.55087724  1.57894737
#  circle 0.002 fill black
#  amove   1.55939854  1.40601504
#  circle 0.002 fill black
#  amove   1.55939854  1.41353383
#  circle 0.002 fill black
#  amove   1.55939854  1.42105263
#  circle 0.002 fill black
#  amove   1.55939854  1.47368421
#  circle 0.002 fill black
#  amove   1.55939854  1.4962406
#  circle 0.002 fill black
#  amove   1.55939854  1.5112782
#  circle 0.002 fill black
#  amove   1.56791984  1.45112782
#  circle 0.002 fill black
#  amove   1.56791984  1.51879699
#  circle 0.002 fill black
#  amove   1.56791984  1.54135338
#  circle 0.002 fill black
#  amove   1.57644115  1.45112782
#  circle 0.002 fill black
#  amove   1.57644115  1.46616541
#  circle 0.002 fill black
#  amove   1.57644115  1.52631579
#  circle 0.002 fill black
#  amove   1.57644115  1.53383459
#  circle 0.002 fill black
#  amove   1.57644115  1.54135338
#  circle 0.002 fill black
#  amove   1.57644115  1.54887218
#  circle 0.002 fill black
#  amove   1.58496245  1.42857143
#  circle 0.002 fill black
#  amove   1.58496245  1.4962406
#  circle 0.002 fill black
#  amove   1.58496245  1.52631579
#  circle 0.002 fill black
#  amove   1.58496245  1.54887218
#  circle 0.002 fill black
#  amove   1.58496245  1.57142857
#  circle 0.002 fill black
#  amove   1.58496245  1.68421053
#  circle 0.002 fill black
#  amove   1.59348375  1.45864662
#  circle 0.002 fill black
#  amove   1.59348375  1.46616541
#  circle 0.002 fill black
#  amove   1.59348375  1.47368421
#  circle 0.002 fill black
#  amove   1.59348375  1.48120301
#  circle 0.002 fill black
#  amove   1.59348375  1.4962406
#  circle 0.002 fill black
#  amove   1.59348375  1.54135338
#  circle 0.002 fill black
#  amove   1.59348375  1.55639098
#  circle 0.002 fill black
#  amove   1.59348375  1.57142857
#  circle 0.002 fill black
#  amove   1.60200506  1.42105263
#  circle 0.002 fill black
#  amove   1.60200506  1.45864662
#  circle 0.002 fill black
#  amove   1.60200506  1.56390977
#  circle 0.002 fill black
#  amove   1.61052636  1.42105263
#  circle 0.002 fill black
#  amove   1.61052636  1.44360902
#  circle 0.002 fill black
#  amove   1.61052636  1.4887218
#  circle 0.002 fill black
#  amove   1.61052636  1.5037594
#  circle 0.002 fill black
#  amove   1.61052636  1.51879699
#  circle 0.002 fill black
#  amove   1.61904766  1.44360902
#  circle 0.002 fill black
#  amove   1.61904766  1.5037594
#  circle 0.002 fill black
#  amove   1.61904766  1.53383459
#  circle 0.002 fill black
#  amove   1.61904766  1.54135338
#  circle 0.002 fill black
#  amove   1.62756897  1.4962406
#  circle 0.002 fill black
#  amove   1.62756897  1.5112782
#  circle 0.002 fill black
#  amove   1.62756897  1.54135338
#  circle 0.002 fill black
#  amove   1.63609027  1.47368421
#  circle 0.002 fill black
#  amove   1.63609027  1.48120301
#  circle 0.002 fill black
#  amove   1.63609027  1.4887218
#  circle 0.002 fill black
#  amove   1.63609027  1.54135338
#  circle 0.002 fill black
#  amove   1.63609027  1.56390977
#  circle 0.002 fill black
#  amove   1.64461157  1.39849624
#  circle 0.002 fill black
#  amove   1.64461157  1.42105263
#  circle 0.002 fill black
#  amove   1.64461157  1.42857143
#  circle 0.002 fill black
#  amove   1.64461157  1.45864662
#  circle 0.002 fill black
#  amove   1.64461157  1.46616541
#  circle 0.002 fill black
#  amove   1.64461157  1.4887218
#  circle 0.002 fill black
#  amove   1.64461157  1.5037594
#  circle 0.002 fill black
#  amove   1.64461157  1.54135338
#  circle 0.002 fill black
#  amove   1.64461157  1.55639098
#  circle 0.002 fill black
#  amove   1.64461157  1.57142857
#  circle 0.002 fill black
#  amove   1.65313288  1.54135338
#  circle 0.002 fill black
#  amove   1.65313288  1.54887218
#  circle 0.002 fill black
#  amove   1.66165418  1.43609023
#  circle 0.002 fill black
#  amove   1.66165418  1.47368421
#  circle 0.002 fill black
#  amove   1.66165418  1.5037594
#  circle 0.002 fill black
#  amove   1.66165418  1.51879699
#  circle 0.002 fill black
#  amove   1.66165418  1.60150376
#  circle 0.002 fill black
#  amove   1.67017549  1.40601504
#  circle 0.002 fill black
#  amove   1.67017549  1.42857143
#  circle 0.002 fill black
#  amove   1.67017549  1.5037594
#  circle 0.002 fill black
#  amove   1.67017549  1.54887218
#  circle 0.002 fill black
#  amove   1.67017549  1.56390977
#  circle 0.002 fill black
#  amove   1.67869679  1.45112782
#  circle 0.002 fill black
#  amove   1.67869679  1.48120301
#  circle 0.002 fill black
#  amove   1.67869679  1.52631579
#  circle 0.002 fill black
#  amove   1.67869679  1.53383459
#  circle 0.002 fill black
#  amove   1.68721809  1.46616541
#  circle 0.002 fill black
#  amove   1.68721809  1.48120301
#  circle 0.002 fill black
#  amove   1.68721809  1.4887218
#  circle 0.002 fill black
#  amove   1.68721809  1.52631579
#  circle 0.002 fill black
#  amove   1.68721809  1.57142857
#  circle 0.002 fill black
#  amove   1.6957394  1.56390977
#  circle 0.002 fill black
#  amove   1.6957394  1.57142857
#  circle 0.002 fill black
#  amove   1.7042607  1.48120301
#  circle 0.002 fill black
#  amove   1.7042607  1.4962406
#  circle 0.002 fill black
#  amove   1.7042607  1.54135338
#  circle 0.002 fill black
#  amove   1.7042607  1.57142857
#  circle 0.002 fill black
#  amove   1.7042607  1.57894737
#  circle 0.002 fill black
#  amove   1.712782  1.46616541
#  circle 0.002 fill black
#  amove   1.712782  1.4887218
#  circle 0.002 fill black
#  amove   1.712782  1.5037594
#  circle 0.002 fill black
#  amove   1.712782  1.5112782
#  circle 0.002 fill black
#  amove   1.712782  1.54135338
#  circle 0.002 fill black
#  amove   1.712782  1.57894737
#  circle 0.002 fill black
#  amove   1.72130331  1.43609023
#  circle 0.002 fill black
#  amove   1.72130331  1.4962406
#  circle 0.002 fill black
#  amove   1.72130331  1.5037594
#  circle 0.002 fill black
#  amove   1.72130331  1.5112782
#  circle 0.002 fill black
#  amove   1.72130331  1.57142857
#  circle 0.002 fill black
#  amove   1.72982461  1.36842105
#  circle 0.002 fill black
#  amove   1.72982461  1.41353383
#  circle 0.002 fill black
#  amove   1.72982461  1.45864662
#  circle 0.002 fill black
#  amove   1.72982461  1.48120301
#  circle 0.002 fill black
#  amove   1.72982461  1.5037594
#  circle 0.002 fill black
#  amove   1.72982461  1.51879699
#  circle 0.002 fill black
#  amove   1.72982461  1.52631579
#  circle 0.002 fill black
#  amove   1.72982461  1.54135338
#  circle 0.002 fill black
#  amove   1.72982461  1.56390977
#  circle 0.002 fill black
#  amove   1.72982461  1.59398496
#  circle 0.002 fill black
#  amove   1.73834591  1.42857143
#  circle 0.002 fill black
#  amove   1.73834591  1.48120301
#  circle 0.002 fill black
#  amove   1.73834591  1.4887218
#  circle 0.002 fill black
#  amove   1.73834591  1.55639098
#  circle 0.002 fill black
#  amove   1.73834591  1.62406015
#  circle 0.002 fill black
#  amove   1.74686722  1.48120301
#  circle 0.002 fill black
#  amove   1.74686722  1.4887218
#  circle 0.002 fill black
#  amove   1.74686722  1.52631579
#  circle 0.002 fill black
#  amove   1.74686722  1.54887218
#  circle 0.002 fill black
#  amove   1.74686722  1.63909774
#  circle 0.002 fill black
#  amove   1.75538852  1.42857143
#  circle 0.002 fill black
#  amove   1.75538852  1.47368421
#  circle 0.002 fill black
#  amove   1.75538852  1.48120301
#  circle 0.002 fill black
#  amove   1.75538852  1.55639098
#  circle 0.002 fill black
#  amove   1.75538852  1.56390977
#  circle 0.002 fill black
#  amove   1.76390982  1.37593985
#  circle 0.002 fill black
#  amove   1.76390982  1.4887218
#  circle 0.002 fill black
#  amove   1.76390982  1.59398496
#  circle 0.002 fill black
#  amove   1.77243113  1.36090226
#  circle 0.002 fill black
#  amove   1.77243113  1.38345865
#  circle 0.002 fill black
#  amove   1.77243113  1.42857143
#  circle 0.002 fill black
#  amove   1.77243113  1.45112782
#  circle 0.002 fill black
#  amove   1.77243113  1.48120301
#  circle 0.002 fill black
#  amove   1.77243113  1.5112782
#  circle 0.002 fill black
#  amove   1.77243113  1.51879699
#  circle 0.002 fill black
#  amove   1.77243113  1.56390977
#  circle 0.002 fill black
#  amove   1.78095243  1.42105263
#  circle 0.002 fill black
#  amove   1.78095243  1.45864662
#  circle 0.002 fill black
#  amove   1.78095243  1.4887218
#  circle 0.002 fill black
#  amove   1.78095243  1.4962406
#  circle 0.002 fill black
#  amove   1.78095243  1.51879699
#  circle 0.002 fill black
#  amove   1.78095243  1.53383459
#  circle 0.002 fill black
#  amove   1.78095243  1.55639098
#  circle 0.002 fill black
#  amove   1.78095243  1.56390977
#  circle 0.002 fill black
#  amove   1.78947373  1.42857143
#  circle 0.002 fill black
#  amove   1.78947373  1.45864662
#  circle 0.002 fill black
#  amove   1.78947373  1.46616541
#  circle 0.002 fill black
#  amove   1.78947373  1.48120301
#  circle 0.002 fill black
#  amove   1.78947373  1.5037594
#  circle 0.002 fill black
#  amove   1.78947373  1.52631579
#  circle 0.002 fill black
#  amove   1.78947373  1.56390977
#  circle 0.002 fill black
#  amove   1.79799504  1.42105263
#  circle 0.002 fill black
#  amove   1.79799504  1.46616541
#  circle 0.002 fill black
#  amove   1.79799504  1.48120301
#  circle 0.002 fill black
#  amove   1.79799504  1.5112782
#  circle 0.002 fill black
#  amove   1.79799504  1.54887218
#  circle 0.002 fill black
#  amove   1.79799504  1.55639098
#  circle 0.002 fill black
#  amove   1.79799504  1.59398496
#  circle 0.002 fill black
#  amove   1.80651634  1.44360902
#  circle 0.002 fill black
#  amove   1.80651634  1.47368421
#  circle 0.002 fill black
#  amove   1.80651634  1.5112782
#  circle 0.002 fill black
#  amove   1.80651634  1.52631579
#  circle 0.002 fill black
#  amove   1.80651634  1.54887218
#  circle 0.002 fill black
#  amove   1.80651634  1.55639098
#  circle 0.002 fill black
#  amove   1.80651634  1.56390977
#  circle 0.002 fill black
#  amove   1.81503764  1.4887218
#  circle 0.002 fill black
#  amove   1.81503764  1.5112782
#  circle 0.002 fill black
#  amove   1.81503764  1.52631579
#  circle 0.002 fill black
#  amove   1.81503764  1.56390977
#  circle 0.002 fill black
#  amove   1.81503764  1.61654135
#  circle 0.002 fill black
#  amove   1.81503764  1.64661654
#  circle 0.002 fill black
#  amove   1.82355895  1.40601504
#  circle 0.002 fill black
#  amove   1.82355895  1.56390977
#  circle 0.002 fill black
#  amove   1.82355895  1.58646617
#  circle 0.002 fill black
#  amove   1.83208025  1.42857143
#  circle 0.002 fill black
#  amove   1.83208025  1.43609023
#  circle 0.002 fill black
#  amove   1.83208025  1.44360902
#  circle 0.002 fill black
#  amove   1.83208025  1.46616541
#  circle 0.002 fill black
#  amove   1.83208025  1.4887218
#  circle 0.002 fill black
#  amove   1.83208025  1.54887218
#  circle 0.002 fill black
#  amove   1.83208025  1.63157895
#  circle 0.002 fill black
#  amove   1.84060156  1.46616541
#  circle 0.002 fill black
#  amove   1.84060156  1.4887218
#  circle 0.002 fill black
#  amove   1.84060156  1.53383459
#  circle 0.002 fill black
#  amove   1.84060156  1.55639098
#  circle 0.002 fill black
#  amove   1.84060156  1.57142857
#  circle 0.002 fill black
#  amove   1.84060156  1.60150376
#  circle 0.002 fill black
#  amove   1.84912286  1.37593985
#  circle 0.002 fill black
#  amove   1.84912286  1.46616541
#  circle 0.002 fill black
#  amove   1.84912286  1.47368421
#  circle 0.002 fill black
#  amove   1.84912286  1.4887218
#  circle 0.002 fill black
#  amove   1.84912286  1.5037594
#  circle 0.002 fill black
#  amove   1.84912286  1.52631579
#  circle 0.002 fill black
#  amove   1.84912286  1.56390977
#  circle 0.002 fill black
#  amove   1.84912286  1.57142857
#  circle 0.002 fill black
#  amove   1.85764416  1.41353383
#  circle 0.002 fill black
#  amove   1.85764416  1.44360902
#  circle 0.002 fill black
#  amove   1.85764416  1.4962406
#  circle 0.002 fill black
#  amove   1.85764416  1.5037594
#  circle 0.002 fill black
#  amove   1.85764416  1.5112782
#  circle 0.002 fill black
#  amove   1.85764416  1.51879699
#  circle 0.002 fill black
#  amove   1.85764416  1.53383459
#  circle 0.002 fill black
#  amove   1.85764416  1.55639098
#  circle 0.002 fill black
#  amove   1.85764416  1.57142857
#  circle 0.002 fill black
#  amove   1.86616547  1.44360902
#  circle 0.002 fill black
#  amove   1.86616547  1.4887218
#  circle 0.002 fill black
#  amove   1.86616547  1.4962406
#  circle 0.002 fill black
#  amove   1.86616547  1.57142857
#  circle 0.002 fill black
#  amove   1.87468677  1.36090226
#  circle 0.002 fill black
#  amove   1.87468677  1.43609023
#  circle 0.002 fill black
#  amove   1.87468677  1.44360902
#  circle 0.002 fill black
#  amove   1.87468677  1.56390977
#  circle 0.002 fill black
#  amove   1.87468677  1.57894737
#  circle 0.002 fill black
#  amove   1.87468677  1.60150376
#  circle 0.002 fill black
#  amove   1.88320807  1.41353383
#  circle 0.002 fill black
#  amove   1.88320807  1.4887218
#  circle 0.002 fill black
#  amove   1.88320807  1.5112782
#  circle 0.002 fill black
#  amove   1.88320807  1.51879699
#  circle 0.002 fill black
#  amove   1.88320807  1.54135338
#  circle 0.002 fill black
#  amove   1.88320807  1.56390977
#  circle 0.002 fill black
#  amove   1.89172938  1.43609023
#  circle 0.002 fill black
#  amove   1.89172938  1.44360902
#  circle 0.002 fill black
#  amove   1.89172938  1.57142857
#  circle 0.002 fill black
#  amove   1.89172938  1.59398496
#  circle 0.002 fill black
#  amove   1.90025068  1.40601504
#  circle 0.002 fill black
#  amove   1.90025068  1.45112782
#  circle 0.002 fill black
#  amove   1.90025068  1.4887218
#  circle 0.002 fill black
#  amove   1.90025068  1.5112782
#  circle 0.002 fill black
#  amove   1.90025068  1.53383459
#  circle 0.002 fill black
#  amove   1.90877198  1.39097744
#  circle 0.002 fill black
#  amove   1.90877198  1.52631579
#  circle 0.002 fill black
#  amove   1.90877198  1.57142857
#  circle 0.002 fill black
#  amove   1.91729329  1.41353383
#  circle 0.002 fill black
#  amove   1.91729329  1.44360902
#  circle 0.002 fill black
#  amove   1.91729329  1.47368421
#  circle 0.002 fill black
#  amove   1.91729329  1.52631579
#  circle 0.002 fill black
#  amove   1.91729329  1.55639098
#  circle 0.002 fill black
#  amove   1.91729329  1.58646617
#  circle 0.002 fill black
#  amove   1.92581459  1.44360902
#  circle 0.002 fill black
#  amove   1.92581459  1.5037594
#  circle 0.002 fill black
#  amove   1.92581459  1.51879699
#  circle 0.002 fill black
#  amove   1.93433589  1.51879699
#  circle 0.002 fill black
#  amove   1.93433589  1.52631579
#  circle 0.002 fill black
#  amove   1.93433589  1.54135338
#  circle 0.002 fill black
#  amove   1.93433589  1.57142857
#  circle 0.002 fill black
#  amove   1.9428572  1.42857143
#  circle 0.002 fill black
#  amove   1.9428572  1.44360902
#  circle 0.002 fill black
#  amove   1.9428572  1.45112782
#  circle 0.002 fill black
#  amove   1.9428572  1.4887218
#  circle 0.002 fill black
#  amove   1.9428572  1.51879699
#  circle 0.002 fill black
#  amove   1.9428572  1.52631579
#  circle 0.002 fill black
#  amove   1.9428572  1.57894737
#  circle 0.002 fill black
#  amove   1.9513785  1.31578947
#  circle 0.002 fill black
#  amove   1.9513785  1.40601504
#  circle 0.002 fill black
#  amove   1.9513785  1.47368421
#  circle 0.002 fill black
#  amove   1.9513785  1.54135338
#  circle 0.002 fill black
#  amove   1.9513785  1.55639098
#  circle 0.002 fill black
#  amove   1.9513785  1.57142857
#  circle 0.002 fill black
#  amove   1.9598998  1.42857143
#  circle 0.002 fill black
#  amove   1.9598998  1.45112782
#  circle 0.002 fill black
#  amove   1.9598998  1.4962406
#  circle 0.002 fill black
#  amove   1.96842111  1.42105263
#  circle 0.002 fill black
#  amove   1.96842111  1.45112782
#  circle 0.002 fill black
#  amove   1.96842111  1.46616541
#  circle 0.002 fill black
#  amove   1.96842111  1.5112782
#  circle 0.002 fill black
#  amove   1.96842111  1.57142857
#  circle 0.002 fill black
#  amove   1.97694241  1.43609023
#  circle 0.002 fill black
#  amove   1.97694241  1.46616541
#  circle 0.002 fill black
#  amove   1.97694241  1.48120301
#  circle 0.002 fill black
#  amove   1.97694241  1.5037594
#  circle 0.002 fill black
#  amove   1.97694241  1.58646617
#  circle 0.002 fill black
#  amove   1.98546371  1.45112782
#  circle 0.002 fill black
#  amove   1.98546371  1.46616541
#  circle 0.002 fill black
#  amove   1.98546371  1.47368421
#  circle 0.002 fill black
#  amove   1.98546371  1.48120301
#  circle 0.002 fill black
#  amove   1.98546371  1.4887218
#  circle 0.002 fill black
#  amove   1.98546371  1.51879699
#  circle 0.002 fill black
#  amove   1.99398502  1.41353383
#  circle 0.002 fill black
#  amove   1.99398502  1.47368421
#  circle 0.002 fill black
#  amove   1.99398502  1.48120301
#  circle 0.002 fill black
#  amove   1.99398502  1.5112782
#  circle 0.002 fill black
#  amove   1.99398502  1.53383459
#  circle 0.002 fill black
#  amove   1.99398502  1.54887218
#  circle 0.002 fill black
#  amove   2.00250632  1.4887218
#  circle 0.002 fill black
#  amove   2.00250632  1.4962406
#  circle 0.002 fill black
#  amove   2.00250632  1.51879699
#  circle 0.002 fill black
#  amove   2.00250632  1.54887218
#  circle 0.002 fill black
#  amove   2.01102763  1.45864662
#  circle 0.002 fill black
#  amove   2.01102763  1.48120301
#  circle 0.002 fill black
#  amove   2.01102763  1.5037594
#  circle 0.002 fill black
#  amove   2.01102763  1.5112782
#  circle 0.002 fill black
#  amove   2.01102763  1.54887218
#  circle 0.002 fill black
#  amove   2.01102763  1.57142857
#  circle 0.002 fill black
#  amove   2.01102763  1.63909774
#  circle 0.002 fill black
#  amove   2.01954893  1.55639098
#  circle 0.002 fill black
#  amove   2.01954893  1.56390977
#  circle 0.002 fill black
#  amove   2.01954893  1.57142857
#  circle 0.002 fill black
#  amove   2.01954893  1.57894737
#  circle 0.002 fill black
#  amove   2.01954893  1.63157895
#  circle 0.002 fill black
#  amove   2.02807023  1.37593985
#  circle 0.002 fill black
#  amove   2.02807023  1.39097744
#  circle 0.002 fill black
#  amove   2.02807023  1.42857143
#  circle 0.002 fill black
#  amove   2.02807023  1.43609023
#  circle 0.002 fill black
#  amove   2.02807023  1.47368421
#  circle 0.002 fill black
#  amove   2.02807023  1.48120301
#  circle 0.002 fill black
#  amove   2.02807023  1.54135338
#  circle 0.002 fill black
#  amove   2.02807023  1.54887218
#  circle 0.002 fill black
#  amove   2.02807023  1.57894737
#  circle 0.002 fill black
#  amove   2.02807023  1.64661654
#  circle 0.002 fill black
#  amove   2.03659154  1.37593985
#  circle 0.002 fill black
#  amove   2.03659154  1.43609023
#  circle 0.002 fill black
#  amove   2.03659154  1.48120301
#  circle 0.002 fill black
#  amove   2.03659154  1.4962406
#  circle 0.002 fill black
#  amove   2.03659154  1.60902256
#  circle 0.002 fill black
#  amove   2.04511284  1.36842105
#  circle 0.002 fill black
#  amove   2.04511284  1.41353383
#  circle 0.002 fill black
#  amove   2.04511284  1.45112782
#  circle 0.002 fill black
#  amove   2.04511284  1.47368421
#  circle 0.002 fill black
#  amove   2.04511284  1.48120301
#  circle 0.002 fill black
#  amove   2.04511284  1.5037594
#  circle 0.002 fill black
#  amove   2.04511284  1.5112782
#  circle 0.002 fill black
#  amove   2.05363414  1.47368421
#  circle 0.002 fill black
#  amove   2.05363414  1.4887218
#  circle 0.002 fill black
#  amove   2.05363414  1.5037594
#  circle 0.002 fill black
#  amove   2.05363414  1.51879699
#  circle 0.002 fill black
#  amove   2.06215545  1.44360902
#  circle 0.002 fill black
#  amove   2.06215545  1.45112782
#  circle 0.002 fill black
#  amove   2.06215545  1.4962406
#  circle 0.002 fill black
#  amove   2.06215545  1.53383459
#  circle 0.002 fill black
#  amove   2.06215545  1.54135338
#  circle 0.002 fill black
#  amove   2.06215545  1.54887218
#  circle 0.002 fill black
#  amove   2.06215545  1.57142857
#  circle 0.002 fill black
#  amove   2.06215545  1.57894737
#  circle 0.002 fill black
#  amove   2.06215545  1.61654135
#  circle 0.002 fill black
#  amove   2.06215545  1.64661654
#  circle 0.002 fill black
#  amove   2.07067675  1.43609023
#  circle 0.002 fill black
#  amove   2.07067675  1.44360902
#  circle 0.002 fill black
#  amove   2.07067675  1.5112782
#  circle 0.002 fill black
#  amove   2.07067675  1.51879699
#  circle 0.002 fill black
#  amove   2.07067675  1.57894737
#  circle 0.002 fill black
#  amove   2.07919805  1.43609023
#  circle 0.002 fill black
#  amove   2.07919805  1.5037594
#  circle 0.002 fill black
#  amove   2.07919805  1.52631579
#  circle 0.002 fill black
#  amove   2.07919805  1.54135338
#  circle 0.002 fill black
#  amove   2.07919805  1.54887218
#  circle 0.002 fill black
#  amove   2.07919805  1.56390977
#  circle 0.002 fill black
#  amove   2.08771936  1.45864662
#  circle 0.002 fill black
#  amove   2.08771936  1.46616541
#  circle 0.002 fill black
#  amove   2.08771936  1.52631579
#  circle 0.002 fill black
#  amove   2.08771936  1.54887218
#  circle 0.002 fill black
#  amove   2.08771936  1.59398496
#  circle 0.002 fill black
#  amove   2.08771936  1.60150376
#  circle 0.002 fill black
#  amove   2.09624066  1.39849624
#  circle 0.002 fill black
#  amove   2.09624066  1.48120301
#  circle 0.002 fill black
#  amove   2.09624066  1.4962406
#  circle 0.002 fill black
#  amove   2.09624066  1.54135338
#  circle 0.002 fill black
#  amove   2.10476196  1.41353383
#  circle 0.002 fill black
#  amove   2.10476196  1.48120301
#  circle 0.002 fill black
#  amove   2.10476196  1.5037594
#  circle 0.002 fill black
#  amove   2.10476196  1.5112782
#  circle 0.002 fill black
#  amove   2.10476196  1.52631579
#  circle 0.002 fill black
#  amove   2.11328327  1.42857143
#  circle 0.002 fill black
#  amove   2.11328327  1.45112782
#  circle 0.002 fill black
#  amove   2.11328327  1.4887218
#  circle 0.002 fill black
#  amove   2.11328327  1.4962406
#  circle 0.002 fill black
#  amove   2.11328327  1.5037594
#  circle 0.002 fill black
#  amove   2.11328327  1.54135338
#  circle 0.002 fill black
#  amove   2.12180457  1.43609023
#  circle 0.002 fill black
#  amove   2.12180457  1.48120301
#  circle 0.002 fill black
#  amove   2.12180457  1.4962406
#  circle 0.002 fill black
#  amove   2.13032587  1.38345865
#  circle 0.002 fill black
#  amove   2.13032587  1.4962406
#  circle 0.002 fill black
#  amove   2.13032587  1.5112782
#  circle 0.002 fill black
#  amove   2.13032587  1.51879699
#  circle 0.002 fill black
#  amove   2.13032587  1.57142857
#  circle 0.002 fill black
#  amove   2.13884718  1.39849624
#  circle 0.002 fill black
#  amove   2.13884718  1.45864662
#  circle 0.002 fill black
#  amove   2.13884718  1.47368421
#  circle 0.002 fill black
#  amove   2.13884718  1.48120301
#  circle 0.002 fill black
#  amove   2.13884718  1.53383459
#  circle 0.002 fill black
#  amove   2.13884718  1.60150376
#  circle 0.002 fill black
#  amove   2.14736848  1.45864662
#  circle 0.002 fill black
#  amove   2.14736848  1.47368421
#  circle 0.002 fill black
#  amove   2.14736848  1.4962406
#  circle 0.002 fill black
#  amove   2.14736848  1.5037594
#  circle 0.002 fill black
#  amove   2.14736848  1.53383459
#  circle 0.002 fill black
#  amove   2.14736848  1.57894737
#  circle 0.002 fill black
#  amove   2.15588978  1.41353383
#  circle 0.002 fill black
#  amove   2.15588978  1.4962406
#  circle 0.002 fill black
#  amove   2.15588978  1.57894737
#  circle 0.002 fill black
#  amove   2.16441109  1.44360902
#  circle 0.002 fill black
#  amove   2.16441109  1.45864662
#  circle 0.002 fill black
#  amove   2.16441109  1.57142857
#  circle 0.002 fill black
#  amove   2.16441109  1.63909774
#  circle 0.002 fill black
#  amove   2.17293239  1.41353383
#  circle 0.002 fill black
#  amove   2.17293239  1.42105263
#  circle 0.002 fill black
#  amove   2.17293239  1.45112782
#  circle 0.002 fill black
#  amove   2.17293239  1.46616541
#  circle 0.002 fill black
#  amove   2.17293239  1.4887218
#  circle 0.002 fill black
#  amove   2.17293239  1.52631579
#  circle 0.002 fill black
#  amove   2.17293239  1.57142857
#  circle 0.002 fill black
#  amove   2.1814537  1.38345865
#  circle 0.002 fill black
#  amove   2.1814537  1.42857143
#  circle 0.002 fill black
#  amove   2.1814537  1.4962406
#  circle 0.002 fill black
#  amove   2.1814537  1.5037594
#  circle 0.002 fill black
#  amove   2.1814537  1.5112782
#  circle 0.002 fill black
#  amove   2.1814537  1.51879699
#  circle 0.002 fill black
#  amove   2.189975  1.45112782
#  circle 0.002 fill black
#  amove   2.189975  1.4887218
#  circle 0.002 fill black
#  amove   2.1984963  1.39097744
#  circle 0.002 fill black
#  amove   2.1984963  1.39849624
#  circle 0.002 fill black
#  amove   2.1984963  1.42857143
#  circle 0.002 fill black
#  amove   2.1984963  1.45112782
#  circle 0.002 fill black
#  amove   2.1984963  1.48120301
#  circle 0.002 fill black
#  amove   2.1984963  1.4962406
#  circle 0.002 fill black
#  amove   2.1984963  1.5112782
#  circle 0.002 fill black
#  amove   2.1984963  1.53383459
#  circle 0.002 fill black
#  amove   2.1984963  1.55639098
#  circle 0.002 fill black
#  amove   2.1984963  1.61654135
#  circle 0.002 fill black
#  amove   2.20701761  1.42105263
#  circle 0.002 fill black
#  amove   2.20701761  1.42857143
#  circle 0.002 fill black
#  amove   2.20701761  1.46616541
#  circle 0.002 fill black
#  amove   2.20701761  1.48120301
#  circle 0.002 fill black
#  amove   2.20701761  1.4962406
#  circle 0.002 fill black
#  amove   2.20701761  1.57142857
#  circle 0.002 fill black
#  amove   2.20701761  1.67669173
#  circle 0.002 fill black
#  amove   2.21553891  1.41353383
#  circle 0.002 fill black
#  amove   2.21553891  1.44360902
#  circle 0.002 fill black
#  amove   2.21553891  1.47368421
#  circle 0.002 fill black
#  amove   2.21553891  1.54135338
#  circle 0.002 fill black
#  amove   2.21553891  1.60150376
#  circle 0.002 fill black
#  amove   2.22406021  1.36090226
#  circle 0.002 fill black
#  amove   2.22406021  1.39849624
#  circle 0.002 fill black
#  amove   2.22406021  1.42857143
#  circle 0.002 fill black
#  amove   2.22406021  1.45864662
#  circle 0.002 fill black
#  amove   2.22406021  1.46616541
#  circle 0.002 fill black
#  amove   2.22406021  1.47368421
#  circle 0.002 fill black
#  amove   2.22406021  1.48120301
#  circle 0.002 fill black
#  amove   2.22406021  1.4887218
#  circle 0.002 fill black
#  amove   2.22406021  1.4962406
#  circle 0.002 fill black
#  amove   2.22406021  1.52631579
#  circle 0.002 fill black
#  amove   2.22406021  1.53383459
#  circle 0.002 fill black
#  amove   2.23258152  1.42857143
#  circle 0.002 fill black
#  amove   2.23258152  1.45864662
#  circle 0.002 fill black
#  amove   2.23258152  1.48120301
#  circle 0.002 fill black
#  amove   2.23258152  1.4962406
#  circle 0.002 fill black
#  amove   2.24110282  1.42857143
#  circle 0.002 fill black
#  amove   2.24110282  1.45112782
#  circle 0.002 fill black
#  amove   2.24110282  1.45864662
#  circle 0.002 fill black
#  amove   2.24110282  1.47368421
#  circle 0.002 fill black
#  amove   2.24110282  1.48120301
#  circle 0.002 fill black
#  amove   2.24110282  1.54135338
#  circle 0.002 fill black
#  amove   2.24110282  1.56390977
#  circle 0.002 fill black
#  amove   2.24962412  1.46616541
#  circle 0.002 fill black
#  amove   2.24962412  1.47368421
#  circle 0.002 fill black
#  amove   2.24962412  1.4887218
#  circle 0.002 fill black
#  amove   2.24962412  1.53383459
#  circle 0.002 fill black
#  amove   2.24962412  1.54135338
#  circle 0.002 fill black
#  amove   2.24962412  1.59398496
#  circle 0.002 fill black
#  amove   2.25814543  1.31578947
#  circle 0.002 fill black
#  amove   2.25814543  1.42105263
#  circle 0.002 fill black
#  amove   2.25814543  1.44360902
#  circle 0.002 fill black
#  amove   2.25814543  1.45112782
#  circle 0.002 fill black
#  amove   2.25814543  1.48120301
#  circle 0.002 fill black
#  amove   2.25814543  1.52631579
#  circle 0.002 fill black
#  amove   2.25814543  1.54887218
#  circle 0.002 fill black
#  amove   2.26666673  1.47368421
#  circle 0.002 fill black
#  amove   2.27518803  1.42857143
#  circle 0.002 fill black
#  amove   2.27518803  1.43609023
#  circle 0.002 fill black
#  amove   2.27518803  1.47368421
#  circle 0.002 fill black
#  amove   2.27518803  1.5037594
#  circle 0.002 fill black
#  amove   2.27518803  1.5112782
#  circle 0.002 fill black
#  amove   2.27518803  1.54135338
#  circle 0.002 fill black
#  amove   2.27518803  1.54887218
#  circle 0.002 fill black
#  amove   2.27518803  1.58646617
#  circle 0.002 fill black
#  amove   2.28370934  1.42857143
#  circle 0.002 fill black
#  amove   2.29223064  1.38345865
#  circle 0.002 fill black
#  amove   2.29223064  1.40601504
#  circle 0.002 fill black
#  amove   2.29223064  1.4962406
#  circle 0.002 fill black
#  amove   2.29223064  1.51879699
#  circle 0.002 fill black
#  amove   2.29223064  1.54135338
#  circle 0.002 fill black
#  amove   2.29223064  1.59398496
#  circle 0.002 fill black
#  amove   2.29223064  1.60150376
#  circle 0.002 fill black
#  amove   2.30075194  1.39849624
#  circle 0.002 fill black
#  amove   2.30075194  1.42857143
#  circle 0.002 fill black
#  amove   2.30075194  1.44360902
#  circle 0.002 fill black
#  amove   2.30075194  1.4962406
#  circle 0.002 fill black
#  amove   2.30075194  1.5037594
#  circle 0.002 fill black
#  amove   2.30075194  1.5112782
#  circle 0.002 fill black
#  amove   2.30075194  1.53383459
#  circle 0.002 fill black
#  amove   2.30927325  1.51879699
#  circle 0.002 fill black
#  amove   2.30927325  1.53383459
#  circle 0.002 fill black
#  amove   2.30927325  1.63157895
#  circle 0.002 fill black
#  amove   2.31779455  1.38345865
#  circle 0.002 fill black
#  amove   2.31779455  1.48120301
#  circle 0.002 fill black
#  amove   2.31779455  1.4962406
#  circle 0.002 fill black
#  amove   2.31779455  1.5112782
#  circle 0.002 fill black
#  amove   2.31779455  1.56390977
#  circle 0.002 fill black
#  amove   2.31779455  1.57894737
#  circle 0.002 fill black
#  amove   2.32631585  1.44360902
#  circle 0.002 fill black
#  amove   2.32631585  1.47368421
#  circle 0.002 fill black
#  amove   2.32631585  1.5037594
#  circle 0.002 fill black
#  amove   2.33483716  1.33082707
#  circle 0.002 fill black
#  amove   2.33483716  1.39097744
#  circle 0.002 fill black
#  amove   2.33483716  1.42857143
#  circle 0.002 fill black
#  amove   2.33483716  1.43609023
#  circle 0.002 fill black
#  amove   2.33483716  1.5037594
#  circle 0.002 fill black
#  amove   2.33483716  1.5112782
#  circle 0.002 fill black
#  amove   2.33483716  1.51879699
#  circle 0.002 fill black
#  amove   2.33483716  1.54135338
#  circle 0.002 fill black
#  amove   2.33483716  1.54887218
#  circle 0.002 fill black
#  amove   2.33483716  1.56390977
#  circle 0.002 fill black
#  amove   2.33483716  1.62406015
#  circle 0.002 fill black
#  amove   2.34335846  1.42857143
#  circle 0.002 fill black
#  amove   2.34335846  1.48120301
#  circle 0.002 fill black
#  amove   2.34335846  1.5037594
#  circle 0.002 fill black
#  amove   2.35187977  1.45864662
#  circle 0.002 fill black
#  amove   2.35187977  1.4962406
#  circle 0.002 fill black
#  amove   2.35187977  1.58646617
#  circle 0.002 fill black
#  amove   2.35187977  1.60150376
#  circle 0.002 fill black
#  amove   2.36040107  1.39849624
#  circle 0.002 fill black
#  amove   2.36040107  1.40601504
#  circle 0.002 fill black
#  amove   2.36040107  1.43609023
#  circle 0.002 fill black
#  amove   2.36040107  1.46616541
#  circle 0.002 fill black
#  amove   2.36040107  1.47368421
#  circle 0.002 fill black
#  amove   2.36040107  1.48120301
#  circle 0.002 fill black
#  amove   2.36040107  1.4887218
#  circle 0.002 fill black
#  amove   2.36040107  1.5037594
#  circle 0.002 fill black
#  amove   2.36040107  1.5112782
#  circle 0.002 fill black
#  amove   2.36040107  1.53383459
#  circle 0.002 fill black
#  amove   2.36040107  1.54887218
#  circle 0.002 fill black
#  amove   2.36040107  1.56390977
#  circle 0.002 fill black
#  amove   2.36040107  1.62406015
#  circle 0.002 fill black
#  amove   2.36892237  1.46616541
#  circle 0.002 fill black
#  amove   2.36892237  1.60150376
#  circle 0.002 fill black
#  amove   2.37744368  1.41353383
#  circle 0.002 fill black
#  amove   2.37744368  1.43609023
#  circle 0.002 fill black
#  amove   2.37744368  1.4887218
#  circle 0.002 fill black
#  amove   2.37744368  1.57142857
#  circle 0.002 fill black
#  amove   2.37744368  1.60150376
#  circle 0.002 fill black
#  amove   2.38596498  1.42105263
#  circle 0.002 fill black
#  amove   2.38596498  1.45112782
#  circle 0.002 fill black
#  amove   2.38596498  1.47368421
#  circle 0.002 fill black
#  amove   2.38596498  1.5037594
#  circle 0.002 fill black
#  amove   2.38596498  1.5112782
#  circle 0.002 fill black
#  amove   2.38596498  1.57894737
#  circle 0.002 fill black
#  amove   2.39448628  1.4887218
#  circle 0.002 fill black
#  amove   2.39448628  1.5112782
#  circle 0.002 fill black
#  amove   2.39448628  1.54887218
#  circle 0.002 fill black
#  amove   2.39448628  1.56390977
#  circle 0.002 fill black
#  amove   2.39448628  1.60150376
#  circle 0.002 fill black
#  amove   2.39448628  1.60902256
#  circle 0.002 fill black
#  amove   2.40300759  1.51879699
#  circle 0.002 fill black
#  amove   2.40300759  1.52631579
#  circle 0.002 fill black
#  amove   2.41152889  1.45864662
#  circle 0.002 fill black
#  amove   2.41152889  1.47368421
#  circle 0.002 fill black
#  amove   2.41152889  1.5112782
#  circle 0.002 fill black
#  amove   2.41152889  1.51879699
#  circle 0.002 fill black
#  amove   2.41152889  1.54887218
#  circle 0.002 fill black
#  amove   2.42005019  1.29323308
#  circle 0.002 fill black
#  amove   2.42005019  1.38345865
#  circle 0.002 fill black
#  amove   2.42005019  1.41353383
#  circle 0.002 fill black
#  amove   2.42005019  1.44360902
#  circle 0.002 fill black
#  amove   2.42005019  1.47368421
#  circle 0.002 fill black
#  amove   2.42005019  1.5112782
#  circle 0.002 fill black
#  amove   2.42005019  1.54135338
#  circle 0.002 fill black
#  amove   2.42005019  1.54887218
#  circle 0.002 fill black
#  amove   2.42005019  1.57894737
#  circle 0.002 fill black
#  amove   2.4285715  1.38345865
#  circle 0.002 fill black
#  amove   2.4285715  1.45112782
#  circle 0.002 fill black
#  amove   2.4285715  1.47368421
#  circle 0.002 fill black
#  amove   2.4285715  1.48120301
#  circle 0.002 fill black
#  amove   2.4285715  1.4887218
#  circle 0.002 fill black
#  amove   2.4285715  1.4962406
#  circle 0.002 fill black
#  amove   2.4285715  1.5112782
#  circle 0.002 fill black
#  amove   2.4285715  1.53383459
#  circle 0.002 fill black
#  amove   2.4285715  1.57142857
#  circle 0.002 fill black
#  amove   2.4370928  1.45864662
#  circle 0.002 fill black
#  amove   2.4370928  1.48120301
#  circle 0.002 fill black
#  amove   2.4370928  1.4962406
#  circle 0.002 fill black
#  amove   2.4370928  1.5112782
#  circle 0.002 fill black
#  amove   2.4370928  1.51879699
#  circle 0.002 fill black
#  amove   2.4456141  1.40601504
#  circle 0.002 fill black
#  amove   2.4456141  1.42105263
#  circle 0.002 fill black
#  amove   2.4456141  1.46616541
#  circle 0.002 fill black
#  amove   2.4456141  1.47368421
#  circle 0.002 fill black
#  amove   2.4456141  1.48120301
#  circle 0.002 fill black
#  amove   2.4456141  1.5112782
#  circle 0.002 fill black
#  amove   2.4456141  1.55639098
#  circle 0.002 fill black
#  amove   2.45413541  1.41353383
#  circle 0.002 fill black
#  amove   2.45413541  1.54135338
#  circle 0.002 fill black
#  amove   2.45413541  1.54887218
#  circle 0.002 fill black
#  amove   2.45413541  1.55639098
#  circle 0.002 fill black
#  amove   2.46265671  1.47368421
#  circle 0.002 fill black
#  amove   2.46265671  1.52631579
#  circle 0.002 fill black
#  amove   2.46265671  1.56390977
#  circle 0.002 fill black
#  amove   2.46265671  1.63909774
#  circle 0.002 fill black
#  amove   2.47117801  1.40601504
#  circle 0.002 fill black
#  amove   2.47117801  1.41353383
#  circle 0.002 fill black
#  amove   2.47117801  1.44360902
#  circle 0.002 fill black
#  amove   2.47117801  1.45112782
#  circle 0.002 fill black
#  amove   2.47117801  1.45864662
#  circle 0.002 fill black
#  amove   2.47117801  1.47368421
#  circle 0.002 fill black
#  amove   2.47117801  1.4887218
#  circle 0.002 fill black
#  amove   2.47117801  1.4962406
#  circle 0.002 fill black
#  amove   2.47117801  1.5037594
#  circle 0.002 fill black
#  amove   2.47969932  1.40601504
#  circle 0.002 fill black
#  amove   2.47969932  1.42857143
#  circle 0.002 fill black
#  amove   2.47969932  1.43609023
#  circle 0.002 fill black
#  amove   2.47969932  1.46616541
#  circle 0.002 fill black
#  amove   2.47969932  1.5037594
#  circle 0.002 fill black
#  amove   2.47969932  1.5112782
#  circle 0.002 fill black
#  amove   2.47969932  1.51879699
#  circle 0.002 fill black
#  amove   2.47969932  1.58646617
#  circle 0.002 fill black
#  amove   2.48822062  1.41353383
#  circle 0.002 fill black
#  amove   2.48822062  1.43609023
#  circle 0.002 fill black
#  amove   2.48822062  1.45112782
#  circle 0.002 fill black
#  amove   2.48822062  1.48120301
#  circle 0.002 fill black
#  amove   2.48822062  1.4887218
#  circle 0.002 fill black
#  amove   2.48822062  1.5037594
#  circle 0.002 fill black
#  amove   2.48822062  1.52631579
#  circle 0.002 fill black
#  amove   2.48822062  1.54135338
#  circle 0.002 fill black
#  amove   2.48822062  1.57894737
#  circle 0.002 fill black
#  amove   2.48822062  1.60902256
#  circle 0.002 fill black
#  amove   2.49674192  1.5112782
#  circle 0.002 fill black
#  amove   2.49674192  1.52631579
#  circle 0.002 fill black
#  amove   2.49674192  1.57894737
#  circle 0.002 fill black
#  amove   2.49674192  1.62406015
#  circle 0.002 fill black
#  amove   2.50526323  1.42857143
#  circle 0.002 fill black
#  amove   2.50526323  1.45112782
#  circle 0.002 fill black
#  amove   2.50526323  1.45864662
#  circle 0.002 fill black
#  amove   2.50526323  1.4887218
#  circle 0.002 fill black
#  amove   2.50526323  1.4962406
#  circle 0.002 fill black
#  amove   2.50526323  1.52631579
#  circle 0.002 fill black
#  amove   2.50526323  1.54135338
#  circle 0.002 fill black
#  amove   2.51378453  1.43609023
#  circle 0.002 fill black
#  amove   2.51378453  1.44360902
#  circle 0.002 fill black
#  amove   2.51378453  1.51879699
#  circle 0.002 fill black
#  amove   2.51378453  1.55639098
#  circle 0.002 fill black
#  amove   2.52230584  1.35338346
#  circle 0.002 fill black
#  amove   2.52230584  1.36842105
#  circle 0.002 fill black
#  amove   2.52230584  1.38345865
#  circle 0.002 fill black
#  amove   2.52230584  1.44360902
#  circle 0.002 fill black
#  amove   2.52230584  1.45112782
#  circle 0.002 fill black
#  amove   2.53082714  1.45112782
#  circle 0.002 fill black
#  amove   2.53082714  1.48120301
#  circle 0.002 fill black
#  amove   2.53082714  1.4962406
#  circle 0.002 fill black
#  amove   2.53082714  1.51879699
#  circle 0.002 fill black
#  amove   2.53082714  1.58646617
#  circle 0.002 fill black
#  amove   2.53934844  1.5112782
#  circle 0.002 fill black
#  amove   2.53934844  1.51879699
#  circle 0.002 fill black
#  amove   2.53934844  1.53383459
#  circle 0.002 fill black
#  amove   2.53934844  1.54135338
#  circle 0.002 fill black
#  amove   2.53934844  1.56390977
#  circle 0.002 fill black
#  amove   2.54786975  1.45112782
#  circle 0.002 fill black
#  amove   2.54786975  1.48120301
#  circle 0.002 fill black
#  amove   2.54786975  1.5037594
#  circle 0.002 fill black
#  amove   2.54786975  1.5112782
#  circle 0.002 fill black
#  amove   2.54786975  1.51879699
#  circle 0.002 fill black
#  amove   2.54786975  1.54135338
#  circle 0.002 fill black
#  amove   2.54786975  1.55639098
#  circle 0.002 fill black
#  amove   2.54786975  1.60150376
#  circle 0.002 fill black
#  amove   2.55639105  1.28571429
#  circle 0.002 fill black
#  amove   2.55639105  1.42857143
#  circle 0.002 fill black
#  amove   2.55639105  1.44360902
#  circle 0.002 fill black
#  amove   2.55639105  1.4887218
#  circle 0.002 fill black
#  amove   2.55639105  1.5112782
#  circle 0.002 fill black
#  amove   2.55639105  1.52631579
#  circle 0.002 fill black
#  amove   2.55639105  1.63157895
#  circle 0.002 fill black
#  amove   2.56491235  1.48120301
#  circle 0.002 fill black
#  amove   2.56491235  1.51879699
#  circle 0.002 fill black
#  amove   2.56491235  1.52631579
#  circle 0.002 fill black
#  amove   2.56491235  1.53383459
#  circle 0.002 fill black
#  amove   2.56491235  1.55639098
#  circle 0.002 fill black
#  amove   2.56491235  1.57894737
#  circle 0.002 fill black
#  amove   2.57343366  1.42105263
#  circle 0.002 fill black
#  amove   2.57343366  1.45864662
#  circle 0.002 fill black
#  amove   2.57343366  1.4887218
#  circle 0.002 fill black
#  amove   2.57343366  1.57142857
#  circle 0.002 fill black
#  amove   2.58195496  1.45112782
#  circle 0.002 fill black
#  amove   2.58195496  1.46616541
#  circle 0.002 fill black
#  amove   2.58195496  1.4962406
#  circle 0.002 fill black
#  amove   2.58195496  1.52631579
#  circle 0.002 fill black
#  amove   2.58195496  1.54887218
#  circle 0.002 fill black
#  amove   2.58195496  1.57894737
#  circle 0.002 fill black
#  amove   2.59047626  1.39849624
#  circle 0.002 fill black
#  amove   2.59047626  1.43609023
#  circle 0.002 fill black
#  amove   2.59047626  1.47368421
#  circle 0.002 fill black
#  amove   2.59047626  1.4962406
#  circle 0.002 fill black
#  amove   2.59047626  1.57142857
#  circle 0.002 fill black
#  amove   2.59899757  1.43609023
#  circle 0.002 fill black
#  amove   2.59899757  1.4887218
#  circle 0.002 fill black
#  amove   2.59899757  1.54887218
#  circle 0.002 fill black
#  amove   2.59899757  1.56390977
#  circle 0.002 fill black
#  amove   2.60751887  1.39849624
#  circle 0.002 fill black
#  amove   2.60751887  1.42105263
#  circle 0.002 fill black
#  amove   2.60751887  1.47368421
#  circle 0.002 fill black
#  amove   2.60751887  1.51879699
#  circle 0.002 fill black
#  amove   2.61604017  1.39097744
#  circle 0.002 fill black
#  amove   2.61604017  1.46616541
#  circle 0.002 fill black
#  amove   2.61604017  1.5037594
#  circle 0.002 fill black
#  amove   2.61604017  1.54135338
#  circle 0.002 fill black
#  amove   2.61604017  1.57894737
#  circle 0.002 fill black
#  amove   2.62456148  1.43609023
#  circle 0.002 fill black
#  amove   2.62456148  1.54887218
#  circle 0.002 fill black
#  amove   2.62456148  1.55639098
#  circle 0.002 fill black
#  amove   2.63308278  1.44360902
#  circle 0.002 fill black
#  amove   2.63308278  1.46616541
#  circle 0.002 fill black
#  amove   2.63308278  1.47368421
#  circle 0.002 fill black
#  amove   2.63308278  1.48120301
#  circle 0.002 fill black
#  amove   2.63308278  1.51879699
#  circle 0.002 fill black
#  amove   2.63308278  1.52631579
#  circle 0.002 fill black
#  amove   2.63308278  1.55639098
#  circle 0.002 fill black
#  amove   2.63308278  1.60150376
#  circle 0.002 fill black
#  amove   2.64160408  1.42105263
#  circle 0.002 fill black
#  amove   2.64160408  1.44360902
#  circle 0.002 fill black
#  amove   2.64160408  1.5037594
#  circle 0.002 fill black
#  amove   2.65012539  1.4887218
#  circle 0.002 fill black
#  amove   2.65012539  1.5037594
#  circle 0.002 fill black
#  amove   2.65012539  1.51879699
#  circle 0.002 fill black
#  amove   2.65012539  1.54887218
#  circle 0.002 fill black
#  amove   2.65864669  1.45864662
#  circle 0.002 fill black
#  amove   2.65864669  1.47368421
#  circle 0.002 fill black
#  amove   2.66716799  1.40601504
#  circle 0.002 fill black
#  amove   2.66716799  1.46616541
#  circle 0.002 fill black
#  amove   2.66716799  1.57894737
#  circle 0.002 fill black
#  amove   2.6756893  1.5037594
#  circle 0.002 fill black
#  amove   2.6756893  1.5112782
#  circle 0.002 fill black
#  amove   2.6756893  1.51879699
#  circle 0.002 fill black
#  amove   2.6756893  1.52631579
#  circle 0.002 fill black
#  amove   2.6756893  1.59398496
#  circle 0.002 fill black
#  amove   2.6842106  1.41353383
#  circle 0.002 fill black
#  amove   2.6842106  1.44360902
#  circle 0.002 fill black
#  amove   2.6842106  1.48120301
#  circle 0.002 fill black
#  amove   2.6842106  1.63157895
#  circle 0.002 fill black
#  amove   2.69273191  1.47368421
#  circle 0.002 fill black
#  amove   2.69273191  1.4962406
#  circle 0.002 fill black
#  amove   2.69273191  1.5112782
#  circle 0.002 fill black
#  amove   2.69273191  1.51879699
#  circle 0.002 fill black
#  amove   2.69273191  1.52631579
#  circle 0.002 fill black
#  amove   2.70125321  1.40601504
#  circle 0.002 fill black
#  amove   2.70125321  1.43609023
#  circle 0.002 fill black
#  amove   2.70125321  1.4887218
#  circle 0.002 fill black
#  amove   2.70125321  1.5037594
#  circle 0.002 fill black
#  amove   2.70125321  1.5112782
#  circle 0.002 fill black
#  amove   2.70125321  1.51879699
#  circle 0.002 fill black
#  amove   2.70125321  1.54135338
#  circle 0.002 fill black
#  amove   2.70125321  1.60150376
#  circle 0.002 fill black
#  amove   2.70125321  1.62406015
#  circle 0.002 fill black
#  amove   2.70977451  1.40601504
#  circle 0.002 fill black
#  amove   2.70977451  1.42105263
#  circle 0.002 fill black
#  amove   2.70977451  1.53383459
#  circle 0.002 fill black
#  amove   2.70977451  1.55639098
#  circle 0.002 fill black
#  amove   2.70977451  1.57894737
#  circle 0.002 fill black
#  amove   2.70977451  1.59398496
#  circle 0.002 fill black
#  amove   2.71829582  1.36090226
#  circle 0.002 fill black
#  amove   2.71829582  1.48120301
#  circle 0.002 fill black
#  amove   2.71829582  1.4887218
#  circle 0.002 fill black
#  amove   2.71829582  1.4962406
#  circle 0.002 fill black
#  amove   2.71829582  1.57142857
#  circle 0.002 fill black
#  amove   2.72681712  1.39097744
#  circle 0.002 fill black
#  amove   2.72681712  1.52631579
#  circle 0.002 fill black
#  amove   2.73533842  1.48120301
#  circle 0.002 fill black
#  amove   2.73533842  1.4887218
#  circle 0.002 fill black
#  amove   2.73533842  1.56390977
#  circle 0.002 fill black
#  amove   2.74385973  1.45864662
#  circle 0.002 fill black
#  amove   2.74385973  1.48120301
#  circle 0.002 fill black
#  amove   2.74385973  1.4887218
#  circle 0.002 fill black
#  amove   2.74385973  1.52631579
#  circle 0.002 fill black
#  amove   2.74385973  1.54887218
#  circle 0.002 fill black
#  amove   2.75238103  1.4962406
#  circle 0.002 fill black
#  amove   2.75238103  1.51879699
#  circle 0.002 fill black
#  amove   2.75238103  1.53383459
#  circle 0.002 fill black
#  amove   2.75238103  1.54135338
#  circle 0.002 fill black
#  amove   2.76090233  1.45112782
#  circle 0.002 fill black
#  amove   2.76090233  1.46616541
#  circle 0.002 fill black
#  amove   2.76090233  1.47368421
#  circle 0.002 fill black
#  amove   2.76090233  1.4962406
#  circle 0.002 fill black
#  amove   2.76090233  1.60150376
#  circle 0.002 fill black
#  amove   2.76942364  1.41353383
#  circle 0.002 fill black
#  amove   2.76942364  1.42857143
#  circle 0.002 fill black
#  amove   2.76942364  1.46616541
#  circle 0.002 fill black
#  amove   2.76942364  1.48120301
#  circle 0.002 fill black
#  amove   2.76942364  1.5037594
#  circle 0.002 fill black
#  amove   2.76942364  1.5112782
#  circle 0.002 fill black
#  amove   2.76942364  1.51879699
#  circle 0.002 fill black
#  amove   2.76942364  1.52631579
#  circle 0.002 fill black
#  amove   2.76942364  1.53383459
#  circle 0.002 fill black
#  amove   2.76942364  1.54135338
#  circle 0.002 fill black
#  amove   2.76942364  1.55639098
#  circle 0.002 fill black
#  amove   2.77794494  1.45864662
#  circle 0.002 fill black
#  amove   2.77794494  1.5037594
#  circle 0.002 fill black
#  amove   2.77794494  1.52631579
#  circle 0.002 fill black
#  amove   2.77794494  1.53383459
#  circle 0.002 fill black
#  amove   2.77794494  1.55639098
#  circle 0.002 fill black
#  amove   2.78646624  1.41353383
#  circle 0.002 fill black
#  amove   2.78646624  1.44360902
#  circle 0.002 fill black
#  amove   2.78646624  1.45864662
#  circle 0.002 fill black
#  amove   2.78646624  1.46616541
#  circle 0.002 fill black
#  amove   2.78646624  1.48120301
#  circle 0.002 fill black
#  amove   2.78646624  1.5037594
#  circle 0.002 fill black
#  amove   2.78646624  1.53383459
#  circle 0.002 fill black
#  amove   2.78646624  1.57894737
#  circle 0.002 fill black
#  amove   2.79498755  1.44360902
#  circle 0.002 fill black
#  amove   2.79498755  1.45112782
#  circle 0.002 fill black
#  amove   2.79498755  1.51879699
#  circle 0.002 fill black
#  amove   2.79498755  1.54135338
#  circle 0.002 fill black
#  amove   2.79498755  1.54887218
#  circle 0.002 fill black
#  amove   2.80350885  1.45864662
#  circle 0.002 fill black
#  amove   2.80350885  1.4887218
#  circle 0.002 fill black
#  amove   2.80350885  1.54135338
#  circle 0.002 fill black
#  amove   2.80350885  1.54887218
#  circle 0.002 fill black
#  amove   2.80350885  1.57894737
#  circle 0.002 fill black
#  amove   2.81203015  1.46616541
#  circle 0.002 fill black
#  amove   2.81203015  1.5112782
#  circle 0.002 fill black
#  amove   2.81203015  1.55639098
#  circle 0.002 fill black
#  amove   2.82055146  1.44360902
#  circle 0.002 fill black
#  amove   2.82055146  1.45864662
#  circle 0.002 fill black
#  amove   2.82055146  1.46616541
#  circle 0.002 fill black
#  amove   2.82055146  1.4887218
#  circle 0.002 fill black
#  amove   2.82055146  1.4962406
#  circle 0.002 fill black
#  amove   2.82055146  1.5112782
#  circle 0.002 fill black
#  amove   2.82055146  1.53383459
#  circle 0.002 fill black
#  amove   2.82055146  1.58646617
#  circle 0.002 fill black
#  amove   2.82907276  1.44360902
#  circle 0.002 fill black
#  amove   2.82907276  1.4962406
#  circle 0.002 fill black
#  amove   2.82907276  1.5037594
#  circle 0.002 fill black
#  amove   2.82907276  1.52631579
#  circle 0.002 fill black
#  amove   2.82907276  1.61654135
#  circle 0.002 fill black
#  amove   2.83759406  1.45112782
#  circle 0.002 fill black
#  amove   2.83759406  1.4962406
#  circle 0.002 fill black
#  amove   2.83759406  1.56390977
#  circle 0.002 fill black
#  amove   2.83759406  1.57142857
#  circle 0.002 fill black
#  amove   2.83759406  1.61654135
#  circle 0.002 fill black
#  amove   2.84611537  1.47368421
#  circle 0.002 fill black
#  amove   2.85463667  1.53383459
#  circle 0.002 fill black
#  amove   2.85463667  1.55639098
#  circle 0.002 fill black
#  amove   2.85463667  1.63157895
#  circle 0.002 fill black
#  amove   2.86315798  1.5112782
#  circle 0.002 fill black
#  amove   2.86315798  1.53383459
#  circle 0.002 fill black
#  amove   2.86315798  1.58646617
#  circle 0.002 fill black
#  amove   2.87167928  1.45112782
#  circle 0.002 fill black
#  amove   2.87167928  1.47368421
#  circle 0.002 fill black
#  amove   2.87167928  1.4962406
#  circle 0.002 fill black
#  amove   2.87167928  1.5037594
#  circle 0.002 fill black
#  amove   2.88020058  1.45112782
#  circle 0.002 fill black
#  amove   2.88020058  1.4887218
#  circle 0.002 fill black
#  amove   2.88020058  1.51879699
#  circle 0.002 fill black
#  amove   2.88020058  1.52631579
#  circle 0.002 fill black
#  amove   2.88020058  1.55639098
#  circle 0.002 fill black
#  amove   2.88020058  1.57142857
#  circle 0.002 fill black
#  amove   2.88872189  1.44360902
#  circle 0.002 fill black
#  amove   2.88872189  1.45112782
#  circle 0.002 fill black
#  amove   2.88872189  1.47368421
#  circle 0.002 fill black
#  amove   2.88872189  1.48120301
#  circle 0.002 fill black
#  amove   2.88872189  1.4887218
#  circle 0.002 fill black
#  amove   2.88872189  1.5112782
#  circle 0.002 fill black
#  amove   2.88872189  1.52631579
#  circle 0.002 fill black
#  amove   2.89724319  1.41353383
#  circle 0.002 fill black
#  amove   2.89724319  1.5037594
#  circle 0.002 fill black
#  amove   2.89724319  1.51879699
#  circle 0.002 fill black
#  amove   2.89724319  1.53383459
#  circle 0.002 fill black
#  amove   2.89724319  1.60150376
#  circle 0.002 fill black
#  amove   2.90576449  1.45864662
#  circle 0.002 fill black
#  amove   2.90576449  1.46616541
#  circle 0.002 fill black
#  amove   2.90576449  1.48120301
#  circle 0.002 fill black
#  amove   2.90576449  1.54887218
#  circle 0.002 fill black
#  amove   2.90576449  1.57894737
#  circle 0.002 fill black
#  amove   2.90576449  1.61654135
#  circle 0.002 fill black
#  amove   2.9142858  1.42857143
#  circle 0.002 fill black
#  amove   2.9142858  1.47368421
#  circle 0.002 fill black
#  amove   2.9142858  1.53383459
#  circle 0.002 fill black
#  amove   2.9142858  1.55639098
#  circle 0.002 fill black
#  amove   2.9142858  1.62406015
#  circle 0.002 fill black
#  amove   2.9228071  1.44360902
#  circle 0.002 fill black
#  amove   2.9228071  1.47368421
#  circle 0.002 fill black
#  amove   2.9228071  1.4887218
#  circle 0.002 fill black
#  amove   2.9228071  1.4962406
#  circle 0.002 fill black
#  amove   2.9228071  1.57142857
#  circle 0.002 fill black
#  amove   2.9313284  1.39097744
#  circle 0.002 fill black
#  amove   2.9313284  1.45864662
#  circle 0.002 fill black
#  amove   2.9313284  1.46616541
#  circle 0.002 fill black
#  amove   2.9313284  1.5037594
#  circle 0.002 fill black
#  amove   2.9313284  1.5112782
#  circle 0.002 fill black
#  amove   2.9313284  1.52631579
#  circle 0.002 fill black
#  amove   2.9313284  1.54887218
#  circle 0.002 fill black
#  amove   2.9313284  1.57142857
#  circle 0.002 fill black
#  amove   2.93984971  1.48120301
#  circle 0.002 fill black
#  amove   2.93984971  1.5112782
#  circle 0.002 fill black
#  amove   2.93984971  1.51879699
#  circle 0.002 fill black
#  amove   2.94837101  1.39097744
#  circle 0.002 fill black
#  amove   2.94837101  1.44360902
#  circle 0.002 fill black
#  amove   2.94837101  1.48120301
#  circle 0.002 fill black
#  amove   2.94837101  1.4962406
#  circle 0.002 fill black
#  amove   2.94837101  1.5037594
#  circle 0.002 fill black
#  amove   2.94837101  1.5112782
#  circle 0.002 fill black
#  amove   2.94837101  1.54135338
#  circle 0.002 fill black
#  amove   2.94837101  1.57142857
#  circle 0.002 fill black
#  amove   2.95689231  1.45864662
#  circle 0.002 fill black
#  amove   2.95689231  1.46616541
#  circle 0.002 fill black
#  amove   2.95689231  1.4887218
#  circle 0.002 fill black
#  amove   2.95689231  1.4962406
#  circle 0.002 fill black
#  amove   2.95689231  1.5112782
#  circle 0.002 fill black
#  amove   2.96541362  1.36842105
#  circle 0.002 fill black
#  amove   2.96541362  1.42857143
#  circle 0.002 fill black
#  amove   2.96541362  1.4962406
#  circle 0.002 fill black
#  amove   2.96541362  1.5112782
#  circle 0.002 fill black
#  amove   2.96541362  1.54135338
#  circle 0.002 fill black
#  amove   2.96541362  1.54887218
#  circle 0.002 fill black
#  amove   2.96541362  1.55639098
#  circle 0.002 fill black
#  amove   2.96541362  1.63909774
#  circle 0.002 fill black
#  amove   2.97393492  1.43609023
#  circle 0.002 fill black
#  amove   2.97393492  1.45112782
#  circle 0.002 fill black
#  amove   2.97393492  1.51879699
#  circle 0.002 fill black
#  amove   2.97393492  1.52631579
#  circle 0.002 fill black
#  amove   2.97393492  1.53383459
#  circle 0.002 fill black
#  amove   2.98245622  1.48120301
#  circle 0.002 fill black
#  amove   2.98245622  1.56390977
#  circle 0.002 fill black
#  amove   2.99097753  1.42857143
#  circle 0.002 fill black
#  amove   2.99097753  1.45864662
#  circle 0.002 fill black
#  amove   2.99097753  1.4887218
#  circle 0.002 fill black
#  amove   2.99097753  1.4962406
#  circle 0.002 fill black
#  amove   2.99097753  1.54135338
#  circle 0.002 fill black
#  amove   2.99097753  1.63157895
#  circle 0.002 fill black
#  amove   2.99949883  1.45112782
#  circle 0.002 fill black
#  amove   2.99949883  1.45864662
#  circle 0.002 fill black
#  amove   2.99949883  1.4887218
#  circle 0.002 fill black
#  amove   3.00802013  1.40601504
#  circle 0.002 fill black
#  amove   3.00802013  1.43609023
#  circle 0.002 fill black
#  amove   3.00802013  1.45112782
#  circle 0.002 fill black
#  amove   3.00802013  1.46616541
#  circle 0.002 fill black
#  amove   3.00802013  1.5037594
#  circle 0.002 fill black
#  amove   3.00802013  1.56390977
#  circle 0.002 fill black
#  amove   3.00802013  1.59398496
#  circle 0.002 fill black
#  amove   3.01654144  1.39849624
#  circle 0.002 fill black
#  amove   3.01654144  1.42857143
#  circle 0.002 fill black
#  amove   3.01654144  1.45864662
#  circle 0.002 fill black
#  amove   3.01654144  1.47368421
#  circle 0.002 fill black
#  amove   3.01654144  1.48120301
#  circle 0.002 fill black
#  amove   3.01654144  1.4962406
#  circle 0.002 fill black
#  amove   3.01654144  1.5112782
#  circle 0.002 fill black
#  amove   3.01654144  1.51879699
#  circle 0.002 fill black
#  amove   3.01654144  1.52631579
#  circle 0.002 fill black
#  amove   3.01654144  1.56390977
#  circle 0.002 fill black
#  amove   3.02506274  1.44360902
#  circle 0.002 fill black
#  amove   3.02506274  1.46616541
#  circle 0.002 fill black
#  amove   3.02506274  1.52631579
#  circle 0.002 fill black
#  amove   3.02506274  1.54887218
#  circle 0.002 fill black
#  amove   3.02506274  1.55639098
#  circle 0.002 fill black
#  amove   3.03358404  1.56390977
#  circle 0.002 fill black
#  amove   3.03358404  1.58646617
#  circle 0.002 fill black
#  amove   3.04210535  1.39849624
#  circle 0.002 fill black
#  amove   3.04210535  1.40601504
#  circle 0.002 fill black
#  amove   3.04210535  1.42105263
#  circle 0.002 fill black
#  amove   3.04210535  1.46616541
#  circle 0.002 fill black
#  amove   3.04210535  1.5112782
#  circle 0.002 fill black
#  amove   3.04210535  1.51879699
#  circle 0.002 fill black
#  amove   3.04210535  1.53383459
#  circle 0.002 fill black
#  amove   3.05062665  1.40601504
#  circle 0.002 fill black
#  amove   3.05062665  1.44360902
#  circle 0.002 fill black
#  amove   3.05062665  1.46616541
#  circle 0.002 fill black
#  amove   3.05062665  1.48120301
#  circle 0.002 fill black
#  amove   3.05062665  1.4887218
#  circle 0.002 fill black
#  amove   3.05062665  1.52631579
#  circle 0.002 fill black
#  amove   3.05062665  1.53383459
#  circle 0.002 fill black
#  amove   3.05914796  1.40601504
#  circle 0.002 fill black
#  amove   3.05914796  1.45864662
#  circle 0.002 fill black
#  amove   3.05914796  1.5112782
#  circle 0.002 fill black
#  amove   3.05914796  1.54135338
#  circle 0.002 fill black
#  amove   3.05914796  1.55639098
#  circle 0.002 fill black
#  amove   3.05914796  1.57142857
#  circle 0.002 fill black
#  amove   3.05914796  1.57894737
#  circle 0.002 fill black
#  amove   3.05914796  1.60150376
#  circle 0.002 fill black
#  amove   3.06766926  1.44360902
#  circle 0.002 fill black
#  amove   3.06766926  1.4887218
#  circle 0.002 fill black
#  amove   3.06766926  1.5037594
#  circle 0.002 fill black
#  amove   3.06766926  1.5112782
#  circle 0.002 fill black
#  amove   3.07619056  1.42105263
#  circle 0.002 fill black
#  amove   3.07619056  1.46616541
#  circle 0.002 fill black
#  amove   3.07619056  1.5037594
#  circle 0.002 fill black
#  amove   3.07619056  1.51879699
#  circle 0.002 fill black
#  amove   3.07619056  1.52631579
#  circle 0.002 fill black
#  amove   3.07619056  1.53383459
#  circle 0.002 fill black
#  amove   3.07619056  1.55639098
#  circle 0.002 fill black
#  amove   3.08471187  1.42857143
#  circle 0.002 fill black
#  amove   3.08471187  1.45112782
#  circle 0.002 fill black
#  amove   3.08471187  1.51879699
#  circle 0.002 fill black
#  amove   3.08471187  1.57142857
#  circle 0.002 fill black
#  amove   3.09323317  1.40601504
#  circle 0.002 fill black
#  amove   3.09323317  1.45864662
#  circle 0.002 fill black
#  amove   3.09323317  1.47368421
#  circle 0.002 fill black
#  amove   3.09323317  1.4962406
#  circle 0.002 fill black
#  amove   3.09323317  1.54135338
#  circle 0.002 fill black
#  amove   3.09323317  1.54887218
#  circle 0.002 fill black
#  amove   3.09323317  1.61654135
#  circle 0.002 fill black
#  amove   3.10175447  1.40601504
#  circle 0.002 fill black
#  amove   3.10175447  1.4887218
#  circle 0.002 fill black
#  amove   3.10175447  1.5037594
#  circle 0.002 fill black
#  amove   3.11027578  1.43609023
#  circle 0.002 fill black
#  amove   3.11027578  1.47368421
#  circle 0.002 fill black
#  amove   3.11027578  1.51879699
#  circle 0.002 fill black
#  amove   3.11027578  1.52631579
#  circle 0.002 fill black
#  amove   3.11027578  1.59398496
#  circle 0.002 fill black
#  amove   3.11879708  1.4962406
#  circle 0.002 fill black
#  amove   3.11879708  1.62406015
#  circle 0.002 fill black
#  amove   3.12731838  1.42857143
#  circle 0.002 fill black
#  amove   3.12731838  1.44360902
#  circle 0.002 fill black
#  amove   3.12731838  1.4887218
#  circle 0.002 fill black
#  amove   3.12731838  1.4962406
#  circle 0.002 fill black
#  amove   3.12731838  1.55639098
#  circle 0.002 fill black
#  amove   3.13583969  1.47368421
#  circle 0.002 fill black
#  amove   3.13583969  1.4962406
#  circle 0.002 fill black
#  amove   3.13583969  1.5037594
#  circle 0.002 fill black
#  amove   3.13583969  1.51879699
#  circle 0.002 fill black
#  amove   3.13583969  1.54135338
#  circle 0.002 fill black
#  amove   3.13583969  1.59398496
#  circle 0.002 fill black
#  amove   3.14436099  1.44360902
#  circle 0.002 fill black
#  amove   3.14436099  1.48120301
#  circle 0.002 fill black
#  amove   3.14436099  1.54887218
#  circle 0.002 fill black
#  amove   3.14436099  1.57894737
#  circle 0.002 fill black
#  amove   3.15288229  1.40601504
#  circle 0.002 fill black
#  amove   3.15288229  1.48120301
#  circle 0.002 fill black
#  amove   3.15288229  1.4887218
#  circle 0.002 fill black
#  amove   3.15288229  1.53383459
#  circle 0.002 fill black
#  amove   3.15288229  1.62406015
#  circle 0.002 fill black
#  amove   3.1614036  1.38345865
#  circle 0.002 fill black
#  amove   3.1614036  1.45112782
#  circle 0.002 fill black
#  amove   3.1614036  1.54135338
#  circle 0.002 fill black
#  amove   3.1699249  1.43609023
#  circle 0.002 fill black
#  amove   3.1699249  1.44360902
#  circle 0.002 fill black
#  amove   3.1699249  1.46616541
#  circle 0.002 fill black
#  amove   3.1699249  1.51879699
#  circle 0.002 fill black
#  amove   3.1699249  1.53383459
#  circle 0.002 fill black
#  amove   3.1784462  1.38345865
#  circle 0.002 fill black
#  amove   3.1784462  1.44360902
#  circle 0.002 fill black
#  amove   3.1784462  1.45864662
#  circle 0.002 fill black
#  amove   3.1784462  1.5037594
#  circle 0.002 fill black
#  amove   3.1784462  1.52631579
#  circle 0.002 fill black
#  amove   3.18696751  1.45864662
#  circle 0.002 fill black
#  amove   3.18696751  1.4962406
#  circle 0.002 fill black
#  amove   3.18696751  1.57894737
#  circle 0.002 fill black
#  amove   3.18696751  1.60150376
#  circle 0.002 fill black
#  amove   3.19548881  1.39849624
#  circle 0.002 fill black
#  amove   3.19548881  1.44360902
#  circle 0.002 fill black
#  amove   3.19548881  1.52631579
#  circle 0.002 fill black
#  amove   3.19548881  1.53383459
#  circle 0.002 fill black
#  amove   3.19548881  1.57894737
#  circle 0.002 fill black
#  amove   3.19548881  1.62406015
#  circle 0.002 fill black
#  amove   3.20401011  1.46616541
#  circle 0.002 fill black
#  amove   3.20401011  1.4962406
#  circle 0.002 fill black
#  amove   3.20401011  1.51879699
#  circle 0.002 fill black
#  amove   3.20401011  1.52631579
#  circle 0.002 fill black
#  amove   3.20401011  1.60902256
#  circle 0.002 fill black
#  amove   3.21253142  1.41353383
#  circle 0.002 fill black
#  amove   3.21253142  1.53383459
#  circle 0.002 fill black
#  amove   3.21253142  1.56390977
#  circle 0.002 fill black
#  amove   3.22105272  1.4962406
#  circle 0.002 fill black
#  amove   3.22105272  1.53383459
#  circle 0.002 fill black
#  amove   3.22105272  1.57894737
#  circle 0.002 fill black
#  amove   3.22957403  1.46616541
#  circle 0.002 fill black
#  amove   3.22957403  1.5037594
#  circle 0.002 fill black
#  amove   3.22957403  1.51879699
#  circle 0.002 fill black
#  amove   3.22957403  1.52631579
#  circle 0.002 fill black
#  amove   3.22957403  1.55639098
#  circle 0.002 fill black
#  amove   3.22957403  1.63909774
#  circle 0.002 fill black
#  amove   3.23809533  1.47368421
#  circle 0.002 fill black
#  amove   3.23809533  1.5037594
#  circle 0.002 fill black
#  amove   3.24661663  1.44360902
#  circle 0.002 fill black
#  amove   3.24661663  1.45112782
#  circle 0.002 fill black
#  amove   3.24661663  1.4962406
#  circle 0.002 fill black
#  amove   3.24661663  1.55639098
#  circle 0.002 fill black
#  amove   3.24661663  1.58646617
#  circle 0.002 fill black
#  amove   3.25513794  1.44360902
#  circle 0.002 fill black
#  amove   3.25513794  1.45112782
#  circle 0.002 fill black
#  amove   3.25513794  1.46616541
#  circle 0.002 fill black
#  amove   3.25513794  1.4962406
#  circle 0.002 fill black
#  amove   3.25513794  1.57894737
#  circle 0.002 fill black
#  amove   3.26365924  1.45112782
#  circle 0.002 fill black
#  amove   3.26365924  1.46616541
#  circle 0.002 fill black
#  amove   3.26365924  1.48120301
#  circle 0.002 fill black
#  amove   3.26365924  1.5112782
#  circle 0.002 fill black
#  amove   3.26365924  1.57142857
#  circle 0.002 fill black
#  amove   3.27218054  1.56390977
#  circle 0.002 fill black
#  amove   3.28070185  1.45864662
#  circle 0.002 fill black
#  amove   3.28070185  1.55639098
#  circle 0.002 fill black
#  amove   3.28070185  1.68421053
#  circle 0.002 fill black
#  amove   3.28922315  1.44360902
#  circle 0.002 fill black
#  amove   3.28922315  1.45864662
#  circle 0.002 fill black
#  amove   3.28922315  1.4962406
#  circle 0.002 fill black
#  amove   3.28922315  1.54887218
#  circle 0.002 fill black
#  amove   3.28922315  1.56390977
#  circle 0.002 fill black
#  amove   3.29774445  1.44360902
#  circle 0.002 fill black
#  amove   3.29774445  1.48120301
#  circle 0.002 fill black
#  amove   3.29774445  1.4962406
#  circle 0.002 fill black
#  amove   3.29774445  1.5037594
#  circle 0.002 fill black
#  amove   3.30626576  1.44360902
#  circle 0.002 fill black
#  amove   3.30626576  1.46616541
#  circle 0.002 fill black
#  amove   3.30626576  1.47368421
#  circle 0.002 fill black
#  amove   3.30626576  1.51879699
#  circle 0.002 fill black
#  amove   3.30626576  1.57894737
#  circle 0.002 fill black
#  amove   3.31478706  1.48120301
#  circle 0.002 fill black
#  amove   3.31478706  1.5037594
#  circle 0.002 fill black
#  amove   3.31478706  1.5112782
#  circle 0.002 fill black
#  amove   3.31478706  1.54135338
#  circle 0.002 fill black
#  amove   3.31478706  1.58646617
#  circle 0.002 fill black
#  amove   3.32330836  1.42105263
#  circle 0.002 fill black
#  amove   3.32330836  1.45864662
#  circle 0.002 fill black
#  amove   3.32330836  1.48120301
#  circle 0.002 fill black
#  amove   3.32330836  1.4887218
#  circle 0.002 fill black
#  amove   3.32330836  1.5037594
#  circle 0.002 fill black
#  amove   3.32330836  1.57142857
#  circle 0.002 fill black
#  amove   3.32330836  1.64661654
#  circle 0.002 fill black
#  amove   3.33182967  1.42857143
#  circle 0.002 fill black
#  amove   3.33182967  1.45112782
#  circle 0.002 fill black
#  amove   3.33182967  1.46616541
#  circle 0.002 fill black
#  amove   3.33182967  1.4887218
#  circle 0.002 fill black
#  amove   3.33182967  1.52631579
#  circle 0.002 fill black
#  amove   3.34035097  1.48120301
#  circle 0.002 fill black
#  amove   3.34035097  1.5112782
#  circle 0.002 fill black
#  amove   3.34035097  1.51879699
#  circle 0.002 fill black
#  amove   3.34035097  1.56390977
#  circle 0.002 fill black
#  amove   3.34887227  1.46616541
#  circle 0.002 fill black
#  amove   3.34887227  1.52631579
#  circle 0.002 fill black
#  amove   3.34887227  1.54135338
#  circle 0.002 fill black
#  amove   3.35739358  1.47368421
#  circle 0.002 fill black
#  amove   3.35739358  1.5112782
#  circle 0.002 fill black
#  amove   3.36591488  1.40601504
#  circle 0.002 fill black
#  amove   3.36591488  1.46616541
#  circle 0.002 fill black
#  amove   3.36591488  1.4887218
#  circle 0.002 fill black
#  amove   3.36591488  1.5037594
#  circle 0.002 fill black
#  amove   3.36591488  1.52631579
#  circle 0.002 fill black
#  amove   3.36591488  1.54887218
#  circle 0.002 fill black
#  amove   3.36591488  1.61654135
#  circle 0.002 fill black
#  amove   3.37443618  1.40601504
#  circle 0.002 fill black
#  amove   3.37443618  1.45864662
#  circle 0.002 fill black
#  amove   3.37443618  1.4887218
#  circle 0.002 fill black
#  amove   3.37443618  1.4962406
#  circle 0.002 fill black
#  amove   3.37443618  1.53383459
#  circle 0.002 fill black
#  amove   3.38295749  1.33082707
#  circle 0.002 fill black
#  amove   3.38295749  1.39849624
#  circle 0.002 fill black
#  amove   3.38295749  1.40601504
#  circle 0.002 fill black
#  amove   3.38295749  1.45112782
#  circle 0.002 fill black
#  amove   3.38295749  1.45864662
#  circle 0.002 fill black
#  amove   3.38295749  1.54887218
#  circle 0.002 fill black
#  amove   3.38295749  1.55639098
#  circle 0.002 fill black
#  amove   3.38295749  1.60902256
#  circle 0.002 fill black
#  amove   3.39147879  1.40601504
#  circle 0.002 fill black
#  amove   3.39147879  1.45112782
#  circle 0.002 fill black
#  amove   3.39147879  1.5112782
#  circle 0.002 fill black
#  amove   3.4000001  1.46616541
#  circle 0.002 fill black
#  amove   3.4000001  1.51879699
#  circle 0.002 fill black
#  amove   3.4000001  1.52631579
#  circle 0.002 fill black
# set hei 1
# amove xoff yoff-1.2
# rline 0 2.7 arrow end
# amove xoff yoff
# rline xs*8 0 arrow end
# set font psh
# set hei 0.3
# amove xoff-0.2 yoff+1.5
# set just br
# begin rotate 90
#  text Feldst\"arke
# end rotate
# amove xoff+xs*8 yoff+0.2
# set just br
# text Zeit
# amove xoff+xs*8-0.2 yoff-1.2
# 
# end translate
