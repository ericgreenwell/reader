import cv2
import pytesseract
from time import sleep
import numpy as np
from PIL import Image
import Image
import RPi.GPIO as gpio
from time import sleep
import os, sys

pathname=os.path.dirname(sys.argv[0])
fullpath=os.path.abspath(pathname)

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(24, gpio.OUT)
gpio.setup(23, gpio.OUT)

r = gpio.PWM(23,120)
l = gpio.PWM(24, 120)
r.start(30)
l.start(30)


#cam = PiCamera()
#cam.resolution= (600,60)
#cam.shutter_speed=80000
#cam.iso=80
#cam.brightness=40
#cam.framerate = 30
#cam.capture(fullpath+'/raw_image.jpg')

#cam.capture('ROITest.jpg')
#gpio.output(24,gpio.LOW)
#gpio.output(23, gpio.LOW)

l.stop()
r.stop()

#cam.close()
gpio.cleanup()
cap = cv2.VideoCapture(0)
#cap.set(15, 100)
while:
  _, im = cap.read()

  #im = cv2.imread('ROITest.jpg',0)
  rot = np.rot90(im)
  full = np.rot90(rot)

  clipped = full[350:480, 100:700]
  equal = cv2.equalizeHist(clipped)
  #equal = cv2.equalizeHist(equal)

  #thresh = 18
  #equal = cv2.threshold(clipped, thresh, 255, cv2.THRESH_BINARY)[1]

  cv2.imshow("clipped", equal)
  


  print(pytesseract.image_to_string(equal))
  print(pytesseract.image_to_string(Image.fromarray(equal)))
  
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
  
cv2.DestroyAllWindows()
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
