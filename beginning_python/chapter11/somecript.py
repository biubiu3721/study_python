# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : import sys
Author    : Focus
Date      : 8/14/2023 10:54 AM
Keywords  : 
Abstract  :
Param     : 
Usage     : py import sys
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys

import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print("wordcount:", wordcount)
