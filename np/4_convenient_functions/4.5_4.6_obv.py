#!/bin/python
# -*- UTF-8 -*-
# 1. import
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
# 2. Prepare data
close, volume = np.loadtxt("BHP.csv", delimiter=',', usecols=(6, 7), unpack=True)
change = np.diff(close)
print("change", change)

signs = np.sign(change)
print("Signs", signs)
pieces = np.piecewise(change, [change < 0, change > 0], [-1, 1]) #Others Keep
print("Pieces", pieces)

print("Array Equal", np.array_equal(signs, pieces))
print("On balance Volume", volume[1:] * signs)