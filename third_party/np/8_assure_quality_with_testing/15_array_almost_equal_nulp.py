# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 15_array_almost_equal_nulp
Author    : Focus
Date      : 8/23/2021 9:26 AM
Keywords  : assert_array_almost_equal_nulp, IEEE 754, finfo, machine epsilon
Abstract  :
            Assert:
                 abs(x - y) <= nulps * spacing(maximum(abs(x), abs(y)))
            float point is not actual in computer.
             >>> x = np.array([1., 1e-10, 1e-20])
             >>> eps = np.finfo(x.dtype).eps
             >>> np.testing.assert_array_almost_equal_nulp(x, x*eps/2 + x)
             >>> np.testing.assert_array_almost_equal_nulp(x, x*eps + x)
            Traceback (most recent call last):
            AssertionError: X and Y are not equal to 1 ULP (max is 2)
Param     : 
Usage     : py 15_array_almost_equal_nulp
Reference :
"""
import numpy as np
# import matplotlib.pyplot as plt
# import sys


eps = np.finfo(float).eps
print("EPS", eps)
print("Case1: ")
print(np.testing.assert_array_almost_equal_nulp(1.0, 1.0 + eps))
print("Case2: ")
print(np.testing.assert_array_almost_equal_nulp(1.0, 1.0 + 2 * eps))



