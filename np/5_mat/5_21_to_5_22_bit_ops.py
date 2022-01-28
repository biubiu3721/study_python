# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 5_21_to_5_22_bit_ops
Author    : Focus
Date      : 8/21/2021 3:33 PM
Keywords  : Bitwise, Compare
Abstract  : 1.Check(Sign(x) == Sign(y)).
            2 Check(log(2,n) == floor(log(2,n)))
            3. Compute x = n - 2^(floor(log(2,n))
Param     : 
Usage     : py 5_21_to_5_22_bit_ops
Reference :
"""
import numpy as np


"""
1. Check(Sign(x) == Sign(y)).
"""
x = np.arange(-9, 9)
y = -x
print("bit xor", x ^ y)
print("Sign different? ", (x ^ y) < 0)
print("Sign different? ", np.less(np.bitwise_xor(x, y), 0))


"""
2. Check a number is power of 2.
"""
x = np.arange(-9, 9)
print("Pow of 2\n", x,)
print(x & (x - 1) == 0)
print(np.equal(0, np.bitwise_and(x, x - 1)))


"""
3. Bitwise for Mod. 
"""
print("Modulus 4 \n", x, "\n", x & (1 << 2) - 1)
print("Modulus 4 \n", x, "\n", np.bitwise_and(x, np.left_shift(1, 2) - 1))

