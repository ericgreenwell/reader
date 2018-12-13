
import cv2
import numpy as np
import peakutils
import matplotlib
import sys
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
#plt.switch_backend('agg')
from scipy.signal import find_peaks_cwt

im = cv2.imread("whole.jpg",0)

#im = im[:,:,2]

temp = np.rot90(im)
rot = np.rot90(temp)

clipped =rot[110:240, 115:660]

#equal = cv2.equalizeHist(clipped)

avg = -clipped.mean(axis=0)
avg = avg+200 
baseline_vals = peakutils.baseline(avg,4)

_, ax = plt.subplots(2,1)
ax[0].plot(avg)
ax[0].plot(baseline_vals)
ax[0].set_ylabel('8-bit Val')
ax[0].grid(True)

cleanDat= avg-baseline_vals
indices=peakutils.indexes(cleanDat, thres=0.5, min_dist=30)
peaks = cleanDat[indices]
  
ax[1].plot(indices, peaks, 'x')
ax[1].plot(cleanDat)
ax[1].set_xlabel('pixel Index')
ax[1].set_ylabel('8-bit Value')
ax[1].grid(True)

#cv2.imshow("clipped",clipped)
#cv2.waitKey(0)

if len(indices) == 2:
  print('matched')
  rat = peaks[0]/peaks[-1]
  if rat > 0.6:
    res = 'Postitive'
  if 0.3 <= rat <= 0.6:
    res = 'Weak Positive'

elif len(indices) == 1:
  res= 'Negative'
  rat = 0


plt.show()
plt.close()

#print("finished")

#sys.stdout.flush()


