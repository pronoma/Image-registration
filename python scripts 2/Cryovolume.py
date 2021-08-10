from PIL import Image
import numpy as np
import os
from numpy import asarray

input_dir = '/home/krupa/Documents/Research/VirtualEndoscopy/data/segmented' #tiff file directory
output_dir = '/home/krupa/Documents/Research/VirtualEndoscopy/data/volumes'

#outputfile = open(os.path.join(output_dir, '/VisibleKorean_Segmented.raw'), "wb")
outputfile = open("VisibleKorean_Segmented.raw", "wb")

for image_file in sorted(os.listdir(input_dir), reverse= True):
	
    print(image_file)
    img = Image.open(os.path.join(input_dir,image_file)).convert('L') 

    arr = asarray(img)
    arr.flatten('C')
    arr2 = np.array(arr).flatten('C').astype('uint16')
    outputfile.write(arr2)

outputfile.close()
