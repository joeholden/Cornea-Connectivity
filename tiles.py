import cv2
from collections import defaultdict
import numpy as np


def create_tiles(image_path, num_cols, num_rows, write_tiles=True, stitch_tiles=False):
    """creates tiles, saves them in new directory"""
    im = cv2.imread(image_path)

    image_height = im.shape[0]
    image_width = im.shape[1]

    y1 = 0
    height_increment = image_height // num_rows
    width_increment = image_width // num_cols

    for y in range(0, image_height, height_increment):
        for x in range(0, image_width, width_increment):
            y1 = y + height_increment
            x1 = x + width_increment
            tile = im[y:y + height_increment, x:x + width_increment]
            if write_tiles:
                cv2.imwrite("tiles/" + str(x) + '_' + str(y) + ".png", tile)

    # code to stitch tiles together
    # concatenate tiles in a row together and then concatenate those rows vertically.
    # cv2.hconcat([img1, img2]) or cv2.vconcat([img1, img2])

    if stitch_tiles:
        rows = defaultdict(list)
        row_counter = 0
        for y in range(0, image_height, height_increment):
            for x in range(0, image_width, width_increment):
                y1 = y + height_increment
                x1 = x + width_increment
                tile_name = str(x) + '_' + str(y) + ".png"
                try:
                    rows[f'{row_counter}'].append(tile_name)
                except Exception as e:
                    print(e)
                    print(rows)

            rows[f'{row_counter}'].append(cv2.hconcat([cv2.imread(f'tiles/{i}') for i in rows[f'{row_counter}']]))
            row_counter += 1
        rows_to_stack = []
        for r in rows.values():
            rows_to_stack.append(r[-1])
        stitched_image = cv2.vconcat(rows_to_stack)

        cv2.imwrite(f"stitched_images/{image_path.split('/')[-1]}", stitched_image)


def is_identical(image1, image2):
    return image1.shape == image2.shape and not (np.bitwise_xor(image1, image2).any())


p = '/Users/joemattholden/PycharmProjects/cornea/first run/Processed/atropine cmp ' \
    'central/processed_Central_Atropine_CMP_M3_RE_40x.png'

create_tiles(p, num_rows=5, num_cols=4, write_tiles=True, stitch_tiles=True)
