#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q2: A^2 = A  =>  (I+A)^2 - 3A = I
import numpy as np
#Random idempotent matrix: orthogonal projector P = M (M^T M)^{-1} M^T
rng = np.random.default_rng(1)
M = rng.standard_normal((4, 2))
A = M @ np.linalg.inv(M.T @ M) @ M.T
I = np.eye(4)
print("A^2 = A :", np.allclose(A @ A, A))
print("(I+A)^2 - 3A = I :", np.allclose((I + A) @ (I + A) - 3*A, I))
