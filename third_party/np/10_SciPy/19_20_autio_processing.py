# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 10_autio_processing
Author    : Focus
Date      : 8/25/2021 1:57 PM
Keywords  : audio, tile, wavefile urllib2
Abstract  :
Param     : 
Usage     : py 10_autio_processing
Reference :
"""

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import sys
import urllib.request as url_req

# section 2
web_addr = "http://www.thesoundarchive.com/austinpowers/smashingbaby.wav"
response = url_req.urlopen(web_addr)
bytes = response.read()
print(response.info)
WAV_FILE = "smashingbaby.wav"

# second 3
filehandle = open(WAV_FILE, "wb") # wb for b'**', w for str
filehandle.write(bytes) #
filehandle.close()

# second 4
sample_rate, data = wavfile.read(WAV_FILE)
print("sample_rate:", sample_rate, "Data type", data.dtype, "Shape", data.shape)

# section 5

plt.subplot(2, 1, 1)
plt.title("Original")
plt.plot(data)

# Section
plt.subplot(2,1,2)
repeated = np.tile(data, int(5))
plt.title("Repeated")
plt.plot(repeated)
wavfile.write("repeated_yababy.wav", sample_rate, repeated)
plt.show()