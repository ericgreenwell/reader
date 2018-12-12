import cv2
import pytesseract
from time import sleep
import numpy as np
from PIL import Image
import Image


im = cv2.imread('ROITest.jpg',0)
rot = np.rot90(im)
full = np.rot90(rot)


#cv2.imshow("rotated", full)
#cv2.waitKey(0)

clipped = full[350:480, 100:700]
equal = cv2.equalizeHist(clipped)
equal = cv2.equalizeHist(equal)


#(thresh, equal) = cv2.threshold(equal, 210, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 18
equal = cv2.threshold(clipped, thresh, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("clipped", equal)
cv2.waitKey(0)


print(pytesseract.image_to_string(equal))
print(pytesseract.image_to_string(Image.fromarray(equal)))
