# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 23_to_24_docstring
Author    : Focus
Date      : 8/23/2021 12:10 PM
Keywords  : docstring,
Abstract  :

Param     : 
Usage     :
>> py
>> import numpy as np
>> from numpy.testing import rundocs
>> rundocs(23_to_24_docstring.py)
Reference :
"""
import numpy as np

def factorial(n):
    """
    Test for the factorial of 3 that should pass.
    >>> factorial(3)
    6
    Test for the factorial of 0 that should pass.
    >>> factorial(0)
    1
    """
    return np.arange(1, n + 1).cumprod()[-1]

