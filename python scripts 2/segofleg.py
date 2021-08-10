import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
cryos ='/home/krupa/Documents/Research/VirtualEndoscopy/data/01VisibleMale/VM-3'
segs = '/home/krupa/Documents/Research/VirtualEndoscopy/data/segmented'
segd = '/home/krupa/Documents/Research/VirtualEndoscopy/data/oriseg'
eroded = '/home/krupa/Documents/Research/VirtualEndoscopy/data/erodedseg'

final_leg = '/home/krupa/Documents/Research/VirtualEndoscopy/data/finalleg'
for i in range(8075,8076,5):
  
  images = "{:04d}".format(i) + '.tif'
  print(images)
  cryop = os.path.join(cryos,images)
  segp = os.path.join(segs,images)
  img = cv2.imread(cryop)
  seg = cv2.imread(segp)
  seg = cv2.cvtColor(seg,cv2.COLOR_BGR2GRAY)
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  #print(seg)
  seg[seg==0] = 255
  seg[seg!=255] = 0
  segdp = os.path.join(segd,images)
  cv2.imwrite(segdp,seg)
  kernel = np.ones((5,5), np.uint8)
 
# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
  img_erosion = cv2.erode(seg, kernel, iterations=5)
  erodedp = os.path.join(eroded,images)
  cv2.imwrite(erodedp,img_erosion)
  img = cv2.imread(cryop)
  b,g,r = cv2.split(img)
  rgb_img = cv2.merge([r,g,b])

  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

  # noise removal
  kernel = np.ones((2,2),np.uint8)
  closing = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
  #closing = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel, iterations = 2)

  # sure background area
  sure_bg = cv2.dilate(closing,kernel,iterations=3)

  # Finding sure foreground area
  dist_transform = cv2.distanceTransform(sure_bg,cv2.DIST_L2,3)

  # Threshold
  #unknown = cv2.subtract(sure_bg,img_erosion)
  unknown = cv2.subtract(sure_bg,seg)

# Marker labelling
  #ret, markers = cv2.connectedComponents(img_erosion)
  ret, markers = cv2.connectedComponents(seg)

# Add one to all labels so that sure background is not 0, but 1
  markers = markers+1

# Now, mark the region of unknown with zero
  markers[unknown==255] = 0

  markers = cv2.watershed(img,markers)
  # img[markers != -1] = [255,0,0]
  
  img[sure_bg!=0] = [0,0,0]
  final_legp = os.path.join(final_leg,images)
  cv2.imwrite(final_legp,img)
  
