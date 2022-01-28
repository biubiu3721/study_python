# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 13_to_14_string_equal
Author    : Focus
Date      : 8/23/2021 9:19 AM
Keywords  : 
Abstract  :
Param     : 
Usage     : py 13_to_14_string_equal
Reference :
"""
import numpy as np
# import matplotlib.pyplot as plt
# import sys


print("Pass Case: ")
print(np.testing.assert_string_equal("NumPy", "NumPy"))
print("Fail Case:")
print(np.testing.assert_string_equal("Numpy", "numpy"))

#>> Traceback (most recent call last):
#  File "C:\work\code\python\numpy\8_assure_quality_with_testing\13_to_14_string_equal.py", line 21, in <module>
#     print(np.testing.assert_string_equal("Numpy", "numpy"))
#   File "C:\work\code\python\numpy\venv\lib\site-packages\numpy\testing\_private\utils.py", line 1206, in assert_string_equal
#     raise AssertionError(msg)
#  AssertionError: Differences in strings:
#  - Numpy? ^
#  + numpy? ^

