import PIL
from PIL import Image
import numpy as np
import pandas as pd
import os
import csv
df = pd.read_csv('filenames.csv')
fieldnames = ['Plane_no','label','path','L1','L2','L3','L1_desc','L2_desc','L3_desc']
error_df = pd.DataFrame(columns=fieldnames)
dst = '/home/krupa/Documents/Research/VirtualEndoscopy/data/segmented'
for i in range(1905,8506,5):
  images = "{:04d}".format(i) + '.tif'
  base_image = np.zeros((1407,2468),dtype = 'ushort')
  selected_df = df.loc[df['Plane_no'] == "{:04d}".format(i)]
  for adress in selected_df['path']:
    try:
      image = Image.open(adress)
      image = np.array(image)
      x = np.where(image == 0)
    #base_image[x[0],x[1]] = np.ushort(df['label'][df['path'] == adress].values[0])
      base_image[x[0],x[1]] = df['label'][df['path'] == adress].values[0]
    except:
      error_df = error_df.append(df[df['path']==adress],ignore_index =True)
      print(error_df)

    
  base_image = Image.fromarray(base_image)
  base_image.save(os.path.join(dst,images))
error_df.to_csv('errors.csv')