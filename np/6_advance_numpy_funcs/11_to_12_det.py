# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 11_to_12_det
Author    : Focus
Date      : 8/21/2021 10:22 PM
Keywords  :  Determination
Abstract  :  !!! 行列式描述的是一个线性变换对"由向体积"所造成的.
             行列式的值为正表示保持空间的定向(顺时针或逆时针),
             为负表示颠倒了空间的定向.
             之前从未见到由文献提到这个概念.
             For an n x n real value matrix the determinant corresponds
             to the scaling an n-dimensional volume undergoes
             when transformed by the matrix.
             The positive sign of the determinant means the volume
             preserves its orientation ("clockwise" or "anticlockwise"),
             while a negative sign means reversed orientation.
             看了原著中的英文, 我觉得是翻译的问题， 英文部分是对det经常见到的解释.
Param     : 
Usage     : py 11_to_12_det
Reference :
"""
import numpy as np


A = np.mat("3 4; 5 6")
print("A: \n", A)
print("Determination: ", np.linalg.det(A))



