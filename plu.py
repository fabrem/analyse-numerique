# Méthode de décomposition -> 1. Ly = b ( trouver y ) 2. Ux = y (trouver x)
import numpy as np
from scipy.linalg import lu

A = np.array([[3, -2, 2], [1, 2, 3], [2, -2, -1]])
L, U = lu(A, permute_l=True)

print(f"A = \n{A}")
print(f"L = \n{L}")
print(f"U = \n{U}")

