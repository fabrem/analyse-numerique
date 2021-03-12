from math import exp, cos


def g(f, x: float):
    """First-order divided difference function.

    Arguments:
        f(callable): Function input to g
        x(float): Point at which to evaluate g
    """
    return lambda x: f(x + f(x)) / f(x) - 1


def steff(f, x: float):
    """Steffenson algorithm for finding roots.

    This recursive generator yields the x_n+1 value first then, when the generator iterates,
    it yields x_n + 2 from the next level of recursion.

    Arguments:
        f(callable): Function whose root we are searching for
        x(float): Starting value upon first call, each level n that the function recurses x is x_n
    """
    print(x)
    if g(f, x)(x) != 0:
        yield x - f(x) / g(f, x)(x)  # First give x_n + 1
        yield from steff(f, x - f(x) / g(f, x)(x))  # Then give new iterator


if __name__ == '__main__':
    special_func = lambda x: cos(x)
    binou = steff(special_func, 0)
    for element in binou:
        print(element)