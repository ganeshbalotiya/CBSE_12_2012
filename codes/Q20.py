#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q20: integral of x^2 atan x dx
import sympy as sp
x = sp.symbols('x')
F1 = x**3/3*sp.atan(x) - x**2/6 + sp.log(1 + x**2)/6
print("d/dx F1 - x^2 atan x =", sp.simplify(sp.diff(F1, x) - x**2*sp.atan(x)))
