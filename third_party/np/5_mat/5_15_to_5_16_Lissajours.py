# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 5_15_to_5_16_Lissajours
Keywords  : Lissajours curve, sin, cos, tan
Abstract  : 
Author    : Focus
Date      : 8/21/2021 2:18 PM
"""


import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
t = np.linspace(-np.pi, np.pi, 201)
x = np.sin(a * t + np.pi / 2.0)
y = np.sin(b * t)
plot(x, y)
show()

