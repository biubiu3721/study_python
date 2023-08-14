# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : reverseargs.py
Author    : Focus
Date      : 7/11/2023 11:21 AM
Keywords  : 
Abstract  :
Param     : 
Usage     : py reverseargs.py
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys

import sys
args = sys.argv[1:]
print(sys.argv)
args.reverse()
print(" ".join(args))