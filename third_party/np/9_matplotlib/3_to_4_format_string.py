# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 3_to_4_format_string
Author    : Focus
Date      : 8/23/2021 1:32 PM
Keywords  : func.deriv, 'ro', 'b-', 'g--'
Abstract  :
Param     : 
Usage     : py 3_to_4_format_string
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys


func = np.poly1d(np.array([1, 2, 3, 4]))
func1 = func.deriv(m=1)
x = np.linspace(-10, 10, 30)
y = func(x)
y1 = func1(x)
plt.plot(x, y, 'r*')
plt.plot(x, y1, 'g--')
plt.xlabel("x")
plt.ylabel("y")
plt.show()