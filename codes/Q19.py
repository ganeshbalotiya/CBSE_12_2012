#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q19: pair of dice thrown 4 times, success = doublet (p = 1/6)
import numpy as np
from math import comb
from fractions import Fraction
import matplotlib.pyplot as plt
p = Fraction(1, 6); q = 1 - p; n = 4
pmf = [comb(n, k)*p**k*q**(n - k) for k in range(n + 1)]
for k, v in enumerate(pmf):
    print("P(X=%d) = %s = %.5f" % (k, v, float(v)))
print("sum =", sum(pmf), " mean =", sum(k*v for k, v in enumerate(pmf)))
# Monte Carlo cross-check
rng = np.random.default_rng(0)
d = rng.integers(1, 7, size=(200000, 4, 2))
X = (d[:, :, 0] == d[:, :, 1]).sum(axis=1)
print("simulated mean =", X.mean(), " simulated pmf =", np.bincount(X)/len(X))
plt.figure(figsize=(6, 4))
plt.bar(range(n + 1), [float(v) for v in pmf], color='#a6d5ff', edgecolor='b')
plt.xlabel('number of doublets X'); plt.ylabel('P(X)'); plt.grid(True, ls='--', alpha=0.5)
plt.savefig('figs/Q19.png', dpi=150)
#plt.show()
