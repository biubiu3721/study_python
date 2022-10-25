# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 15_to_16_fill_between
Author    : Focus
Date      : 8/24/2021 12:33 AM
Keywords  : fill_between
Abstract  :
Param     : 
Usage     : py 15_to_16_fill_between
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
fig = plt.figure()
dates = df.index
close = df["Close"]
ax = fig.add_subplot(111)
ax.plot(df.index, df["Close"])
plt.fill_between(dates, close.min(), close, where=close>close.mean(), facecolor="green", alpha=0.4)
plt.fill_between(dates, close.min(), close, where=close<close.mean(), facecolor="red", alpha=0.4)
plt.show()
