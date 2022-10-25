# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 19_20_3D_plot
Author    : Focus
Date      : 8/24/2021 1:17 AM
Keywords  : Axes3D, meshgrid, plot_surface
Abstract  :
Param     : 
Usage     : py 19_20_3D_plot
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
from mpl_toolkits.mplot3d import Axes3D
from matplotlib  import cm

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
u = np.linspace(-1, 1, 100)
x, y = np.meshgrid(u, u)
print(x)
print(y)
z = x ** 2 + y ** 2
ax.plot_surface(x, y, z, rstride=4, cstride=4, cmap=cm.YlGnBu_r)
plt.show()