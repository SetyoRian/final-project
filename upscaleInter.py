import cv2
from pathlib import Path
import os
import time


def count():
    pathFile = Path(r"E:\PENS\PA\PL-3-Image\PL3-Cropped")
    pathFile2 = Path(r"E:\PENS\PA\PL-3-Image\PL3-Cropped\Upscaled\Dummies")

    number = 1
    totalTime = 0
    for first in range(5):
        for second in range(5):
            # Read image
            path_name = str(pathFile)
            image_name = path_name + '\PL3_1_0' + str(first + 1) + '_0' + str(second + 1) + '.png'
            image = cv2.imread(image_name)
            filename = 'PL3_1_0' + str(first + 1) + '_0' + str(second + 1) + '_' \
                       + str(number) + '_inter' + 'Linear' + '.png'

            # Upscale the image
            scale_percent = 400  # percent of original size
            width = int(image.shape[1] * scale_percent / 100)
            height = int(image.shape[0] * scale_percent / 100)
            dim = (width, height)

            # resize image
            st = time.time()
            result = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)
            et = time.time()
            elapsed_time = et - st
            final_res = elapsed_time * 1000
            totalTime += final_res
            print('Execution time:', final_res, 'miliSeconds')

            cv2.imwrite(os.path.join(pathFile2, filename), result)
            number += 1
            print(filename)

    print('Average Time:', totalTime / number, 'miliSeconds')


def count2():
    pathFile = Path(r"E:\PENS\PA\PL-3-Image\Downscaled")
    pathFile2 = Path(r"E:\PENS\PA\PL-3-Image\Upscaled")

    number = 1
    totalTime = 0
    while number <= 10:
        # Read image
        path_name = str(pathFile)
        image_name = path_name + '\PL3_' + str(number) + '.png'
        filename = 'PL3_' + str(number) + '_inter' + 'Linear' + '.png'

        image = cv2.imread(image_name)

        # Upscale the image
        scale_percent = 400  # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        st = time.time()
        result = cv2.resize(image, dim, interpolation=cv2.INTER_NEAREST)
        et = time.time()
        elapsed_time = et - st
        totalTime += elapsed_time
        print('Execution time:', elapsed_time, 'seconds')

        cv2.imwrite(os.path.join(pathFile2, filename), result)
        print(number)
        number += 1

    print('Average Time:', totalTime / 10, 'seconds')


# count2()
count()
