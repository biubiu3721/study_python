# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 2_almost_equal
Author    : Focus
Date      : 8/23/2021 12:32 AM
Keywords  : assert_almost_equal
Abstract  : np.testing.assert_almost_equal
Param     : (a, b, decimal=7)
Usage     : py 2_almost_equal
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys

print("Decimal 7", np.testing.assert_almost_equal(0.123456789, 0.123456780, decimal=8))
# >> Decimal 6 None
print("Decimal 8", np.testing.assert_almost_equal(0.123456789, 0.123456780, decimal=9))
# AssertionError:
# Arrays are not almost equal to 9 decimals
#  ACTUAL: 0.123456789
#  DESIRED: 0.12345678