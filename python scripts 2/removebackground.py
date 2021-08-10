import PIL
from PIL import Image
import numpy as np
import os
import cv2
cryo_src='/home/krupa/Documents/Research/VirtualEndoscopy/data/01VisibleMale/VM-3' #folder to cryo images
seg_src='/home/krupa/Documents/Research/VirtualEndoscopy/data/segmented' #folder to segmented images
dst = '/home/krupa/Documents/Research/VirtualEndoscopy/data/backgroundcleancryo' #folder to new noise free images
for i in range(5,8506,5):
  print(i)
  images = "{:04d}".format(i) + '.tif'
  cpath = os.path.join(cryo_src,images)
  spath = os.path.join(seg_src,images)
  cryo = Image.open(cpath)
  seg = Image.open(spath)
  
  cryo = np.array(cryo)
  seg = np.array(seg)
  x = np.where(seg!=0)
  seg[x[0],x[1]] = 66535
  kernel = np.ones((3,3), np.uint8) 
  img_dilation = cv2.dilate(seg, kernel, iterations=1)
  z=np.where(img_dilation==0)
  #z=np.where(seg==0)
  cryo[z[0],z[1]] = [0,0,0]
  cryo = Image.fromarray(cryo)
  cpath = os.path.join(dst,images)
  cryo.save(cpath)

