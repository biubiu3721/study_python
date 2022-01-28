# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 5_to_6_array_approx_equal
Author    : Focus
Date      : 8/23/2021 12:48 AM
Keywords  : assert_array_almost_equal
Abstract  : |expected - actual| < 0.5 * 10 ** (-decimal)
Param     : (expected, actual, decimal)
Usage     : py 5_to_6_array_approx_equal
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys


print("Decimal 8: ")
print(np.testing.assert_array_almost_equal([0, 0.123456789], [0, 0.123456780], decimal=8))
print("Decimal 9")
print(np.testing.assert_array_almost_equal([0, 0.123456789], [0, 0.123456780], decimal=9))
