#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q20: solve x-y+z=4, 2x+y-3z=0, x+y+z=2 ; OR (AB)^-1 = B^-1 A^-1
import numpy as np
import sympy as sp
A = sp.Matrix([[1, -1, 1], [2, 1, -3], [1, 1, 1]])
b = sp.Matrix([4, 0, 2])
print("det A =", A.det(), " solution =", list(A.LUsolve(b)), " rref:", A.row_join(b).rref()[0].tolist())
# OR part
Ai = sp.Matrix([[3, -1, 1], [-15, 6, -5], [5, -2, 2]])
B = sp.Matrix([[1, 2, -2], [-1, 3, 0], [0, -2, 1]])
print("det B =", B.det(), " B^-1 =", B.inv().tolist())
ABi = B.inv()*Ai
print("(AB)^-1 = B^-1 A^-1 =", ABi.tolist())
A_ = Ai.inv()
print("check (A B)(B^-1 A^-1) = I :", (A_*B*ABi) == sp.eye(3))
