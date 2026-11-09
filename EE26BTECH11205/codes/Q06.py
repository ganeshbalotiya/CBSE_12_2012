#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q6: area of the parallelogram spanned by 2i and 3j
import numpy as np
a = np.array([2, 0, 0]); b = np.array([0, 3, 0])
print("area =", np.linalg.norm(np.cross(a, b)))
print("check |det [a b]| in the plane =", abs(np.linalg.det(np.array([[2, 0], [0, 3]]))))
M = np.array([[2, 0], [0, 3]], dtype=float)
print("Gram: sqrt(det(M^T M)) =", np.sqrt(np.linalg.det(M.T @ M)))
