# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 5_6_subplot
Author    : Focus
Date      : 8/23/2021 1:40 PM
Keywords  : plt.subplot, plt.title
Abstract  :
Param     : 
Usage     : py 5_6_subplot
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys


func = np.poly1d(np.array([1, 2, 3, 4]))
x = np.linspace(-10, 10, 30)
y = func(x)
func1 = func.deriv(m=1)
func2 = func1.deriv(m=1)
y1 = func1(x)
y2 = func2(x)
plt.subplot(311)
plt.plot(x, y, "r-")
plt.title("Polynomial")
plt.subplot(312)
plt.plot(x, y1, "b^")
plt.title("First derivative")
plt.subplot(313)
plt.plot(x, y2, "go")
plt.title("Second Derivative")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
