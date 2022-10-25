# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 17_18_ndimage
Author    : Focus
Date      : 8/25/2021 1:51 AM
Keywords  : misc.lena().astype(np.float32)
Abstract  :
Param     : 
Usage     : py 17_18_ndimage
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy import ndimage
#TODO(Yu) what's the meaning of misc.
image = misc.ascent().astype(np.float32)

# 1
plt.subplot(221)
plt.title("Original Image")
img = plt.imshow(image, cmap=plt.cm.gray)

# 2 medium filter
plt.subplot(222)
plt.title("Median Filter")
filtered = ndimage.median_filter(image, size=(42, 42))
plt.imshow(filtered, cmap=plt.cm.gray)

# 3. rotate
plt.subplot(223)
plt.title("Rotated")
rotated = ndimage.rotate(image, 90)
plt.imshow(rotated, cmap=plt.cm.gray)

#4 Prewitt
plt.subplot(224)
plt.title("Prewitt")
prewitted = ndimage.prewitt(image)
plt.imshow(prewitted, cmap=plt.cm.gray)


plt.show()