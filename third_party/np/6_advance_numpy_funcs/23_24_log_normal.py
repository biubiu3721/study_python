# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 23_24_log_normal.py
Author    : Focus
Date      : 8/22/2021 9:43 PM
Keywords  : np.random.lognormal
Abstract  :
Param     : 
Usage     : py 23_24_log_normal.py
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt


N = 10000
lognormal_values = np.random.lognormal(size=N)
dummy, bins, dummy = plt.hist(lognormal_values, int(np.sqrt(N)), density=True, lw=1)
sigma = 1
mu = 0
x = np.linspace(min(bins), max(bins), len(bins))
pdf = np.exp(-(np.log(x) - mu) ** 2 / (2 * sigma ** 2))
pdf = pdf / (x * sigma * np.sqrt(2 * np.pi))
plt.plot(x, pdf, lw=3)
plt.show()
