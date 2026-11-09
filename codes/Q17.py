#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q17: beta = beta1 + beta2,  beta1 || alpha,  beta2 _|_ alpha
import numpy as np
from fractions import Fraction
al = np.array([[3], [4], [5]], dtype=float)
be = np.array([[2], [1], [-4]], dtype=float)
P = al @ al.T/(al.T @ al)             # projection matrix onto span{alpha}
b1 = P @ be
b2 = be - b1
print("beta1 =", b1.ravel(), [str(Fraction(v).limit_denominator(10)) for v in b1.ravel()])
print("beta2 =", b2.ravel(), [str(Fraction(v).limit_denominator(10)) for v in b2.ravel()])
print("alpha.beta2 =", (al.T @ b2).item(), " beta1+beta2 = beta :", np.allclose(b1 + b2, be))
