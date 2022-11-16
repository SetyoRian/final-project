import cv2
from pathlib import Path
import os
import numpy as np
from PIL import Image


def make_image_square(filename):
    img = cv2.imread(filename)
    # Size of the image
    # s = max(img.shape[0:2])
    # s = 640
    #
    # # Creating a dark square with NUMPY
    # f = np.zeros((s,s,3),np.uint8)
    #
    # # Getting the centering position
    # ax,ay = (s - img.shape[1])//2,(s - img.shape[0])//2
    #
    # # Pasting the 'image' in a centering position
    # f[ay:img.shape[0]+ay,ax:ax+img.shape[1]] = img

    f = cv2.resize(img, (640, 640), interpolation=cv2.INTER_AREA)
    cv2.imwrite(filename, f)


# Main codes start here
pathFile = Path(r"E:\PENS\PA\PL-3-Image")
pathFile2 = Path(r"E:\PENS\PA\PL-3-Image\PL3-Cropped")
image_amount = 166
for image_index in range(image_amount):

    path_name = str(pathFile)
    image_name = path_name + '\PL3_' + str(image_index + 1) + '.jpg'
    img = cv2.imread(image_name)

    h, w, c = img.shape

    print(h, w, image_name)

    w_constant = w / 5
    h_constant = h / 5

    image_part_index = 0

    for index_w in range(2):
        for index_h in range(2):
            start_width = int(w_constant * index_w)
            end_width = int(w_constant * (index_w + 1))

            start_height = int(h_constant * index_h)
            end_height = int(h_constant * (index_h + 1))

            current_index = image_part_index

            # For training image set
            section_name = 'PL_3_' + str(image_index + 1) + '_'
            file_name = section_name + str(image_part_index + 1) + '.jpg'

            # For testing image set
            # section_name = str(image_index+1) + '/'
            # file_name = section_name + str(image_part_index+1) + '.jpg'

            crop_img = img[start_height:end_height, start_width:end_width]

            image_part_index = image_part_index + 1
            # cv2.imwrite(file_name, crop_img)
            cv2.imwrite(os.path.join(pathFile2, file_name), crop_img)

            # make_image_square(file_name)
