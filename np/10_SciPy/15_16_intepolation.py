# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 15_16_intepolation
Author    : Focus
Date      : 8/25/2021 1:39 AM
Keywords  : intepolation,
Abstract  :
Param     : 
Usage     : py 15_16_intepolation
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import interpolate


x = np.linspace(-18, 18, 20)
noise = 0.1 * np.random.random(len(x))
signal = np.sinc(x) + noise
plt.plot(x, signal)
interpreted = interpolate.interp1d(x, signal)
x2 = np.linspace(-18, 18, 180)
y = interpreted(x2)
cubic = interpolate.interp1d(x, signal, kind="cubic")
y2 = cubic(x2)

plt.plot(x, signal, "o", label="data")
plt.plot(x2, y, "g-", label="linear")
plt.plot(x2, y2, "r-", lw=2, label="cubic")
plt.show()



