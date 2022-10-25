# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 7_to_8_all_close
Author    : Focus
Date      : 8/23/2021 9:02 AM
Keywords  : assert_allclose, assert_array_equal,
Abstract  : |a - b| <= (atol + rtol * |b|)
Param     : 
Usage     : py 7_to_8_all_close
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys

l0 = [0, 0.123456789, np.nan]
l1 = [0, 0.123456780, np.nan]
print("Pass", np.testing.assert_allclose(l0, l1, rtol=1e-7, atol=0))
print("Fail", np.testing.assert_array_equal(l0, l1))



