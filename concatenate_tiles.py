import cv2
import os
from collections import defaultdict
import numpy as np
# add this as own function for re-stitching

dir = '/Users/joemattholden/Desktop/finished/laurens/Atropine_M3_LE_40x Processed Binary Files/'
row_images = defaultdict(list)
for root, dirs, files in os.walk(dir, topdown=False):
    files.sort()
    for f in files:
        if f.endswith('.png') or f.endswith('.tif'):
            row = f.split('_')[-1].split('.')[0]
            row_images[row].append(f)

print(row_images)
h_images = []
for entry in row_images.values():
    entry.sort()
    h_images.append(cv2.hconcat([cv2.imread(dir + i) for i in entry]))


for k in h_images:
    print(np.shape(k))
reconstruct = cv2.vconcat(h_images)

cv2.imshow('image', reconstruct)
cv2.imwrite(dir+'processed_stdev.png', reconstruct)
