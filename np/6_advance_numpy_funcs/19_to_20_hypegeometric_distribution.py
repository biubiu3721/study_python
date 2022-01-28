# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 19_to_20_hypegeometric_distribution
Author    : Focus
Date      : 8/22/2021 4:37 PM
Keywords  :  
Abstract  :
Param     : 
Usage     : py 19_to_20_hypegeometric_distribution
Reference :
"""
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show


points = np.zeros(100)
# sum(1,1,0) , 1 for first class, 0 for odd class.
# choose nsamples from (ngood + nbad), return the number of ngoods.
outcomes = np.random.hypergeometric(ngood=25, nbad=1, nsample=3, size=len(points))
for i in range(len(points)):
    if outcomes[i] == 3:
        points[i] = points[i - 1] + 1
    elif outcomes[i] == 2:
        points[i] = points[i - 1] - 6
    else:
        print("i:", outcomes[i])
plot(np.arange(len(points)), points)
show()