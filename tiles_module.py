import cv2
from collections import defaultdict
import numpy as np
import os


def create_tiles(image_name, image_path, stack_pos, num_cols, num_rows, write_tiles=True, stitch_tiles=False, path_to_tiles_to_stitch=None):
    """creates tiles, saves them in new directory"""
    im = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    grid_image = cv2.imread(image_path)
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
            cv2.rectangle(grid_image, (x, y), (x1, y1), (255, 255, 255))
            # cv2.putText(grid_image, text=f'({x1}, {y1})', org=(x1, y1+20), color=(255, 255, 255),
            #             fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5)
            if write_tiles:
                if not os.path.exists(f"tiles/{image_name}/{str(x)}_{str(y)}"):
                    os.makedirs(f"tiles/{image_name}/{str(x)}_{str(y)}")
                cv2.imwrite(f"tiles/{image_name}/{str(x)}_{str(y)}/{stack_pos}.png", tile)
    cv2.imwrite(f'grids/grid_copy_{stack_pos}.png', grid_image)
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

            rows[f'{row_counter}'].append(cv2.hconcat([cv2.imread(f'tiles/{i}') for i in rows[f'{row_counter}']]))
            row_counter += 1
        rows_to_stack = []

        for r in rows.values():
            rows_to_stack.append(r[-1])
        stitched_image = cv2.vconcat(rows_to_stack)

        cv2.imwrite(f"stitched_images/{image_path.split('/')[-1]}", stitched_image)


def is_identical(image1, image2):
    return image1.shape == image2.shape and not (np.bitwise_xor(image1, image2).any())



