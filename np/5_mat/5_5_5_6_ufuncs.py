#！/bin/python
# -*- UTF-8 -*-


"""
Ufuncs expect a set of scalars as input and produce a set of scalars as output.
Universal functions can typically be mapped to mathematical counterparts,
such as, add, subtract, divide, multiply, and likewise.
"""


import numpy as np


def ultimate_answer(a):
    result = np.zeros_like(a)
    print("result", result)
    result.flat = 42
    print("result", result)
    return result

"""
Create a universal function with frompyfunc; 
specify 1 as as number of input parameter 
followed by 1 as the number of output parameters
args: 
     function obj
     in_param num
     out param num
"""
ufunc = np.frompyfunc(ultimate_answer, 1, 1) #TODO Figure out why is is vectorized.
a = np.array(np.arange(4).reshape(2, 2))
print("The answer: ", ufunc(a))
