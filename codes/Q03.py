#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q3: x(2,3)^T + y(-1,1)^T = (10,5)^T
import numpy as np
A = np.array([[2, -1], [3, 1]], dtype=float)
b = np.array([[10], [5]], dtype=float)
sol = np.linalg.solve(A, b)
print("x =", sol[0, 0], " y =", sol[1, 0])
Ab = np.hstack([A, b])
print("rank A =", np.linalg.matrix_rank(A), " rank [A|b] =", np.linalg.matrix_rank(Ab), " unknowns = 2")
