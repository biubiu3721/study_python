# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 17_18_ulp
Author    : Focus
Date      : 8/23/2021 9:33 AM
Keywords  : assert_array_max_ulp, ULP, unit of least precision
Abstract  : 
Param     : 
Usage     : py 17_18_ulp
Reference :
"""
import numpy as np
# import matplotlib.pyplot as plt
# import sys


#help(np.testing.assert_array_max_ulp)

eps = np.finfo(float).eps
print("EPS", eps)
print("Case1")
print(np.testing.assert_array_max_ulp(1.0, 1.0 + eps))
print("Case2")
print(np.testing.assert_array_max_ulp(1.0, 1 + 2 * eps, maxulp=2))
