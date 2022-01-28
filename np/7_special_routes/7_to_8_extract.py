# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 7_to_8_extract
Author    : Focus
Date      : 8/22/2021 11:18 PM
Keywords  :  np.extract
Abstract  :
Param     : 
Usage     : py 7_to_8_extract
Reference :
"""
import numpy as np


a = np.arange(7)

# 1. extract
condition = (a % 2) == 0
print("conditons: \n", condition)

# >> conditons:
# >>  [ True False  True False  True False  True]
print("Even number", np.extract(condition, a))
#>> Even number [0 2 4 6]


# 2. nonzero
print("Non zero", np.nonzero(a))
# >> Non zero (array([1, 2, 3, 4, 5, 6], dtype=int64),)