#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q23: 3 e^x tan y dx + (2 - e^x) sec^2 y dy = 0 , y(0) = pi/4
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
# dy/dx = -3 e^x tan y / ((2 - e^x) sec^2 y), valid for 2 - e^x > 0 (x < ln 2)
f = lambda x, y: -3*np.exp(x)*np.tan(y)/((2 - np.exp(x))/np.cos(y)**2)
fw = solve_ivp(f, [0, 0.6], [np.pi/4], rtol=1e-11, atol=1e-13, dense_output=True)
bw = solve_ivp(f, [0, -1.0], [np.pi/4], rtol=1e-11, atol=1e-13, dense_output=True)
xs = np.linspace(0, 0.6, 7)
exact = np.arctan((2 - np.exp(xs))**3)
print("max |numerical - exact| =", np.max(np.abs(fw.sol(xs)[0] - exact)))
x = np.linspace(-1.0, 0.65, 400)
plt.figure(figsize=(6, 4))
plt.plot(x, np.arctan((2 - np.exp(x))**3), 'b-', label=r'$y=\tan^{-1}(2-e^x)^3$')
xn = np.concatenate((np.linspace(-1.0, -0.05, 6), np.linspace(0.05, 0.6, 6)))
yn = np.array([bw.sol(v)[0] if v < 0 else fw.sol(v)[0] for v in xn])
plt.plot(xn, yn, 'r.', label='numerical solution')
plt.plot(0, np.pi/4, 'ko'); plt.annotate(r'$(0,\pi/4)$', (0, np.pi/4), textcoords='offset points', xytext=(6, 6))
plt.xlabel('x'); plt.ylabel('y'); plt.grid(True, ls='--', alpha=0.5); plt.legend()
plt.savefig('../figs/Q23.pdf', dpi=150)
#plt.show()
