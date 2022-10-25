# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 11_to_12_optimization
Author    : Focus
Date      : 8/24/2021 11:34 PM
Keywords  : residual, optimization, scipy.optimization, leastsq
Abstract  :
Param     : 
Usage     : py 11_to_12_optimization
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import fftpack



from scipy import signal
import pandas_datareader.data as pdd
qqq_df = pdd.DataReader("QQQ", "yahoo", "2020-01-01", "2021-01-01")
qqq_dates = qqq_df.index
qqq_close = qqq_df["Close"]
y = signal.detrend(qqq_close)
amps = np.abs(fftpack.fftshift(fftpack.rfft(y)))
filtered = -fftpack.irfft(fftpack.ifftshift(amps))



from scipy import optimize
plsq = optimize.leastsq(residual, p0, args=(filtered, qqq_dates))
p = plsq[0]
print("P", p)