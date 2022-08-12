import cv2
import random
import numpy as np
import os
import pandas as pd
from collections import defaultdict

IMG_DIR = '/Users/joemattholden/PycharmProjects/cornea/Processed/atropine epithelial'


def get_histogram(image):
    freq = defaultdict(lambda: 0)
    for g in range(image.shape[1]):
        for h in range(image.shape[0]):
            if tuple(image[h, g]) != (0, 0, 0):
                freq[tuple(image[h, g])] += 1
    return list(freq.values())


df = pd.DataFrame()
filenames = []
frq = []

for root, dirs, files in os.walk(IMG_DIR):
    for f in files:
        print(f)
        if f.endswith('.png'):
            frequencies = pd.Series(get_histogram(cv2.imread(IMG_DIR + f'/{f}')))
            filenames.append(f)
            frq.append(frequencies)

new = pd.concat(frq, axis=0)
# new.columns = filenames
new.to_excel('frequencies_atropine epithelial.xlsx')
