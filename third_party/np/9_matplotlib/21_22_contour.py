# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 21_22_contour
Author    : Focus
Date      : 8/24/2021 1:24 AM
Keywords  : Contour
Abstract  :
Param     : 
Usage     : py 21_22_contour
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import sys


fig = plt.figure()
ax = fig.add_subplot()
u = np.linspace(-1, 1, 100)
x, y = np.meshgrid(u, u)
z = x ** 2 + y ** 2
ax.contour(x, y, z)


plt.show()

