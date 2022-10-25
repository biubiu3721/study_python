# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 5_6_compare
Author    : Focus
Date      : 8/24/2021 10:50 PM
Keywords  : from two, scikits.statsmodels.stattools
Abstract  :
Param     : 
Usage     : py 5_6_compare
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import sys
from scipy import stats
import pandas_datareader.data as pdd
from statsmodels.stats.stattools import jarque_bera


def get_close(symbol):
    df = pdd.DataReader(symbol, "yahoo", "2020-01-01", "2021-01-01")
    return df["Close"]


spy = np.diff(np.log(get_close("SPY")))
dia = np.diff(np.log(get_close("DIA")))
print("Means comparison", stats.ttest_ind(spy, dia))
print("Kolmogorov simirnov test", stats.ks_2samp(spy, dia))
print("Jarque Bera test", jarque_bera(spy-dia)[1])


plt.hist(spy, histtype="step", lw=1, label="SPY")
plt.hist(dia, histtype="step", lw=2, label="DIA")
plt.hist(np.abs(spy-dia), histtype="step", lw=3, label="Delta")
plt.legend()
plt.show()