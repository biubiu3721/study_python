#！/bin/python
# -*- UTF-8 -*-


import numpy as np


a = np.eye(2)
print("a", a)
b = 2 * a
print("b", b)
print("compound matrix c: ", np.bmat("a, b; a, b"))

