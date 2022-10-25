# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 3_approx_equal
Author    : Focus
Date      : 8/23/2021 12:40 AM
Keywords  : approximately
Abstract  : abs(actual - expected) > 10 ** -(significant - 1)
Param     : 
Usage     : py 3_approx_equal
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys

print("*** Case 1", "**")
print("Significance 8", np.testing.assert_approx_equal(0.123456789, 0.123456780, significant=8))
# >> Significance 8 None
print("*** Case 2", "**")
print("Significance 9", np.testing.assert_approx_equal(0.123456789, 0.123456780, significant=9))


