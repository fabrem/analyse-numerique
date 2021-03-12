from autograd import grad

def ordre(g, r, Nmax=10):
    counter = 1
    dG = grad(g)
    fdG = dG(r)
    if abs(fdG) < 1 and abs(fdG) != 0:
        # ordre, taux de convergence
        return counter, fdG
    elif abs(fdG) > 1:
        raise Exception("Buddey ca dix verges")

    while counter < Nmax or fdG == 0:
        counter += 1
        dG = grad(dG)
        fdG = dG(r)
        if fdG != 0:
            return counter, fdG

    raise Exception("sauce qui peut")


g = lambda x: 1 + x + x**2 + x**3
r = 0.0
print(ordre(g, r))
