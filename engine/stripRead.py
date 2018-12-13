
import cv2
import numpy as np

im = cv2.imread("whole.jpg",0)

temp = np.rot90(im)
rot = np.rot90(temp)

clipped =rot[110:240, 115:660]

#equal = cv2.equalizeHist(clipped)

avg = -clipped.mean(axis=0)
avg = avg + 200
baseline_vals = peakutils.baseline(avg)

_, ax = plt.subplots(2,1)
ax[0].plt(avg)
ax[0].plot(baseline_vals)
ax[0].set_ylabel('8-bit Val')
ax[0].grid(True)

cv2.imshow("clipped",equal)
cv2.waitKey(0)

