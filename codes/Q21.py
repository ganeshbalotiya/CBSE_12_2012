#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q21: maximum-volume right circular cone inscribed in a sphere of radius R has height 4R/3
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
h, R = sp.symbols('h R', positive=True)
V = sp.pi/3*h*(h*(2*R - h))                 # r^2 = h(2R - h)
crit = sp.solve(sp.diff(V, h), h)
print("critical points:", crit)
hc = 4*R/3
print("V'' at h = 4R/3 :", sp.simplify(sp.diff(V, h, 2).subs(h, hc)), "(< 0, maximum)")
print("Vmax =", sp.simplify(V.subs(h, hc)), " ; 32/81 of sphere volume:", sp.simplify(V.subs(h, hc)/(sp.Rational(4, 3)*sp.pi*R**3)))
Rv = 1.0
hs = np.linspace(0, 2*Rv, 400)
Vs = np.pi/3*hs**2*(2*Rv - hs)
print("grid argmax h =", hs[np.argmax(Vs)], " 4/3 =", 4/3)
plt.figure(figsize=(6, 4))
plt.plot(hs, Vs, 'b-'); plt.axvline(4/3, color='r', ls='--', label='h = 4R/3')
plt.xlabel('h (R = 1)'); plt.ylabel('V'); plt.grid(True, ls='--', alpha=0.5); plt.legend()
plt.savefig('../figs/Q21.pdf', dpi=150)
#plt.show()
