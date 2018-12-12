

from picamera import PiCamera
#from picamera.array import PiRGBArray
import RPi.GPIO as gpio
#import cv2
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


cam = PiCamera()
#cam.resolution= (600,60)
#cam.shutter_speed=80000
#cam.iso=80
#cam.brightness=40
#cam.framerate = 30
#cam.capture(fullpath+'/raw_image.jpg')

#img = cv2.imread(fullpath+'/raw_image.jpg')
#raw_capture = PiRGBArray(cam)

#img = raw_capture.array

#cv2.imshow("CV2 Image", img)
#cv2.waitKey(0)
#gpio.output(24, gpio.HIGH)
#gpio.output(23, gpio.HIGH)
cam.start_preview()
sleep(10)
cam.stop_preview()
cam.capture('ROITest.jpg')
#gpio.output(24,gpio.LOW)
#gpio.output(23, gpio.LOW)
l.stop()
r.stop()

#cam.close()
gpio.cleanup()
