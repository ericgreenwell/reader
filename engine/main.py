#! usr/bin/python
import RPi.GPIO as GPIO
import os, sys
import time
from picamera import PiCamera
import cv2
import numpy as np
import peakutils
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from scipy.signal import find_peaks_cwt

dirPath = os.path.dirname(sys.argv[0])
imagePath = os.path.abspath(dirPath+'static/images')
LED_PIN = 24
LED_PIN_2 = 23

######### SETUP GPIO #########
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)

########### SETUP CAMERA #########
#app = Flask(__name__)
#app.config["CACHE_TYPE"] = "null"
#cache = Cache(app, config={'CACHE_TYPE':'null'})
#cache.init_app(app)

# Index route

cache.clear()
if os.path.exists(imagePath+'/raw_image.jpg'):
  os.remove(imagePath+'/raw_image.jpg')

#  return render_template('index.html')

#@cache.cached(timeout=10)

#cache.clear()
#print('Measuring Single Channel...')
cam = PiCamera()
cam.resolution=(600,60)
cam.shutter_speed=550000
cam.iso=120
GPIO.output(LED_PIN, GPIO.HIGH)
GPIO.output(LED_PIN_2, GPIO.HIGH)

cam.capture(imagePath + '/raw_image.jpg')
time.sleep(8)
#print('saving image to:' + imagePath + '/raw_image.jpg')
cam.close()
GPIO.output(LED_PIN, GPIO.LOW)
GPIO.output(LED_PIN_2, GPIO.LOW)

img = cv2.imread(imagePath + '/raw_image.jpg')
#print('opening image from:' + imagePath + '/raw_image.jpg')
ROI = img[:,:,2]
#ROI = cv2.equalizeHist(ROI)
#print('plotting')
avg = -ROI.mean(axis=0)
avg = avg + 200
baseline_vals = peakutils.baseline(avg)

_, ax = plt.subplots(2,1)

ax[0].plot(avg)
ax[0].plot(baseline_vals)
ax[0].set_ylabel('8-bit Value')
ax[0].grid(True)

cleanDat= avg-baseline_vals
indices=peakutils.indexes(cleanDat, thres=0.5, min_dist=30)
peaks = cleanDat[indices]
  
ax[1].plot(indices, peaks, 'x')
ax[1].plot(cleanDat)
ax[1].set_xlabel('pixel Index')
ax[1].set_ylabel('8-bit Value')
ax[1].grid(True)

#  print('finished plotting')
plt.savefig(imagePath+ '/raw_data.jpg')
plt.close()
#  print('found {} peaks'.format(len(indices)))

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

print("finished")

sys.stdout.flush()


