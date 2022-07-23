import cv2
import random
import numpy as np
import os
import pandas as pd

IMG_DIR = 'CMP TIFFs/pngs'


def process_image(path):
    def generate_rgb():
        r = random.randint(1, 254)
        g = random.randint(1, 254)
        b = random.randint(1, 254)
        # can't make it white or black
        return [r, g, b]

    # count white
    white = 0
    for g in range(im_rgb.shape[1]):
        for h in range(im_rgb.shape[0]):
            if tuple(im_rgb[h, g]) == (255, 255, 255):
                white += 1
    white_area = white / (im_rgb.shape[1] * im_rgb.shape[0])

    def flood(node_1, image_object, valid_path_rgb, fill_color):
        image = image_object
        width = image.shape[1]
        height = image.shape[0]

        def find_neighbors(px):
            x = px[0]
            y = px[1]
            neighbors = [
                (x - 1, y - 1),
                (x, y - 1),
                (x + 1, y - 1),
                (x - 1, y),
                (x + 1, y),
                (x - 1, y + 1),
                (x, y + 1),
                (x + 1, y + 1)
            ]
            neighbors = [(i, j) for (i, j) in neighbors if 0 <= i < width and 0 <= j < height]
            return neighbors

        current_pixel = node_1
        visited_px = [node_1]
        finished = False

        while True:
            nbr = find_neighbors(current_pixel)
            for n in nbr:
                if n not in visited_px and tuple(im_rgb[n[0], n[1]]) == valid_path_rgb:
                    visited_px.append(n)
                    im_rgb[n[0], n[1]] = fill_color
            try:
                current_pixel = visited_px[0]
                visited_px.remove(visited_px[0])
            except Exception as e:
                break

    colors = []
    for g in range(im_rgb.shape[1]):
        for h in range(im_rgb.shape[0]):
            if tuple(im_rgb[h, g]) == (255, 255, 255):
                color = generate_rgb()
                colors.append(color)
                im_rgb[h, g] = color
                flood((h, g), image_object=im_rgb, fill_color=color, valid_path_rgb=(255, 255, 255))



    # cv2.imshow('image', im_rgb)
    cv2.imwrite(f'Processed/processed_{path.split("/")[-1]}', im_rgb)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    return len(colors), white_area


data = []
for root, dirs, files in os.walk(IMG_DIR):
    for f in files:
        im_rgb = cv2.imread(IMG_DIR + f'/{f}')
        frags, w_area = process_image(IMG_DIR + f'/{f}')
        data.append((f, frags, w_area))


data = pd.DataFrame(data)
data.to_excel('fragments.xlsx')