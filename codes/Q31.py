#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q31: integral_1^3 (x^2 + x) dx as a limit of a sum
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
n = sp.symbols('n', positive=True)
i = sp.symbols('i', positive=True, integer=True)
h = 2/n
S = sp.summation(h*((1 + i*h)**2 + (1 + i*h)), (i, 1, n))
print("S_n =", sp.simplify(S), "  limit =", sp.limit(S, n, sp.oo))
for N in [10, 100, 1000, 10000]:
    hh = 2/N; k = np.arange(1, N + 1); xk = 1 + k*hh
    print("n =", N, " right Riemann sum =", np.sum((xk**2 + xk)*hh))
print("38/3 =", 38/3)
N = 8; hh = 2/N; xk = 1 + np.arange(1, N + 1)*hh
print("n = 8 :", np.sum((xk**2 + xk)*hh), " = 38/3 + 10/8 + 4/(3*64) =", 38/3 + 10/8 + 4/(3*64))
x = np.linspace(1, 3, 200)
plt.figure(figsize=(6, 4))
plt.bar(xk - hh, xk**2 + xk, width=hh, align='edge', color='#a6d5ff', edgecolor='b')   # right-end rectangles
plt.plot(x, x**2 + x, 'r-', label=r'$f(x)=x^2+x$')
plt.xlabel('x'); plt.ylabel('f(x)'); plt.grid(True, ls='--', alpha=0.5); plt.legend()
plt.savefig('../figs/Q31.pdf', dpi=150)
#plt.show()
