import os
import csv
import numpy as np
fieldnames = ['Plane_no','label','path','L1','L2','L3','L1_desc','L2_desc','L3_desc']
with open(r'filenames.csv', 'a') as f:
  writer = csv.writer(f)
  writer.writerow(fieldnames)
src = '/home/krupa/Documents/Research/VirtualEndoscopy/data/01VisibleMale/VM-4'

level1=1
for L1 in sorted(os.listdir(src)):
  print(level1)
  level2=0
  level1_name = L1[4:]
  src1 = os.path.join(src,L1)
  print(src1)
  #src1 = os.path.join(src1,L1)
  
  for L2 in sorted(os.listdir(src1)):
    level2_name = L2[4:]
    
    level3=0
    for L3 in sorted(os.listdir(os.path.join(src1,L2))):
      level3_name = L3[4:]
      
      src2 = os.path.join(src1,L2)
      for images in os.listdir(os.path.join(src2,L3)):
        src3 = os.path.join(src2,L3)
        src3 = os.path.join(src3,images)
        l1 = bin(level1)[2:].zfill(4)
        l2 = bin(level2)[2:].zfill(4)
        l3 = bin(level3)[2:].zfill(7)

        z = '0' + l1 + l2 + l3 #generating the label(1,4,4,7) in 16 bit format4
        z = int(z,2)
        # z = np.ushort(z)
        # images = str(images)
        fields=[images[:4], z, src3, int(l1,2), int(l2,2), int(l3,2), level1_name, level2_name, level3_name]
        with open(r'filenames.csv', 'a') as f:
          writer = csv.writer(f)
          writer.writerow(fields)

      level3 = level3 + 1

    level2 = level2 + 1

  level1 = level1 + 1