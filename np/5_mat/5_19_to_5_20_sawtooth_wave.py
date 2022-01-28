# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 5_19_to_5_20
Author    : Focus
Date      : 8/21/2021 3:13 PM
Keywords  :  
Abstract  :
Param     : 
Usage     : py 5_19_to_5_20
Reference :
"""
import sys
import numpy as np
from matplotlib.pyplot import show
from matplotlib.pyplot import plot


t = np.linspace(-np.pi, np.pi, 201)
k = np.arange(1, float(sys.argv[1]))
f = np.zeros_like(t)

"""
Generate sawtooth wave.
"""
for i in range(len(t)):
    f[i] = np.sum(np.sin(2 * np.pi * k * t[i]) / k) * (-2 / np.pi)

plot(t, f, lw=1.0)

"""
Generate triangle wave.
"""
for i in range(len(t)):
    f[i] = np.sum(np.sin(2 * np.pi * k * t[i]) / k)
    f[i] = np.abs(f[i] * (-2 / np.pi))


plot(t, f, lw=2.0)
show()