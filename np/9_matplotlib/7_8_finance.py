# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 7_8_finance
Author    : Focus
Date      : 8/23/2021 1:49 PM
Keywords  : matplotlib.finance, matplotlib.dates,
Abstract  :
Param     : 
Usage     : py 7_8_finance
Reference :
"""
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
import mplfinance as mpf
import pandas_datareader.data as web
import pandas as pd
import sys
from datetime import date
import matplotlib.pyplot as plt

today = date.today()
start = (today.year - 1, today.month, today.day)
alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")
df = web.DataReader('DISH', 'yahoo', start='2012-12-01', end='2013-12-01')
print(df.head())
mpf.plot(df, type="candle", title="Candlestick for DISH")