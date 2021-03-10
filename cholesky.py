import numpy as np
from scipy.linalg import cholesky

# A doit être symétrique
A = np.array([[25, 5, 10], [5, 10, 2], [10, 2, 13]])

L = cholesky(A)
print(f"L=\n{L}")
