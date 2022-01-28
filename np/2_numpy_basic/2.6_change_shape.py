"""
ravel vs flatten
ravel make a new obj, but a will be changed as long as a.ravel changed.
flatten also make a new obj, but will not influence ori array whatever change in a.flatten.
But Why ravel could change ori array?
"""
import numpy as np
a = np.arange(24).reshape(4,6)
b = a.copy()
c = a.ravel()
d = b.flatten()
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)
c[1] = 99
d[1] = 99
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)