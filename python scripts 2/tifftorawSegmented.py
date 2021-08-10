from PIL import Image
import numpy as np
import os
from numpy import asarray
slices = []

src = '/home/krupa/Documents/Research/VirtualEndoscopy/data/segmented' #tiff file directory
f = open('seg_final.raw','a')
for i in range(5,8506,5):
  print(i)
  image = "{:04d}".format(i) + '.tif'
  image = Image.open(os.path.join(src,image))
  
  #image.thumbnail((2468//5, 1407//5))
  image = np.array(image)
  
  
  image = image.flatten('C')
  
  image.tofile(f)
