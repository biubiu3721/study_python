# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 1_calc_inv_mat
Author    : Focus
Date      : 8/21/2021 4:17 PM
Keywords  : Inverse
Abstract  :
Param     : 
Usage     : py 1_calc_inv_mat
Reference :
"""
import numpy as np
print("Only Support Square Matrix and Non singular matrix")

A = np.mat("0  1  2; 1 0 3; 4 -3 8")
print("A\n", A)
inverse = np.linalg.inv(A)
print("Inverse A: \n", inverse)
