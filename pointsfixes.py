from math import *
from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np


def iteration(g, x0, Ea, N) -> Tuple[float, List]:
    i = 0
    error = 1
    xp = []
    xn = 0
    while error > Ea and i < N:
        xn = g(x0)
        error = abs(x0 - xn)
        x0 = xn
        xp.append(x0)
        i += 1
    print(xp)
    return xn, xp


def plot(xf, xp, x_start, given_function):
    function_v = np.vectorize(given_function)

    x = np.linspace(x_start, xf, 100)
    y = function_v(x)
    plt.plot(x, y)
    plt.plot(xp, function_v(xp), 'bo')
    plt.plot(x_start, given_function(x_start), 'ro')
    plt.plot(xf, given_function(xf), 'go')
    plt.plot(x, x, 'k')
    plt.show()


def main():
    g1 = lambda x: -2**x + 2
    g2 = lambda x: -2/x**3
    g3 = lambda x: -4*(1-x)**3
    g4 = lambda x: 3*x**2 - 2*x + 1
    x0 = 1
    N = 100
    Ea = 1e-10

    xf, xp = iteration(g1, x0, Ea, N)
    plot(xf, xp, x0, g1)
    # xf, xp = iteration(g2, x0, Ea, N)
    # xf, xp = iteration(g3, x0, Ea, N)
    # xf, xp = iteration(g4, x0, Ea, N)


if __name__ == '__main__':
    main()
