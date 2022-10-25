# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 6_searchsorted.py
Author    : Focus
Date      : 8/22/2021 11:04 PM
Keywords  : insert, sorted, index
Abstract  : find the index of a value, after it has been inserted to an sorted array.
Param     :
            value:
            sorted_array

Usage     : py 6_searchsorted.py
Reference :
"""
import numpy as np


a = np.arange(5)
indices = np.searchsorted(a, [-2, 7])
print("Indices", indices)
# Futher, use insert to combine intact array.
print("The full array", np.insert(a, indices, [-2, 7]))
