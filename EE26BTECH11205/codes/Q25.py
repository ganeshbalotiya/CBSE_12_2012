#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q25: min Z = 10x + 4y  s.t.  4x + y >= 80,  2x + y >= 60,  x, y >= 0
import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt
c = np.array([10, 4])
A = np.array([[-4, -1], [-2, -1]]); b = np.array([-80, -60])
res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None), (0, None)], method='highs')
print("x, y =", res.x, " Z_min =", res.fun)
for p in [(0, 80), (10, 40), (30, 0)]:
    print(p, "Z =", c @ np.array(p))
x = np.linspace(0, 40, 400)
fig, ax = plt.subplots(figsize=(7, 6))
ax.plot(x, 80 - 4*x, 'b-', label=r'$4x+y=80$')
ax.plot(x, 60 - 2*x, 'r-', label=r'$2x+y=60$')
upper = np.maximum(np.maximum(80 - 4*x, 60 - 2*x), 0)
ax.fill_between(x, upper, 100, color='#a6d5ff', alpha=0.6, label='feasible region')
ax.plot([0, 10, 30], [80, 40, 0], 'ko')
for (px, py) in [(0, 80), (10, 40), (30, 0)]:
    ax.annotate('(%d,%d)' % (px, py), (px, py), textcoords='offset points', xytext=(8, 6))
ax.plot(x, (260 - 10*x)/4, 'g--', label=r'$10x+4y=260$')
ax.set_xlim(0, 40); ax.set_ylim(0, 100); ax.set_xlabel('x (packets of S)'); ax.set_ylabel('y (packets of T)')
ax.grid(True, ls='--', alpha=0.5); ax.legend()
plt.savefig('figs/Q25.png', dpi=150)
#plt.show()
