from PIL import Image
import numpy as np
import os
from numpy import asarray

input_dir = '/home/krupa/Documents/Research/VirtualEndoscopy/data/segmented' #tiff file directory
output_dir = '/home/krupa/Documents/Research/VirtualEndoscopy/data/volumes'

src = input_dir
f = open('segmented_final.raw','a')
for i in range(5,8506,5):
  print(i)
  image = "{:04d}".format(i) + '.tif'
  
  image = np.array(Image.open(os.path.join(src,image)))
  
  
  image = image.flatten('C')
  
  image.tofile(f)
