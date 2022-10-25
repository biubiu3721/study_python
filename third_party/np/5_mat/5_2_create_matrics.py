#！/bin/python
# -*- UTF-8 -*-

"""
Matrics is conveyed through np.mat, a subclass of numpy.

"""
import numpy as np


a = np.mat("1.0, 1.0, 2; 1, 1, 3; 1.1, 1, 4")
print("Create from a string")
print(a)
print("Transpose a", a.T)
# 3. Inverse
# |a| = 0 -> sigular, else Non Sigular
# a.I = a.company / a
print("determin is: ", np.linalg.det(a))
print("Inverse a is :", a.I)

# 4. Create from array.
a = np.mat(np.arange(9).reshape(3, 3))
print("Create from np array ", a)