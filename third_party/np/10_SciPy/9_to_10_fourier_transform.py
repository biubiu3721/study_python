# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 9_fourier_transform
Author    : Focus
Date      : 8/24/2021 11:14 PM
Keywords  : fourier transform
Abstract  :
Param     :
Usage     : py 9_fourier_transform
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
amps[amps < 0.1 * amps] = 0
fig = plt.figure()
fig.subplots_adjust(hspace=0.3)
ax=fig.add_subplot(211)



def residuals(p, y, x):
    A, k, theta, b = p
    stage1 = np.array(2 * np.pi * k) * np.array(x) + theta
    err = y - A * np.sin(stage1) + b
    return err


filtered = -fftpack.irfft(fftpack.ifftshift(amps))
N = len(qqq_dates)
f = np.linspace(-N / 2, N / 2, N)
p0 = [int(filtered.max()), int(f[amps.argmax()]/ (2 * N)), 0, 0]
print("P0: ", p0)


import pandas
import time
import datetime

print(qqq_dates)
int_times = []
for i in range(len(qqq_dates)):
    fp_time = time.mktime(time.strptime(str(qqq_dates[i]), "%Y-%m-%d %H:%M:%S"))
    int_times.append(int(fp_time))

from scipy import optimize

plsq = optimize.leastsq(residuals, p0, args=(filtered, int_times))
p = plsq[0]
print("P", p)

plt.plot(qqq_dates, y, "o", label="detrended")
plt.plot(qqq_dates, filtered, label="filtered")
plt.plot(qqq_dates, p[0] * np.sin(np.array(2 * np.pi) * int_times * np.array(p[1]) + p[2]) + p[3], '^', label="fit")
plt.show()

#plt.plot(qqq_dates, -fftpack.irfft(fftpack.ifftshift(amps)), label="filter")
#plt.legend(prop={"size":"x-large"})
#ax2 = fig.add_subplot(212)
#ax2.tick_params(axis="both", which="major", labelsize="x-large")
#N = len(qqq_dates)
#plt.plot(np.linspace(-N/2, N/2, N), amps, label="transformed")
#plt.legend(prop={"size": "x-large"})
#plt.show()