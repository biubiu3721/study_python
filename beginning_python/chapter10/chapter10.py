# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : chapter10
Author    : Focus
Date      : 6/28/2023 7:35 PM
Keywords  : 
Abstract  :
Param     : 
Usage     : py chapter10
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys

import sys
sys.path.append("./python")
import hello
import hello

import importlib
importlib.reload(hello)
importlib.reload(hello)

import drawing
import drawing.colors
import drawing.shapes

import copy
print([n for n in dir(copy) if not n.startswith("_")])
print(copy.__all__)
print(copy.__doc__)

import webbrowser

webbrowser.open("www.python.org")


