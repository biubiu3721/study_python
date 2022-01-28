# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 11_log_arithmic_plots
Author    : Focus
Date      : 8/23/2021 11:18 PM
Keywords  : Logarithmic,
            bell curve,
            semilogx()
            semilogy()
            loglog()
Abstract  : Logarithmic plots are useful when the data
            has a wide range of values. Matplotlib has the
            fuctions semilogx, semilogy and loglog
Param     : 
Usage     : py 11_log_arithmic_plots
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import mplfinance as plf
import pandas_datareader as pdr
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from  datetime import date
today = date.today()
print(today)
start = date(today.year - 1, today.month, today.day)
symbol = "DISH"

df = pdr.data.get_data_yahoo("DISH", start, today)
print(df.head())
df_Date = df.index
df_Volume = df["Volume"]

print("dates", df_Date)
print("volume", df_Volume)
alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")
fig = plt.figure()
plt.semilogy(df_Date, df_Volume)
plt.show()

