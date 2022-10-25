#!/usr/bin/env/python3
"""
    Desciption:
	    This is in chapter 1. 
	    This code shows the vector add in python. 
	    Using the commands below to run this program.
	    python3 vectorsum.py n
	args:
	    n is size of the vector.
"""


import sys
from datetime import datetime
import numpy as np

def python_sum(n):
	a = list(range(n)) # range in pthon2.x return a list,
	b = list(range(n)) # range in python3.x return a range obj.
	c = []
	for i in range(n):
		a[i] = i ** 2
		b[i] = i ** 3
		c.append(a[i] + b[i])
	return c
def numpy_sum(n):
	a = np.arange(n, dtype=np.int64) ** 2
	b = np.arange(n, dtype=np.int64) ** 3
	c = a + b
	return c

size = int(sys.argv[1])
start = datetime.now()
c = python_sum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum: ", c[-2:])
print("PythonSum elapsed time in microseconds", delta.microseconds)
start = datetime.now()
c = numpy_sum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum: ", c[-2:])
print("NumpySum elapsed time in microseconds", delta.microseconds)



"""
C:\software\python\python.exe C:/Users/yuyan01/Desktop/numpy/1_tutorial/1_12_vector_add.py 1000
The last 2 elements of the sum:  [995007996, 998001000]
PythonSum elapsed time in microseconds 997
The last 2 elements of the sum:  [995007996 998001000]
NumpySum elapsed time in microseconds 0

C:\software\python\python.exe C:/Users/yuyan01/Desktop/numpy/1_tutorial/1_12_vector_add.py 2000
The last 2 elements of the sum:  [7980015996, 7992002000]
PythonSum elapsed time in microseconds 1994
The last 2 elements of the sum:  [-609918596 -597932592]
NumpySum elapsed time in microseconds 0

C:\software\python\python.exe C:/Users/yuyan01/Desktop/numpy/1_tutorial/1_12_vector_add.py 3000
The last 2 elements of the sum:  [26955023996, 26982003000]
PythonSum elapsed time in microseconds 2037
The last 2 elements of the sum:  [26955023996 26982003000]
NumpySum elapsed time in microseconds 0

"""