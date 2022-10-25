# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 13_14_fast_fourier_transform
Author    : Focus
Date      : 8/21/2021 11:18 PM
Keywords  : Fast Fourier Transform,
Abstract  : Useful on Signal Process, Image Process, Solve Partial Differencial Equaltion
            Complexity: O(N * logN)
            TODO(Yu):   1. 分析清楚快速fourier变换的原理。
                        2. 搞清楚plot图片的意义。
                        3. 如果1，2搞不定就做5道题先。
Param     : 
Usage     : py 13_14_fast_fourier_transform

Reference :
"""
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show


x = np.linspace(0, 2 * np.pi, 30)
wave = np.cos(x)
transformed = np.fft.fft(wave)
print(np.all(np.abs(np.fft.ifft(transformed) - wave) < 10 ** - 9))

plot(transformed)
show()

