#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q22: area in the first quadrant bounded by x-axis, x = sqrt(3) y, x^2 + y^2 = 4
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
x, y = sp.symbols('x y', positive=True)
s3 = sp.sqrt(3)
A = sp.integrate(x/s3, (x, 0, s3)) + sp.integrate(sp.sqrt(4 - x**2), (x, s3, 2))
print("area =", sp.simplify(A), "=", sp.N(A), " pi/3 =", sp.N(sp.pi/3))
# polar form: (1/2) int_0^{pi/6} 4 dtheta
th = sp.symbols('theta')
print("polar:", sp.integrate(sp.Rational(1, 2)*4, (th, 0, sp.pi/6)))
t = np.linspace(0, np.pi/6, 100)
fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(2*np.cos(np.linspace(0, np.pi/2, 200)), 2*np.sin(np.linspace(0, np.pi/2, 200)), 'b-', label=r'$x^2+y^2=4$')
xl = np.linspace(0, np.sqrt(3), 50); ax.plot(xl, xl/np.sqrt(3), 'r-', label=r'$x=\sqrt{3}y$')
ax.plot([0, 2], [0, 0], 'k-')
px = np.concatenate(([0], 2*np.cos(t))); py = np.concatenate(([0], 2*np.sin(t)))
ax.fill(px, py, color='#a6d5ff', alpha=0.8)
ax.plot(np.sqrt(3), 1, 'ko'); ax.annotate(r'$(\sqrt{3},1)$', (np.sqrt(3), 1), textcoords='offset points', xytext=(5, 8))
ax.set_aspect('equal'); ax.grid(True, ls='--', alpha=0.5); ax.legend()
plt.savefig('../figs/Q22.pdf', dpi=150)
#plt.show()
