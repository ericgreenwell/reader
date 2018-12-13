import cv2
import pytesseract
from time import sleep
import numpy as np
from PIL import Image
import Image
import RPi.GPIO as gpio
from time import sleep
import os, sys
from picamera import PiCamera

pathname=os.path.dirname(sys.argv[0])
fullpath=os.path.abspath(pathname)

im = cv2.imread('ocr.jpg',0)

cv2.imshow("original", im)
cv2.waitKey(0)
rot = np.rot90(im)
full = np.rot90(rot)

clipped = full[350:480, 150:600]
equal = cv2.equalizeHist(clipped)
  #equal = cv2.equalizeHist(equal)

thresh = 42
kernel = np.ones((5,5), np.uint8)
binary = cv2.threshold(clipped, thresh, 255, cv2.THRESH_BINARY)[1]

dilated = cv2.erode(binary, kernel, iterations=2)
eroded = cv2.dilate(dilated, kernel, iterations=1)


cv2.imshow("clipped", eroded)
  
cv2.waitKey(0)

print(pytesseract.image_to_string(eroded))

"""  
0CAP_PROP_POS_MSEC Current position of the video file in milliseconds or video capture timestamp.
1CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
2CAP_PROP_POS_AVI_RATIO Relative position of the video file: 0 - start of the film, 1 - end of the film.
3CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
4CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
5CAP_PROP_FPS Frame rate.
6CAP_PROP_FOURCC 4-character code of codec.
7CAP_PROP_FRAME_COUNT Number of frames in the video file.
8CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
9CAP_PROP_MODE Backend-specific value indicating the current capture mode.
10CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
11CAP_PROP_CONTRAST Contrast of the image (only for cameras).
12CAP_PROP_SATURATION Saturation of the image (only for cameras).
13CAP_PROP_HUE Hue of the image (only for cameras).
14CAP_PROP_GAIN Gain of the image (only for cameras).
15CAP_PROP_EXPOSURE Exposure (only for cameras).
16CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
17CAP_PROP_WHITE_BALANCE Currently not supported
18CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
"""
