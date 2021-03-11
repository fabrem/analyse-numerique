# Méthode de décomposition -> 1. Ly = b ( trouver y ) 2. Ux = y (trouver x)
import numpy as np
from scipy.linalg import lu

A = np.array([[1, 1, 0], [1, 2, 1], [0, 1, 2]])
L, U = lu(A, permute_l=True)
# def crout(A):

#     L = np.zeros((3, 3))
#     U = np.zeros((3, 3))

#     for k in range(0, 3):
#         U[k, k] = 1

#         for j in range(k, 3):
#             sum0 = sum(L[k, s] * U[s, j] for s in range(1, k-1))
#             #reversed
#             L[j, k] = A[k, k] - sum0

#         for j in range(k, 3):
#             sum1 = sum(L[k, s] * U[s, j] for s in range(1, k-1))
#             U[k, j] = (A[k, j] - sum1) / L[k, k]

#     return L, U

# L, U = crout(A)
print(f"A = \n{A}")
print(f"L = \n{L}")
print(f"U = \n{U}")

