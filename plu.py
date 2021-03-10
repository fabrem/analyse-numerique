# Méthode de décomposition -> 1. Ly = b ( trouver y ) 2. Ux = y (trouver x)
import numpy as np
from scipy.linalg import lu

A = np.array([[2, -2, 0, 4], [1, -2, 1, 2], [6, -5, 7, 4], [0, 0, -3, 6]])
P, L, U = lu(A)
print(f"A = \n{A}")
print(f"P = \n{P}")
print(f"L = \n{L}")
print(f"U = \n{U}")

