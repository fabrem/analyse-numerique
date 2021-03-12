# Méthode de décomposition -> 1. Ly = b ( trouver y ) 2. Ux = y (trouver x)
import numpy as np
A = np.array([[1, 2, 0], [2, 3, 2], [0, 1, 4]])

# A = np.array([[60.0, 30.0, 20.0], [30.0, 20.0, 15.0], [20.0, 15.0, 12.0]])
def crout(A):
    """
    Returns the lower-triangular matrix L and the unit upper-triangular
    matrix U such that L*U = the given matrix A.
    The computation uses Crout's Algorithm to perform LU decomposition on A.
    INPUT:
        - A: list; the square matrix to decompose
    OUTPUT:
        - list; the matrix L followed by the matrix U
    """
    # This is Crout's Algorithm.
    n = len(A)
    L = [[0] * n for i in range(n)]
    U = [[0] * n for i in range(n)]
    for j in range(n):
        U[j][j] = 1             # set the j,j-th entry of U to 1
        for i in range(j, n):  # starting at L[j][j], solve j-th column of L
            alpha = float(A[i][j])
            for k in range(j):
                alpha -= L[i][k]*U[k][j]
            L[i][j] = alpha
        for i in range(j+1, n):# starting at U[j][j+1], solve j-th row of U
            tempU = float(A[j][i])
            for k in range(j):
                tempU -= L[j][k]*U[k][i]
            # if int(L[j][j]) == 0:
            #     L[j][j] = e-40
            U[j][i] = tempU/L[j][j]

    return [np.array(L), np.array(U)]

L, U = crout(A)
print("Crout")
print(f"A = \n{A}")
print(f"L = \n{L}")
print(f"U = \n{U}")
