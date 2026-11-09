#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q10: determinant = a^3 via elementary row operations (L M = U, det L = 1)
import sympy as sp
a, b, c = sp.symbols('a b c')
M = sp.Matrix([[a, a + b, a + b + c],
               [2*a, 3*a + 2*b, 4*a + 3*b + 2*c],
               [3*a, 6*a + 3*b, 10*a + 6*b + 3*c]])
E1 = sp.Matrix([[1, 0, 0], [-2, 1, 0], [-3, 0, 1]])     # R2-2R1, R3-3R1
E2 = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, -3, 1]])       # R3-3R2
U = sp.simplify(E2*E1*M)
print("U =", U)
print("det M =", sp.factor(M.det()))
