

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

r = gpio.PWM(23,60)
l = gpio.PWM(24, 60)
r.start(15)
l.start(15)


cam = PiCamera()
#cam.resolution= (600,60)
cam.shutter_speed=8500000 #OCR: 8000000
#cam.iso=80
cam.brightness=70  # OCR 70
cam.contrast=100   # OCR 100

cam.start_preview()
sleep(10)
cam.stop_preview()
cam.capture('ocr.jpg')


l.stop()
r.stop()

#cam.close()
gpio.cleanup()
