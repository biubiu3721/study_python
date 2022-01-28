# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 19_to_20
Author    : Focus
Date      : 8/23/2021 9:49 AM
Keywords  : 
Abstract  :
Param     : 
Usage     : py 19_to_20
Reference :
"""
import numpy as np
import unittest
# import matplotlib.pyplot as plt
# import sys


def factorial(n):
    if n == 0:
        return 1

    if n < 0:
        raise(ValueError, "Unexpected negative value")

    return np.arange(1, n + 1).cumprod()

class FactorialTest(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(6, factorial(3)[-1])
        np.testing.assert_equal(np.array([1, 2, 6]), factorial(3))
    def test_zero(self):
        self.assertEqual(1, factorial(0))
    def test_negative(self):
        self.assertRaises(IndexError, factorial(-10))


unittest.main()