import numpy as np
from scipy.linalg import solve

A = np.array([[2, -2, 0, 4], [1, -2, 1, 2], [6, -5, 7, 4], [0, 0, -3, 6]])
b = np.array([2, 1, 6, 3])

print(f"For equation Ax =b\nA={A}, b={b}\n We have x={solve(A,b)}")
