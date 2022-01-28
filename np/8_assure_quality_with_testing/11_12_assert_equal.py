# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 11_12_assert_equal
Author    : Focus
Date      : 8/23/2021 9:17 AM
Keywords  : assert_equal,
Abstract  : support numpy, list, tuple, dict
Param     : 
Usage     : py 11_12_assert_equal
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys


a = (1, 2)
b = (1, 3)
print("Equal: ?")
print(np.testing.assert_equal(a, b))
