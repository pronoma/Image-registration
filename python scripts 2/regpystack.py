import os
import numpy as np
#import cv2
from PIL import Image
import pystackreg
from pystackreg import StackReg
f = open('CT_bilinear.raw','a')
cryo = '/home/krupa/Documents/Research/VirtualEndoscopy/data/01VisibleMale/VM-3'
ct = '/home/krupa/Documents/Research/VirtualEndoscopy/data/01VisibleMale/VM-2-1'

for i in range(0,8506,5):
  id = "{:04d}".format(i) + '.tif'
  image = os.path.join(cryo,id)
  print(image)
  img = Image.open(image)
  img = img.resize((494,281))
  img = np.array(img)
  mov = Image.open(os.path.join(ct,id))
  mov = np.array(mov)
  ref = np.array(img[:,:,0])
  sr = StackReg(StackReg.BILINEAR)
  reg = sr.register_transform(ref, mov)
  reg = reg.clip(min=0)
  reg = reg.astype('uint8')
  #id = "{:04d}".format(i) + '.png'
  reg = reg.flatten('C')
  
  reg.tofile(f)  
  #reg.save(os.path.join(dst,id))
