"""Fixed Point Iteration"""
import numpy as np
import math
def F(x):
    return x**3 + x - 1

def g(x):
    return (1-x)**(1/3)
x0 = 0.5
err = 0.0005

x0 = 0.5
err = 0.00005
#x = x0


for i in range(2000):
    x = g(x0)
    if math.fabs(x - x0) < err:
        print(x, f"iteration {i}")
        break
    else:
        x0 = x
