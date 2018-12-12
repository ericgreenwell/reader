#! usr/bin/python
import cv2
import matplotlib.pyplot as plt
import peakutils
from picamera import PiCamera
import os, sys
import io

img = cv2.imread('ROITest.jpg')
  #pick ROI
ROI = img[:,:,2]
_,  ax = plt.subplots(2,1)
for col in range(ROI.shape[1]):
  avg = -ROI.mean(axis=0)

avg = avg + 200
baseline_vals = peakutils.baseline(avg)

ax[0].plot(avg)
ax[0].plot(baseline_vals)
ax[0].set_ylabel('8-bit Value')
ax[0].grid(True)

cleanDat= avg-baseline_vals
indices=peakutils.indexes(cleanDat, thres=0.5, min_dist=30)

ax[1].plot(indices, cleanDat[indices], 'x')

ax[1].plot(cleanDat)
ax[1].set_xlabel('pixel Index')
ax[1].set_ylabel('8-bit Value')
ax[1].grid(True)

plt.show()
plt.close()
 

