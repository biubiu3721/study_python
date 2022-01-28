#!/bin/python
# -*- UTF-8 -*-

import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
N = 8
weights = np.hanning(N)
print("weights", weights)
bhp = np.loadtxt("BHP.csv", delimiter=",", usecols=(6,), unpack=True)
print(bhp, len(bhp))
bhp_returns = np.diff(bhp) / bhp[: -1] # (x(i+1) - x(i) / x(i)
# convolve(weight, input)
smooth_bhp = np.convolve(weights / weights.sum(), bhp_returns)[N - 1: -N + 1]
vale = np.loadtxt("VALE.csv", delimiter=",", usecols=(6,), unpack=True)
vale_returns = np.diff(vale) / vale[: -1]
smooth_vale = np.convolve(weights, vale_returns)[N - 1: -N + 1]
t = np.arange(N - 1, len(bhp_returns))

plot(t, bhp_returns[N - 1: ], lw=1.0)
plot(t, smooth_bhp, lw=2.0)
plot(t, vale_returns[N - 1: ], lw=1.0)
plot(t, smooth_vale, lw=2.0)
show()

K = 3

t = np.arange(N - 1, len(bhp_returns))
poly_bhp = np.polyfit(t, smooth_bhp, K)
poly_vale = np.polyfit(t, smooth_vale, K)
poly_sub = np.polysub(poly_bhp, poly_vale)
x_points = np.roots(poly_sub)
print("Intersection points", x_points)
reals = np.isreal(x_points)
print("Real number?", reals)
print("x_points before select", x_points)
x_points = np.select([reals], [x_points])
print("x_points after select", x_points)
x_points= x_points.real
print("Real Intersection points", x_points)
print("San 0s", np.trim_zeros(x_points))