# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 5_argmax.py
Author    : Focus
Date      : 8/22/2021 10:59 PM
Keywords  : np.argmax, np.nanargmax, np.argwhere
Abstract  : np.nanargmax will ignore 'NAN'.
Param     : 
Usage     : py 5_argmax.py
Reference :
"""
import numpy as np


a = np.array([2, 4, 8])
print(np.argmax(a))
b = np.array([np.nan,2, 4])
print(np.nanargmax(b))
c = np.array([2, 4, 8])
print(np.argwhere(a <= 4))

