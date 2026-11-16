#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q13: 2 atan(sin x) = atan(2 sec x), x != pi/2  (roots at pi/4 and 5pi/4)
import numpy as np
import matplotlib.pyplot as plt
g = lambda x: 2*np.arctan(np.sin(x)) - np.arctan(2/np.cos(x))
xs = np.linspace(-np.pi/2 + 1e-3, 3*np.pi/2 - 1e-3, 400001)
vals = g(xs)
idx = np.where(np.diff(np.sign(vals)) != 0)[0]
cands = [c for c in xs[idx] if abs(np.cos(c)) > 1e-2]   # drop the jumps at cos x = 0
print("roots (rad):", [round(c, 5) for c in cands], " pi/4 =", round(np.pi/4, 5), " 5pi/4 =", round(5*np.pi/4, 5))
x = np.linspace(-np.pi/2, 3*np.pi/2, 4001)
with np.errstate(divide='ignore', invalid='ignore'):
    L = 2*np.arctan(np.sin(x))
    R = np.arctan(2/np.cos(x))
R[np.abs(np.cos(x)) < 1e-3] = np.nan                    # break the curve where sec x is undefined
plt.figure(figsize=(7, 4.5))
plt.plot(x, L, 'b-', label=r'$2\tan^{-1}(\sin x)$')
plt.plot(x, R, 'r--', label=r'$\tan^{-1}(2\sec x)$')
plt.plot([np.pi/4, 5*np.pi/4], [2*np.arctan(np.sin(np.pi/4)), 2*np.arctan(np.sin(5*np.pi/4))], 'ko')
plt.xticks([-np.pi/2, 0, np.pi/4, np.pi/2, np.pi, 5*np.pi/4, 3*np.pi/2],
           [r'$-\pi/2$', '0', r'$\pi/4$', r'$\pi/2$', r'$\pi$', r'$5\pi/4$', r'$3\pi/2$'])
plt.xlabel('x'); plt.ylabel('y'); plt.grid(True, ls='--', alpha=0.5); plt.legend()
plt.savefig('../figs/Q13.pdf', dpi=150)
#plt.show()
