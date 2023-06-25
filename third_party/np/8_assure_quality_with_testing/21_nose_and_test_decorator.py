# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 21_nose_and_test_decorator
Author    : Focus
Date      : 8/23/2021 11:24 AM
Keywords  : nose, decorator.py
Abstract  :
            1. pip install nose
Param     : 
Usage     : py 21_nose_and_test_decorator
Reference :
"""
import numpy as np
import setuptools
# import matplotlib.pyplot as plt
# import sys
from numpy.testing import dec

# 1.
@dec.setastest(False)
def test_false():
    pass


# 2.
@dec.setastest(True)
def test_true():
    pass


# 3.
@dec.skipif(True)
def test_skip():
    pass


# 4.
@dec.knownfailureif(True)
def test_alwaysfail():
    pass


class TestClass():
    def test_true2(self):
        pass


class TestClass2():
    def test_false2(self):
        pass


np.testing.decorate_methods(TestClass2, dec.setastest(False), 'test_false2')
