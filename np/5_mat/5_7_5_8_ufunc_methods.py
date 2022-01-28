#！/bin/python
# -*- UTF-8 -*-


"""
Ufuncs expect a set of scalars as input and produce a set of scalars as output.
Universal functions can typically be mapped to mathematical counterparts,
such as, add, subtract, divide, multiply, and likewise.
"""

import numpy as np


a = np.arange(9)
b = np.add.reduce(a)
c = np.add.accumulate(a)
#(indices(i), indices(i+1))] , if i = len - 1, then reduce(indices(i), -1)
d = np.add.reduceat(a, [0, 5, 2, 7])

print("a", a)
print("reduce: ", b)
print("accumu: ", c)
print("reduceat: ", d)
print("Reduceat step I", np.add.reduce(a[0:5]))
print("Reduceat step II", np.add.reduce(a[5]))
print("Reduceat step III", np.add.reduce(a[2:7]))
print("Reduceat step IV", np.add.reduce(a[7:]))
print("Outer", np.add.outer(np.arange(5), a))

