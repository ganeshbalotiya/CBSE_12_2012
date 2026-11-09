#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q15: [e^(-2 sqrt x)/sqrt x - y/sqrt x] dx/dy = 1 , x > 0
import sympy as sp
x, C = sp.symbols('x C', positive=True)
y = sp.Function('y')
ode = sp.Eq(y(x).diff(x), sp.exp(-2*sp.sqrt(x))/sp.sqrt(x) - y(x)/sp.sqrt(x))
print("sympy:", sp.dsolve(ode))
ys = (2*sp.sqrt(x) + C)*sp.exp(-2*sp.sqrt(x))
print("residual of y = (2 sqrt x + C) e^(-2 sqrt x):",
      sp.simplify(sp.diff(ys, x) - (sp.exp(-2*sp.sqrt(x))/sp.sqrt(x) - ys/sp.sqrt(x))))
