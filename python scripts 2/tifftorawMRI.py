from PIL import Image
import numpy as np
import os
from numpy import asarray
src = '/home/krupa/Documents/Research/VirtualEndoscopy/data/erodedseg'
f = open('erodedseg.raw','a')
for i in range(7940,8506,5):
  print(i)
  image = "{:04d}".format(i) + '.tif'
  
  image = np.array(Image.open(os.path.join(src,image)))
  
  
  image = image.flatten('C')
  
  image.tofile(f)
