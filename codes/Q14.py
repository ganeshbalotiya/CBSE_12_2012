#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q14: integral of x^2 atan x dx ; OR integral of (3x-1)/(x+2)^2 dx
import sympy as sp
x = sp.symbols('x')
F1 = x**3/3*sp.atan(x) - x**2/6 + sp.log(1 + x**2)/6
print("d/dx F1 - x^2 atan x =", sp.simplify(sp.diff(F1, x) - x**2*sp.atan(x)))
F2 = 3*sp.log(x + 2) + 7/(x + 2)
print("d/dx F2 - (3x-1)/(x+2)^2 =", sp.simplify(sp.diff(F2, x) - (3*x - 1)/(x + 2)**2))
print("sympy:", sp.integrate((3*x - 1)/(x + 2)**2, x))
