# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 17_to_18_legend_annotate
Author    : Focus
Date      : 8/24/2021 12:42 AM
Keywords  : legend, annotate
Abstract  :
Param     : 
Usage     : py 17_to_18_legend_annotate
Reference :
"""
import pandas_datareader as pdr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
import mplfinance as plf
from  datetime import date
import sys


symbol = "DISH"
df = pdr.data.get_data_yahoo("DISH", start="2012-12-01", end="2013-12-01")
dates = np.array(df.index)
close = df["Close"]
fig = plt.figure()
ax = fig.add_subplot(111)
emas = [] # move average shift
for i in range(9, 19, 3):
    weights = np.exp(np.linspace(-1.0, 0.0, i))
    weights = weights / weights.sum()
    ema = np.convolve(weights, close)[i-1: -i+1]
    idx = (i - 6) / 3
    ax.plot(dates[i-1:], ema, lw=idx, label="EMA(%s)" % (i))
    data = np.column_stack((dates[i-1:].astype(np.float32), ema))
    emas.append(np.rec.fromrecords( data, names=["dates", "ema"]))
print("Second 2")
first = emas[0]["ema"].flatten()
second = emas[1]["ema"].flatten()
bools = np.abs(first[-len(second):] - second) / second < 0.0001
xpoints = np.compress(bools, emas[1])

for xpoint in xpoints:
    ax.annotate("x", xy=xpoint, textcoords="offset points",
                xytext=(-50, 30), arrowprops=dict(arrowstyle="->"))
print("Section 3")
leg = ax.legend(loc="best", fancybox=True)
leg.get_frame().set_alpha(0.5)
alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")
ax.plot(dates, close, lw=1.0, label="Close")
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(month_formatter)
ax.grid(True)
fig.autofmt_xdate()
plt.show()