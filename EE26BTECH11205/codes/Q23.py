#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q23: integral_1^3 (x^2 + x) dx as a limit of a sum ; OR integral_0^{pi/4} cos^2 x/(cos^2 x + 4 sin^2 x) dx
import numpy as np
import sympy as sp
from scipy.integrate import quad
n = sp.symbols('n', positive=True)
i = sp.symbols('i', positive=True, integer=True)
h = 2/n
S = sp.summation(h*((1 + i*h)**2 + (1 + i*h)), (i, 1, n))
print("S_n =", sp.simplify(S), "  limit =", sp.limit(S, n, sp.oo))
for N in [10, 100, 1000, 10000]:
    hh = 2/N; k = np.arange(1, N + 1); xk = 1 + k*hh
    print("n =", N, " right Riemann sum =", np.sum((xk**2 + xk)*hh))
print("38/3 =", 38/3)
# OR part
x = sp.symbols('x')
f = sp.cos(x)**2/(sp.cos(x)**2 + 4*sp.sin(x)**2)
print("exact:", sp.simplify(sp.integrate(f, (x, 0, sp.pi/4))))
cand = sp.Rational(2, 3)*sp.atan(2) - sp.pi/12
print("candidate (2/3)atan(2) - pi/12 =", sp.N(cand))
print("quad:", quad(lambda t: np.cos(t)**2/(np.cos(t)**2 + 4*np.sin(t)**2), 0, np.pi/4)[0])
