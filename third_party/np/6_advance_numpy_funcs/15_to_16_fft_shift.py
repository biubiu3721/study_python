# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 15_to_16_fft_shift
Author    : Focus
Date      : 8/21/2021 11:44 PM
Keywords  :  
Abstract  :
Param     : 
Usage     : py 15_to_16_fft_shift
Reference :
"""
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

x = np.linspace(0, 2 * np.pi, 30) # Create a cosine signal standed by 30 points.
wave = np.cos(x)
transformed = np.fft.fft(wave)
shifted = np.fft.fftshift(transformed)
print(np.all((np.fft.ifftshift(shifted) - transformed) < 10 ** -9))
plot(wave, lw=1)
plot(transformed, lw=2)
plot(shifted, lw=3)
show()

