#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q16: y = e^(a acos x):  (1-x^2) y'' - x y' - a^2 y = 0
import sympy as sp
x, a = sp.symbols('x a')
y = sp.exp(a*sp.acos(x))
print("ODE residual =", sp.simplify((1 - x**2)*sp.diff(y, x, 2) - x*sp.diff(y, x) - a**2*y))
