#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q12: y = e^(a acos x):  (1-x^2) y'' - x y' - a^2 y = 0     and OR part
import sympy as sp
x, a = sp.symbols('x a')
y = sp.exp(a*sp.acos(x))
print("ODE residual =", sp.simplify((1 - x**2)*sp.diff(y, x, 2) - x*sp.diff(y, x) - a**2*y))
# OR: x sqrt(1+y) + y sqrt(1+x) = 0, x != y   ->  y = -x/(1+x)
yy = -x/(1 + x)
res = x*sp.sqrt(1 + yy) + yy*sp.sqrt(1 + x)
print("residual at x = 0.3 :", sp.N(res.subs(x, 0.3)), "  x = -0.6 :", sp.N(res.subs(x, -0.6)))
print("dy/dx =", sp.simplify(sp.diff(yy, x)), "  = -1/(1+x)^2 :", sp.simplify(sp.diff(yy, x) + 1/(1 + x)**2) == 0)
