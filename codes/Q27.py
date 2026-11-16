#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q27: solve x-y+z=4, 2x+y-3z=0, x+y+z=2
import sympy as sp
A = sp.Matrix([[1, -1, 1], [2, 1, -3], [1, 1, 1]])
b = sp.Matrix([4, 0, 2])
print("det A =", A.det(), " solution =", list(A.LUsolve(b)), " rref:", A.row_join(b).rref()[0].tolist())
