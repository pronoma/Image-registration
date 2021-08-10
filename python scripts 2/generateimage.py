from PIL import Image
import PIL
import numpy as np
image = Image.open('/home/krupa/Documents/Research/VirtualEndoscopy/python scripts/0075.tif')
image = np.array(image)
print(image[700][1200])
x = np.where(image==0)
image2 = Image.open('/home/krupa/Documents/Research/VirtualEndoscopy/python scripts/try.png')

image2 = np.array(image2)
print(image2.shape)
print(image[700][1200])
image2[x[0],x[1]] =78
image2 = Image.fromarray(image2)
image2.save('0075.tif')



