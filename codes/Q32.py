#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q32: integral_0^{pi/4} cos^2 x/(cos^2 x + 4 sin^2 x) dx
import numpy as np
import sympy as sp
from scipy.integrate import quad
x = sp.symbols('x')
f = sp.cos(x)**2/(sp.cos(x)**2 + 4*sp.sin(x)**2)
print("exact:", sp.simplify(sp.integrate(f, (x, 0, sp.pi/4))))
cand = sp.Rational(2, 3)*sp.atan(2) - sp.pi/12
print("candidate (2/3)atan(2) - pi/12 =", sp.N(cand))
print("quad:", quad(lambda t: np.cos(t)**2/(np.cos(t)**2 + 4*np.sin(t)**2), 0, np.pi/4)[0])
