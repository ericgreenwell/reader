import cv2
import matplotlib.pyplot as plt
import peakutils
from picamera import PiCamera
import os, sys
import io

def process_redline():
  dirPath= os.path.dirname(sys.argv[0])
  imagePath= os.path.abspath(dirPath+'static/images')

  cam = PiCamera()
  cam.capture(imagePath + "/raw_image.jpg")
  cam.close()
  img = cv2.imread(imagePath + '/raw_image.jpg')
  #pick ROI
  ROI = img

  # convert to colo spaces
  gray = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
  
  print('starting to plot')
  plot=io.BytesIO()
  #_,  ax = plt.subplots()
  for col in range(ROI.shape[1]):
    avg = 1000*ROI.mean(axis=0)
  
  indices = peakutils.indexes(-avg)
  plt.plot(avg)
  plt.plot(indices, avg[indices])

  plt.grid()
  #plt.show()

  print('{} peaks found'.format(len(indices)))
  
  plt.savefig(plot, format='jpg')  #, imagePath + '/output_plot.jpg')
  
  plt.close()
  return

