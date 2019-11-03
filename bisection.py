import math
def F(x):
    val = x**3 + 4*(x**2) - 10 
    return val

def SameSign(a,b):
    neg = ((a < 0) and (b < 0)) #or ((b < 0) and (a < 0))
    pos = (a >= 0) and (b >= 0) #or ((b >= 0) and (a >= 0))
    return (neg or pos)

def sign(a):
    if a < 0:
        return -1
    elif a == 0:
        return 0
    else:
        return 1
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
        if sign(fc) * sign(fa) > 0:
            a = c
            fa = fc
        else:
            b = c
            fb = fc

        
