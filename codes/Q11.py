#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q11: x^m y^n = (x+y)^(m+n)  =>  dy/dx = y/x
import numpy as np
import sympy as sp
from scipy.optimize import brentq

x, y, m, n = sp.symbols('x y m n')
# ln|u| has derivative 1/u, so the same algebra works for every sign of x, y, x+y
F = m*sp.log(x) + n*sp.log(y) - (m + n)*sp.log(x + y)
dydx = sp.simplify(-sp.diff(F, x)/sp.diff(F, y))          # implicit differentiation
print("dy/dx =", sp.factor(dydx))
print("dy/dx - y/x =", sp.simplify(dydx - y/x))

# Numerical check with m = 2, n = 3: put y = t x, so t^3 = (1+t)^5
f = lambda t: t**3 - (1 + t)**5
t0 = brentq(f, -3.0, -2.0)
print("root t =", t0, " residual =", f(t0))
for x0 in [0.5, 1.0, 2.0]:
    y0 = t0*x0
    print("x =", x0, " y =", y0, " relation:", np.isclose(x0**2*y0**3, (x0 + y0)**5),
          " dy/dx = t =", t0, " y/x =", y0/x0)
