#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q28: (AB)^-1 = B^-1 A^-1  for the given A^-1 and B
import sympy as sp
Ai = sp.Matrix([[3, -1, 1], [-15, 6, -5], [5, -2, 2]])
B = sp.Matrix([[1, 2, -2], [-1, 3, 0], [0, -2, 1]])
print("det B =", B.det(), " B^-1 =", B.inv().tolist())
ABi = B.inv()*Ai
print("(AB)^-1 = B^-1 A^-1 =", ABi.tolist())
A_ = Ai.inv()
print("check (A B)(B^-1 A^-1) = I :", (A_*B*ABi) == sp.eye(3))
