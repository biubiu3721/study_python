# -*- coding:utf-8 -*-
"""
Project   :
File Name :
Key word  : Modulo.
Abstract  : Modulo Operation
            The modulo or remainder can be calculated using the NumPy mod,
            remainder, and fmod functions. Also, one can use the % operator.
            The main difference among these functions is how they deal with
            negative numbers.
            The odd one out in this group is the fmod function.
Author    : Focus
Date      : 8/21/2021 1:26 PM
"""
import numpy as np
a = np.arange(-4, 4)
print("Remainder", np.remainder(a, 2))
print("Mod", np.mod(a, 2)) # Exactly the same
# shorthand
print("% operator", a % 2)
print("fmod:", np.fmod(a, 2))
