# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 5_17_to_5_18
Keywords  : Squarewave
Abstract  : f(i) = Sum( 4 * sin( (2k-1) * t(i) ) / ( ( 2k - 1) * PI ), k, 1, +inf)
Author    : Focus
Date      : 8/21/2021 2:47 PM
Param     : k
Example   : py 5_17_to_5_18 99
Reference :
"""


import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import sys


t = np.linspace(-np.pi, np.pi, 201)
k = np.arange(1, float(sys.argv[1]))
k = 2 * k - 1 # vector
f = np.zeros_like(t)

for i in range(len(t)):
    f[i] = np.sum(np.sin(k * t[i]) / k) * (4.0 / np.pi)

plot(t, f)
show()