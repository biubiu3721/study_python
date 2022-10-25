# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 2_plot_polynomial
Author    : Focus
Date      : 8/23/2021 1:27 PM
Keywords  : polynomial, plot, xlabel(), show()
Abstract  :
Param     : 
Usage     : py 2_plot_polynomial
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys

func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
x = np.linspace(-10, 10, 10)
y = func(x)
plt.plot(x, y, lw=1)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
