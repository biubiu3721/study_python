# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 9_10_assert_array_less
Author    : Focus
Date      : 8/23/2021 9:09 AM
Keywords  : assert_array_less
Abstract  :
Param     : 
Usage     : py 9_10_assert_array_less
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys


l0 = [0, 0.123456789, np.nan]
l1 = [1, 0.234567890, np.nan]
print("Pass: ")
print(np.testing.assert_array_less(l0, l1))


l0 = [0, 0.123456789, np.nan]
l1 = [0, 0.123456780, np.nan]
print("Fail: ")
print(np.testing.assert_array_less(l0, l1))


