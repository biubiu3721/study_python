# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 5_13_to_5_14.py
Keywords :
Abstract  : The Fibonacci numbers are based on a recurrence relation.
            It is difficult to express this relation
            directly with NumPy code.
            However, we can express this relation
            in a matrix form or use the golden ratio formula.
            This will introduce the matrix and rint functions.
            The matrix function creates matrices
            and the rint function rounds numbers to
            the closest integer, but the result is not integer.
Author    : Focus
Date      : 8/21/2021 1:27 PM
"""


import numpy as np


"""
1. Computing.
"""
F = np.matrix([[1, 1], [1, 0]])
print("F: ", F)


"""
2. The eighth Fibonacci number(ignore 0)
"""
print("The 8th Fibonacci: ", (F ** 7)[0, 0])


"""
3. Binet's formula.
The golden ratio formula, 
better known as Binet's formula, 
allows us to calculate Fibonacci numbers 
with a rounding step at the end. 
Calculate the first eight Fibonacci numbers:
"""

n = np.arange(1, 9)
sqrt5 = np.sqrt(5)
phi = (1 + sqrt5) / 2
fibonacci = np.rint((phi ** n - (-1 / phi) ** n) / sqrt5)
print("Fibonacci: ", fibonacci)