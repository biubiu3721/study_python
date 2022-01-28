# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 5_to_6_eigen
Author    : Focus
Date      : 8/21/2021 5:32 PM
Keywords  :  eigenvalue, scalar, np.linalg.eigenvals
Abstract  :
Param     : 
Usage     : py 5_to_6_eigen
Reference :
"""
import numpy as np
A = np.mat("3 -2; 1 0")
print("A \n", A)
print("Eigenvalues", np.linalg.eigvals(A))
eigenvalues, eigenvectors = np.linalg.eig(A)
print("First tuple of eigen: ", eigenvalues)
print("Second tuple of eigen: ", eigenvectors)

print("Checking:" + "*"*100)

for i in range(len(eigenvalues)):
    x_left = np.dot(A, eigenvectors[:,i])
    x_right = np.dot(eigenvalues[i], eigenvectors[:,i])
    print("left : \n", x_left)
    print("right: \n", x_right)
    print("error: \n", x_left - x_right)

