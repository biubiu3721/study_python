# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 32_to_32_bessel function
Author    : Focus
Date      : 8/22/2021 11:50 PM
Keywords  : 
Abstract  :
Param     : 
Usage     : py 32_to_32_bessel function
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys


x = np.linspace(0, 4, 100)
vals = np.i0(x)
plt.plot(x, vals)
plt.show()