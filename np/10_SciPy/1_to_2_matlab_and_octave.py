# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 1_to_2_matlab_and_octave
Author    : Focus
Date      : 8/24/2021 10:26 PM
Keywords  :
Abstract  :
Param     : 
Usage     : py 1_to_2_matlab_and_octave
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import io

a = np.arange(7)
io.savemat("a.mat", {"array": a})


