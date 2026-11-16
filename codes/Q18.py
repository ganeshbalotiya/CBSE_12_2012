#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q18: y = log(1+x) - 2x/(2+x) is increasing on x > -1
import numpy as np, sympy as sp
import matplotlib.pyplot as plt
x = sp.symbols('x', positive=True)
y = sp.log(1 + x) - 2*x/(2 + x)
print("y' =", sp.factor(sp.simplify(sp.diff(y, x))))
X = sp.symbols('X', real=True)
dy = sp.diff(sp.log(1 + X) - 2*X/(2 + X), X)
xs = np.linspace(-0.95, 6, 2000)
print("min of y' on grid:", np.min(sp.lambdify(X, dy, 'numpy')(xs)))
fig, ax = plt.subplots(figsize=(7, 4.5))
xp = np.linspace(-0.99, 6, 400)
ax.plot(xp, np.log(1 + xp) - 2*xp/(2 + xp), 'b-', label=r'$y=\ln(1+x)-\frac{2x}{2+x}$')
ax.axhline(0, color='gray', lw=0.8); ax.grid(True, ls='--', alpha=0.5)
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.legend()
plt.savefig('../figs/Q18.pdf', dpi=150)
#plt.show()
