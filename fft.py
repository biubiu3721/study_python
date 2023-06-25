# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : fft
Author    : Focus
Date      : 6/12/2023 9:53 AM
Keywords  : 
Abstract  :
Param     : 
Usage     : py fft
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt

# import sys

if __name__ == "__main__":
    print("start in main")
    ar = 100  # sampling rate
    ts = 1.0 / ar
    t = np.arange(0, 5, ts)
    # sampling frequency = 100 / 5 = 20

    freq = 1
    x = 3 * np.sin(2 * np.pi * freq * t)

    freq = 4.3
    x += np.sin(2 * np.pi * freq * t)

    freq = 7
    x += 0.5 * np.sin(2 * np.pi * freq * t)

    fig, ax = plt.subplots(figsize=(5, 4), dpi=150)
    ax.plot(t, x, 'r')
    ax.set_xlabel("time")
    ax.set_ylabel("Amplitude")

    plt.show()

    from scipy import fft

    X = fft(x)
    print(x)
    print(X)
    N = len(x) #total sample number
    n = np.arange(N)
    T = N / ar # total time = total number / sample_rate

    freq = n / T

    fig, ax = plt.subplots(1, 2, figsize=(10, 4), dpi=150)
    ax[0].stem(freq, np.abs(X), 'b', markerfmt=" ", basefmt="-b")
    ax[0].set_xlable("freq (Hz)")
    ax[0].set_ylable("FFT Amplitute |X(freq|")
    ax[0].set_xlim(4, 10)

