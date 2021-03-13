from autograd import grad
import autograd.numpy as np
from math import sin, cos

def ordre(g, r, Nmax=10):
    counter = 1
    dG = grad(g)
    fdG = dG(r)
    if abs(fdG) < 1 and abs(fdG) != 0:
        # ordre, taux de convergence
        return counter, fdG
    elif abs(fdG) > 1:
        raise Exception("Buddey ca dix verges")
    elif abs(fdG) == 1:
        raise Exception("Buddey cest in des terres minées")

    while counter < Nmax or fdG == 0:
        counter += 1
        dG = grad(dG)
        fdG = dG(r)
        if fdG != 0:
            return counter, fdG

    raise Exception("sauce qui peut")


g1 = lambda x: x**2 - x
g2 = lambda x: np.sin(x)
g3 = lambda x: np.cos(x) - 1
g4 = lambda x: x**2 - (1/2) * x

r = 0.0
# print(ordre(g1, r))
# print(ordre(g2, r))
print(ordre(g3, r))
print(ordre(g4, r))
