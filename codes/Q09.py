#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q9: sin^-1(63/65) = sin^-1(5/13) + cos^-1(3/5)   and   2 atan(sin x) = atan(2 sec x)
import numpy as np, sympy as sp
lhs = np.arcsin(63/65)
rhs = np.arcsin(5/13) + np.arccos(3/5)
print("part 1:", lhs, rhs, np.isclose(lhs, rhs))
z = (12 + 5j)/13 * (3 + 4j)/5                       # rotation composition
print("(12+5j)(3+4j)/65 =", z*65/65, " |z| =", abs(z), " arg =", np.angle(z))
# OR part: scan for roots on (-pi/2, 3pi/2)
g = lambda x: 2*np.arctan(np.sin(x)) - np.arctan(2/np.cos(x))
xs = np.linspace(-np.pi/2 + 1e-3, 3*np.pi/2 - 1e-3, 400001)
vals = g(xs)
idx = np.where(np.diff(np.sign(vals)) != 0)[0]
cands = xs[idx]
cands = [c for c in cands if abs(np.cos(c)) > 1e-2]   # drop jumps at cos x = 0
print("roots (rad):", [round(c, 5) for c in cands], " pi/4 =", round(np.pi/4, 5), " 5pi/4 =", round(5*np.pi/4, 5))
