# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : 10.3
Author    : Focus
Date      : 7/27/2023 3:36 PM
Keywords  : 
Abstract  :
Param     : 
Usage     : py 10.3
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys

from random import randrange


num = int(input("How many dice? "))
sides = int(input("How many sides per die"))
sum = 0
for i in range(num):
    sum += randrange(sides) + 1
print("The result is ", sum)



