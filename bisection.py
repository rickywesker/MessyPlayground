#Bisection Method for root finding.
import math
def F(x):
    val = x**6 - x - 1.0
    return val

def SameSign(a,b):
    neg = ((a < 0) and (b < 0)) #or ((b < 0) and (a < 0))
    pos = (a >= 0) and (b >= 0) #or ((b >= 0) and (a >= 0))
    return (neg or pos)
def Bisection(a1,b1,TOL,N):
    val = []
    x = []
    a = a1
    b = b1
    fa = F(a)
    fb = F(b)
    delta = b - a
    if SameSign(fa,fb):
        return True
    for i in range(N):
        delta = delta / 2
        c = a + delta
        fc = F(c)
        val.append("F(x{}) = {}".format(i,fc))
        x.append("x{} = {}".format(i,c))
        if math.fabs(delta) < TOL:
            return fc, c, val, x
        if SameSign(fc,fa):
            a = c
            fa = fc
        else:
            b = c
            fb = fc

        
