# -*- coding:utf-8 -*-
"""
Project   : study_python
File Name : c3
Author    : Focus
Date      : 4/10/2023 3:07 PM
Keywords  : 
Abstract  :
Param     : 
Usage     : py c3
Reference :
"""
# import numpy as np
# import matplotlib.pyplot as plt
# import sys


width = int(input("Please enter width\n"))
price_width = 10
item_width = width - price_width
header_fmt = "{{:{}}}{{:{}}}".format(item_width, price_width)
fmt = "{{:{}}}{{:>{}.2f}}".format(item_width, price_width)
print("=" * width)
print(header_fmt.format("Item", "Price"))
print("-" * width)
print(fmt.format("Apples", 0.4))
print(fmt.format("Pears", 0.5))
print(fmt.format("Cantaloupes", 1.92))
print(fmt.format("Dried Apricots (16 ooz.)", 8))
print(fmt.format("Prunes (4 lbs.)", 12))

print("=" * width)
