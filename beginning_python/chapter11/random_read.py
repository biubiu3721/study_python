# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : random_read.py
Author    : Focus
Date      : 8/14/2023 11:00 AM
Keywords  : 
Abstract  :
Param     : 
Usage     : py random_read.py
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys

f = open("./somefile.txt", "w")
print(f.write("01234567890123456789"))
print(f.seek(5))
print(f.write("Hello World!"))
f.close()
f = open(r"somefile.txt")
print(f.read())
f.close()
f = open("./somefile.txt")
print(f.read(3))
print(f.read(2))
print(f.tell())