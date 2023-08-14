# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : numberlines.py
Author    : Focus
Date      : 7/27/2023 10:38 AM
Keywords  : 
Abstract  :
Param     : 
Usage     : py numberlines.py
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys

import fileinput

for line in fileinput.input(inplace=False):
    line = line.rstrip()
    num = fileinput.lineno()
    print('{:<50} # {:2d}'.format(line, num))