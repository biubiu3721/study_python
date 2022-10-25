# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 3_to_4_complex_sort.py
Author    : Focus
Date      : 8/22/2021 10:45 PM
Keywords  : Complex number, np.sort_complex()
Abstract  :
Param     : 
Usage     : py 3_to_4_complex_sort.py
Reference :
"""
import numpy as np


np.random.seed(42)
complex_num = np.random.random(5) + 1j * np.random.random(5)
print("Complex number \n", complex_num)
print("Sorte: \n", np.sort_complex(complex_num))



