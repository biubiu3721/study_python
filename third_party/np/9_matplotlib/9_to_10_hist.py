# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 9_to_10_hist
Author    : Focus
Date      : 8/23/2021 10:21 PM
Keywords  : plt.hist
Abstract  :
Param     : 
Usage     : py 9_to_10_hist
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
import mplfinance as mpf
import pandas_datareader.data as web
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt

today = date.today()
start = (today.year - 1, today.month, today.day)
df = web.DataReader('DISH', 'yahoo', start='2012-12-01', end='2013-12-01')
close = df["Close"]
print(df.head())
print(df["Close"])
print(np.min(close), np.max(close))
plt.hist(close, int(np.sqrt(len(close))))
plt.show()