# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 33_34_sinc
Author    : Focus
Date      : 8/22/2021 11:56 PM
Keywords  : sinc
Abstract  : ret = sin(x) / x.
            It is equal to sin
Param     : x
Usage     : py 33_34_sinc
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys

x = np.linspace(-4, 4, 100)
vals = np.sinc(x)
plt.subplot(2,2,1)
plt.plot(x, vals)

xx = np.outer(x, x)
vals2 = np.sinc(xx)
plt.subplot(2,2,2)
plt.imshow(vals2)
plt.show()
