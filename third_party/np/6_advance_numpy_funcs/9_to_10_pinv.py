# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 5_9_to_5_10
Author    : Focus
Date      : 8/21/2021 10:14 PM
Keywords  : Moore Penrose pseudo inverse
Abstract  :
Param     : 
Usage     : py 5_9_to_5_10
Reference :
"""
import numpy as np
A = np.mat("4 11 14; 8 7 -2")
print("A: \n", A)
p_inv0 = np.linalg.pinv(A)
print("Checking:-------")
print(A * p_inv0)

