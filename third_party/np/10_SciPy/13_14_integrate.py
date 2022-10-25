# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 13_14_integrate
Author    : Focus
Date      : 8/25/2021 1:35 AM
Keywords  : integrate
Abstract  :
Param     : 
Usage     : py 13_14_integrate
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import integrate
print("Gauss inegral: ", np.sqrt(np.pi))
ret = integrate.quad(lambda x: np.exp(-x ** 2), -np.inf, np.inf)
print(ret)