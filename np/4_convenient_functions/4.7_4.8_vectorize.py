#!/bin/python
# -*- UTF-8 -*-

import numpy as np
import sys
def calc_profit(open, high, low, close):
    print("I am here")
    buy = open * float(1)
    if low < buy < high:
        print("calc")
        return (close - buy) / buy
    else:
        return 0


o, h, l, c = np.loadtxt("BHP.csv", delimiter=',', usecols=(3,4,5,6), unpack=True)
print("t", len(o))
print("o", o)
print("h", h)
print("l", l)
print("c", c)
func = np.vectorize(calc_profit) # Cal this function many times.
profits = func(o, h, l, c)
print("Profits", profits)

real_trades = profits[profits != 0]
print("Number of trades", len(real_trades), round(100.0 * len(real_trades) / len(c), 2), "%")
print("Average profit / loss % ", round(np.mean(real_trades) * 100, 2))

