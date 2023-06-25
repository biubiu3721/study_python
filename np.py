# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : np
Author    : Focus
Date      : 6/12/2023 1:27 PM
Keywords  : 
Abstract  :
Param     : 
Usage     : py np
Reference :
"""

import numpy as np
# import matplotlib.pyplot as plt
# import sys

N = 16
PI = 3.14159265358979323846264338327950288
SAMPLE_RATE = 10000.0


class Complex:
    def __init__(self, real, image):
        self.r = real
        self.i = image


def fft(complex_arr, n):

    if n > 1:
        k = 0
        m = 0
        z = Complex(0, 0)
        w = Complex(0, 0)
        ve = [Complex(0, 0) for _ in range(int(n / 2))]
        vo = [Complex(0, 0) for _ in range(int(n / 2))]
        for k in range(0, int(n/2)):
            ve[k] = complex_arr[2 * k]
            vo[k] = complex_arr[2 * k + 1]
        ve = fft(ve, int(n / 2))
        vo = fft(vo, int(n / 2))
        ret = [Complex(0, 0) for _ in range(n)]
        for m in range(0, int(n / 2)):
            w.r = np.cos(2 * PI * m / n)
            w.i = -np.sin(2 * PI * m / n)
            z.r = w.r * vo[m].r - w.i * vo[m].i
            z.i = w.r * vo[m].i - w.i * vo[m].r
            ret[m].r = ve[m].r + z.r
            ret[m].i = ve[m].i + z.i
            ret[m + int(n / 2)].r = ve[m].r - z.r
            ret[m + int(n / 2)].i = ve[m].i - z.i
        return ret
    else:
        return complex_arr


if __name__ == "__main__":
    print("start in main")
    t = np.arange(N)
    b = np.sin(t)
    b = t
    print(b)
    print("sum(b)=", np.sum(b))
    s = np.fft.fft(b)
    print(s)

    varr = [Complex(0, 0) for _ in range(N)]
    for k in range(0, N):
        varr[k].r = t[k]
        varr[k].i = 0

    ret = fft(varr, N)

    for i in range(0, N):
        print(varr[i].r, varr[i].i, np.sqrt(varr[i].r**2 + varr[i].i ** 2))
