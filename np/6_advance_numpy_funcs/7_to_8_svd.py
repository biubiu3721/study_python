# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 7_to_8_svd
Author    : Focus
Date      : 8/21/2021 9:29 PM
Keywords  : 1. Singular Value Decomposition
            2.TODO(Yu) eigenvalue decompositon.
            3. Orthogonal Matric: A*Transpose(A) == E or Transpose(A) * A == E
            4. Eigen Decomposition(=Spectral Decomposition)
Abstract  : M = U * Sigma * HermitianConjugate(V)
Param     : 
Usage     : py 7_to_8_svd
Reference :
"""
import numpy as np


A = np.mat("4 11 14; 8 7 -2")
print("A \n", A)
U, Sigma, V = np.linalg.svd(A, full_matrices=False)
print("----------\n""U: \n", U)
print("----------\n""Sigma:\n", Sigma)
print("----------\n""V: \n", V)

print("Product: \n", U * np.diag(Sigma) * V)

