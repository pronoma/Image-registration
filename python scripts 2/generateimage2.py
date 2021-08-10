from PIL import Image
import PIL
import numpy as np
for i in range(5,1006,5):

  image = np.zeros((1407,2468),dtype = 'ushort')
  image = Image.fromarray(image)
  x = "{:04d}".format(i)
  image.save(f'{x}.tif')
