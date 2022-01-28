# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 21_to_22.py
Author    : Focus
Date      : 8/22/2021 4:51 PM
Keywords  : np.random.normal
Abstract  :
Param     : 
Usage     : py 21_to_22.py
Reference :
[1]
matplotlib.pyplot.hist(
 x, bins=10, range=None, normed=False,
 weights=None, cumulative=False, bottom=None,
 histtype=u'bar', align=u'mid', orientation=u'vertical',
 rwidth=None, log=False, color=None, label=None, stacked=False,
 hold=None, **kwargs)
[2]
"""
import numpy as np
from matplotlib.pyplot import plot
import matplotlib.pyplot as plt # A is a file.
import sys


N = 10000
normal_values = np.random.normal(size=N) # Stand Normal Dist
print(int(np.sqrt(N)))
dummy, bins, dummy = plt.hist(normal_values, int(np.sqrt(N)), density=True, lw=1)

sigma = 1

mu = 0
coe = 1 / np.sqrt(sigma * 2 * np.pi)
exp_item = np.exp(- (bins - mu) ** 2 / 2 * sigma ** 2)
print(bins)
plt.plot(bins, coe * exp_item, lw=3)
#plt.plot(bins, coe * exp_item, lw=2)
plt.show()
