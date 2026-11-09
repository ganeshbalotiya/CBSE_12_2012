#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q24: plane through (2,1,-1), (-1,3,4) perpendicular to x - 2y + 4z = 10; contains the given line
import numpy as np
P1 = np.array([2, 1, -1]); P2 = np.array([-1, 3, 4])
n0 = np.array([1, -2, 4])
n = np.cross(P2 - P1, n0)
c = n @ P1
print("normal =", n, " n.r = ", c, " check P2:", n @ P2)
A0 = np.array([-1, 3, 4]); d = np.array([3, -2, -5])
print("n.d =", n @ d, " n.A0 - c =", n @ A0 - c)
# stack as a linear system:  [ (P2-P1)^T ; n0^T ] n = 0
M = np.vstack([P2 - P1, n0])
u, s, vt = np.linalg.svd(M)
nn = vt[-1]
print("null-space direction (normalised):", nn/nn[0]*18)
