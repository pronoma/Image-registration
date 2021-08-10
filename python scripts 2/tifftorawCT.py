from PIL import Image
import numpy as np
import os
from numpy import asarray
slices = []

imageList = '/home/krupa/Documents/Research/VirtualEndoscopy/data/01VisibleMale/VM-2-1' #tiff file directory
for afile in sorted(os.listdir(imageList)):
    print(afile)
    img = Image.open(os.path.join(imageList,afile)).convert('L') 
    arr = asarray(img)
    arr.flatten('C')  #if image gets transposed, then 
    #flatten('F')
    slices.append(arr)

arr2 = np.array(slices).flatten('C').astype('uint8')
arr2.tofile("CT.raw")   #Output file location
