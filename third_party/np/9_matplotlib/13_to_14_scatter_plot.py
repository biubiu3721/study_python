# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 13_to_14_scatter_plot
Author    : Focus
Date      : 8/24/2021 12:20 AM
Keywords  : 
Abstract  :
Param     : 
Usage     : py 13_to_14_scatter_plot
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

today = date.today()
print(today)
start = date(today.year - 1, today.month, today.day)
symbol = "DISH"
df = pdr.data.get_data_yahoo("DISH", start="2012-12-01", end="2013-12-01")
print(df.head())
close = df["Close"]
volume = df["Volume"]
print("dates", close)
print("volume", volume)
ret = np.diff(close) / close[:-1] # (ai - ai+1) / ai
volchange = np.diff(volume) / volume[-1]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(ret, volchange, c = ret * 100, s=volchange * 100, alpha = 0.5)
ax.set_title("Close and volume returns")
ax.grid(True)
plt.show()

