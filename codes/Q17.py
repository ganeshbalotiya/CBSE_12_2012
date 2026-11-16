#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q17: x sqrt(1+y) + y sqrt(1+x) = 0, x != y   ->  y = -x/(1+x),  dy/dx = -1/(1+x)^2
import sympy as sp
x = sp.symbols('x')
yy = -x/(1 + x)
res = x*sp.sqrt(1 + yy) + yy*sp.sqrt(1 + x)
print("residual at x = 0.3 :", sp.N(res.subs(x, 0.3)), "  x = -0.6 :", sp.N(res.subs(x, -0.6)))
print("dy/dx =", sp.simplify(sp.diff(yy, x)), "  = -1/(1+x)^2 :", sp.simplify(sp.diff(yy, x) + 1/(1 + x)**2) == 0)
