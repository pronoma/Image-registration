import PIL
from PIL import Image
import warnings
import numpy as np
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import os
import csv
import cv2
df = pd.read_csv('errors.csv')
#print(df)
#fieldnames = ['Plane_no','label','path','L1','L2','L3','L1_desc','L2_desc','L3_desc']
#errr_df = pd.DataFrame(columns=fieldnames)
dst = '/home/krupa/Documents/Research/VirtualEndoscopy/data/segmented'
for adress in df['path']:
  image = cv2.imread(adress)
  print('image shape:',image.shape)
  b,g,r = cv2.split(image)
  print('single channelshape:',b.shape)
  print(b==g)
  print(g==r)
  print(adress[-8:])
  base = Image.open(os.path.join(dst,adress[-8:]))
  
  base_image = np.array(base)
  x = np.where(b==0)
  #print(base_image[x[0],x[1]])
  
  #base_image[x[0],x[1]] = df['label'][df['path'] == adress].values[0]
  
  #print(df['label'][df['path'] == adress].values[0])
  #base_image = Image.fromarray(base_image)
  #base_image.save(os.path.join('/home/krupa/Documents/Research/VirtualEndoscopy',adress[-8:]))

      
