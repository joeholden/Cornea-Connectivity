import cv2
import numpy as np
from tiles_module import create_tiles
import os


PARENT_DIR_PATH = '/Volumes/Calkins_Lab/User Folders/Joe Holden/Imaging/Confocal Images/' \
                  'LW cornea images atroping cmp/Multi Page Tifs'
assert os.path.exists(PARENT_DIR_PATH)

for root, dirs, files in os.walk(PARENT_DIR_PATH, topdown=False):
    for file in files:
        path_to_multi_page_tif = PARENT_DIR_PATH + f'/{file}'
        print(file)
        ret, images = cv2.imreadmulti(PARENT_DIR_PATH + f'/{file}', [], cv2.IMREAD_UNCHANGED)
        num_pages = np.shape(images)[0]
        image_name = path_to_multi_page_tif.split('/')[-1].split('.')[0]
        if not os.path.exists(f'test pages/{file.split(".")[0]}'):
            os.makedirs(f'test pages/{file.split(".")[0]}')

        for page in range(num_pages):
            print(page)
            z_pos_path = f'test pages/{file.split(".")[0]}/page_{page}.png'
            cv2.imwrite(z_pos_path, images[page])
            create_tiles(image_name=image_name, image_path=z_pos_path, stack_pos=page, path_to_tiles_to_stitch=None,
                         num_rows=3, num_cols=3, write_tiles=True, stitch_tiles=False)





