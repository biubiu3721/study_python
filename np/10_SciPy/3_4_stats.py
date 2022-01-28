# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 3_4_stats
Author    : Focus
Date      : 8/24/2021 10:39 PM
Keywords  : 
Abstract  :
Param     : 
Usage     : py 3_4_stats
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import stats
generated = stats.norm.rvs(size=900)
print("Mean", "std", stats.norm.fit(generated))
print("Skewtest", "pvalue", stats.skewtest(generated))
print("Kurtosistest", "pvalue", stats.kurtosistest(generated))
print("Normality test", stats.normaltest(generated))
print("95 Percentile", stats.scoreatpercentile(generated, 95))
print("95 Percentile", stats.percentileofscore(generated, 1))
plt.hist(generated)
plt.show()