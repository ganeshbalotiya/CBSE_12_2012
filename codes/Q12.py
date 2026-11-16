#Code by EE26BTECH11205
#CBSE 2012 Mathematics (65/2/1)
#Q12: sin^-1(63/65) = sin^-1(5/13) + cos^-1(3/5)
import numpy as np
lhs = np.arcsin(63/65)
rhs = np.arcsin(5/13) + np.arccos(3/5)
print("sin^-1(63/65) =", lhs, " sin^-1(5/13) + cos^-1(3/5) =", rhs, np.isclose(lhs, rhs))
z = (12 + 5j)/13 * (3 + 4j)/5                       # product of the two unit complex numbers
print("(12+5j)(3+4j)/65 =", z, " (16+63j)/65 =", (16 + 63j)/65)
print("|z| =", abs(z), " arg z =", np.angle(z), " sin^-1(63/65) =", lhs)
