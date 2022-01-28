# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 1_to_2_sort
Author    : Focus
Date      : 8/22/2021 10:17 PM
Keywords  : lexsort
Abstract  :
Param     : 
Usage     : py 1_to_2_sort
Reference :
"""
import numpy as np


import numpy as np
import datetime


def date_str_to_num(s):
    s = str(s, encoding='utf-8')
    return datetime.datetime.strptime(s, "%d-%m-%Y").toordinal()


dates, closes = np.loadtxt("./AAPL.csv", delimiter=',', usecols=(1, 6), converters={1 : date_str_to_num}, unpack=True)
closes = np.round(closes)
indices = np.lexsort((dates, closes)) # based on the last column.
print("Indices", indices)
print( ["%s %s " % (datetime.date.fromordinal(int(dates[i])), closes[i]) for i in indices])

