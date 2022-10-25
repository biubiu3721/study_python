# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 7_8_signal
Author    : Focus
Date      : 8/24/2021 11:06 PM
Keywords  : scipy.signal, B-spline interpolation
Abstract  :
Param     : 
Usage     : py 7_8_signal
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import signal
import pandas_datareader.data as pdd

qqq_df = pdd.DataReader("QQQ", "yahoo", "2020-01-01", "2021-01-01")
qqq_date = qqq_df.index
qqq_close = qqq_df["Close"]
y = signal.detrend(qqq_close)
plt.plot(qqq_date, y, lw=1)
plt.show()