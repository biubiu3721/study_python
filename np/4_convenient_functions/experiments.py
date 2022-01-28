#!/bin/python
# -*- UTF-8 -*-
# 1. import
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
# 2. Prepare data
bhp = np.loadtxt("BHP.csv", delimiter=',', usecols=(6, ), unpack=True)
vale = np.loadtxt("vale.csv", delimiter=',', usecols=(6, ), unpack=True)
# 2. Covariance & coefficient
bhp_returns = np.diff(bhp) / bhp[: -1] #(x1-x0) / x0.
vale_returns = np.diff(vale) / vale[: -1]
covariance = np.cov(bhp_returns, vale_returns)
print("cov matrix", covariance)
print("cov matrix diagonal: ", covariance.diagonal())
print("cov matrix trace: ", covariance.trace())
print("corr matrix", covariance / (bhp_returns.std(ddof=1) * vale_returns.std(ddof=1)))
print("corr matrix", np.corrcoef(bhp_returns, vale_returns))
# Sync
avg_diff = np.mean(bhp - vale)
dev = np.std(bhp - vale)
print("Sync: ", np.abs(bhp[-1] - vale[1] - avg_diff) > 2 * dev)
# plot
t = np.arange(len(bhp_returns))
# show
#plot(t, bhp_returns, lw=1)
#plot(t, vale_returns, lw=2)
#show()
# 4.3 4.4 Polyfit
t = np.arange(len(bhp))
poly_diff = np.polyfit(t, bhp - vale, 3)
print("Polynomial fit", poly_diff)
print("Next value", np.polyval(poly_diff, t[-1] + 1))
# roots
print("Roots", np.roots(poly_diff))
# der
der = np.polyder(poly_diff)
print("Derivative", der)
# der roots
print("Extremas", np.roots(der))
# check
vals = np.polyval(poly_diff, t)
print("max point", np.argmax(vals))
print("min point", np.argmin(vals))

# show
#plot(t, bhp - vale)
#plot(t, vals)
#how()


#
