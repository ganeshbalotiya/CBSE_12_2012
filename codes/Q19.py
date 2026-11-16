#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q19: normal to a y^2 = x^3 at (a m^2, a m^3)   (plot for a = 1, m = 1)
import numpy as np, sympy as sp
import matplotlib.pyplot as plt
x, a, m = sp.symbols('x a m', positive=True)
Y = sp.symbols('Y')
Yb = sp.sqrt(x**3/a)                      # branch of a y^2 = x^3 through (a m^2, a m^3) for m > 0
slope = sp.simplify(sp.diff(Yb, x).subs(x, a*m**2))
print("tangent slope at (am^2, am^3) =", slope)
normal = sp.Eq(2*x + 3*m*Y, a*m**2*(2 + 3*m**2))
print("normal:", normal, "; point on it:", sp.simplify(normal.lhs.subs({x: a*m**2, Y: a*m**3}) - normal.rhs) == 0)
av, mv = 1.0, 1.0
t = np.linspace(-1.6, 1.6, 400)
px, py = t**2/av**0, t**3                      # a y^2 = x^3 with a = 1 :  x = t^2, y = t^3
P = (av*mv**2, av*mv**3)
xl = np.linspace(-0.3, 2.6, 100)
fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(px, py, 'b-', label=r'$ay^2=x^3$')
ax.plot(xl, P[1] + 1.5*mv*(xl - P[0]), 'g--', label='tangent')
ax.plot(xl, (av*mv**2*(2 + 3*mv**2) - 2*xl)/(3*mv), 'r-', label='normal')
ax.plot(*P, 'ko'); ax.annotate(r'$(am^2,am^3)$', P, textcoords='offset points', xytext=(6, -14))
ax.set_xlim(-0.3, 2.6); ax.set_ylim(-1.5, 3.2); ax.set_aspect('equal'); ax.grid(True, ls='--', alpha=0.5); ax.legend()
plt.savefig('../figs/Q19.pdf', dpi=150)
#plt.show()
