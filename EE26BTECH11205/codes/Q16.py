#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q16: 3 e^x tan y dx + (2 - e^x) sec^2 y dy = 0 , y(0) = pi/4
import numpy as np
from scipy.integrate import solve_ivp
# dy/dx = -3 e^x tan y / ((2 - e^x) sec^2 y), solved on [0, 0.6] (2 - e^x > 0)
f = lambda x, y: -3*np.exp(x)*np.tan(y)/((2 - np.exp(x))/np.cos(y)**2)
sol = solve_ivp(f, [0, 0.6], [np.pi/4], rtol=1e-11, atol=1e-13, dense_output=True)
xs = np.linspace(0, 0.6, 7)
exact = np.arctan((2 - np.exp(xs))**3)
print("max |numerical - exact| =", np.max(np.abs(sol.sol(xs)[0] - exact)))
