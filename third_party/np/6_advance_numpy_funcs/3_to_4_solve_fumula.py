# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 3_to_4_solve_fumula
Author    : Focus
Date      : 8/21/2021 4:59 PM
Keywords  : np.solve, np.dot
Abstract  : x, s.t. Ax = b
Param     : None
Usage     : py 3_to_4_solve_formula
Reference :
"""
import numpy as np

A = np.mat("1 -2 1; 0 2 -8; -4 5 9")
print("A:\n", A)
b = np.array([0, 8, -9])
print("b:\n", b)
x = np.linalg.solve(A, b)
print("Solution: \n", x)
print("Check: \n", np.dot(A, x))


