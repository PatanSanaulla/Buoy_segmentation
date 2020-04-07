import cv2
from conditionalProbablity import *
import matplotlib.pyplot as plt
import numpy as np

color = 'green'
ColorInfo = sendColorInfo(color)
B_intensities = ColorInfo['B_intensities'][1:-1].split(',')
for index, each in enumerate(B_intensities):
    B_intensities[index] = int(each)
print(B_intensities)
#
plt.figure(1)
n, bins, patches = plt.hist(B_intensities, bins=255)  # `density=False` would make counts
N = [int(x/30) for x in n]
plt.show()
plt.figure(2)
plt.plot(N)
plt.savefig('hist_of_'+color+"_buoy_"+"blue"+"_channel.png")
plt.show()
