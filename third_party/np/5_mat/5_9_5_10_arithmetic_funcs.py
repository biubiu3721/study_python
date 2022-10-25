#！/bin/python
# -*- UTF-8 -*-


"""
How can functions have methods? As we said earlier,
universal functions are not functions
but objects representing functions.
Universal functions have four methods.
They only make sense for functions such as add.
That is, they have two input parameters and return one output parameter.
If the signature of an ufunc does not match this condition,
this will result in a ValueError,
so call this method only for binary universal functions.
The four methods are listed as follows:
 @ reduce
 @ accumulate
 @ reduceat
 @ outer
"""
from __future__ import division
import numpy as np

"""
1. divide
"""
a = np.array([2, 6, 5]) # default dtype is int32
b = np.array([1, 2, 3])
print(a.dtype)
# default divide type is normal floating-point division,
# no matter what dtype is.
print("Divide", np.divide(a, b), np.divide(b, a))

"""
2. true divide
The true_divide function comes closer to 
the mathematical definition of division. 
Integer division returns a floating-point
result and no truncation occurs:
"""

print("True divide: ", np.true_divide(a, b), np.true_divide(b, a))


"""
3. floor_divide
The floor_divide function always 
returns an integer result. 
It is equivalent to calling the floor function 
after calling the divide function. 
The floor function discards the decimal part
of a floating-point number 
and returns an integer:
"""

print("Floor divide: ", np.floor_divide(a, b), np.floor_divide(b, a))
c = 3.14 * b
print("Floor divide 2:", np.floor_divide(c, b), np.floor_divide(b, c))

"""
4. '/' 
By default, the / operator is equivalent to 
calling the divide function: 
"""

print("/ operator: ", a / b, b / a)

"""
5. //
The '//' operator is equivalent to 
calling the floor_divide function. 
For example, look at the following code snippet:
"""

print("// operator: ", a // b, b // a)
print("// operator: ", c // b, b // c)

