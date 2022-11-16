from pathlib import Path
from math import log10, sqrt
import cv2
import numpy as np
import os


def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr


def valPSNR():
    pathFile = Path(r"E:\PENS\PA\PL-3-Image\PL3-Cropped")
    pathFile2 = Path(r"E:\PENS\PA\PL-3-Image\PL3-Cropped\Upscaled\Dummies")

    number = 1
    total = 0
    for first in range(5):
        for second in range(5):
            # Read image
            path_name = str(pathFile)
            path_name2 = str(pathFile2)
            image_name = path_name + '\PL3_1' + '_0' + str(first + 1) + '_0' + str(second + 1) + '.png'
            image_name2 = path_name2 + '\PL3_1_0' + str(first + 1) + '_0' + str(second + 1) + '_' \
                          + str(number) + '_interArea' + '.png'
            image = cv2.imread(image_name)
            image2 = cv2.imread(image_name2, 1)
            value = PSNR(image, image2)
            print(f"PSNR value is {value} dB")
            number += 1
            total += value

    print('Average:', total / 25)


def valPSNR2():
    pathFile = Path(r"E:\PENS\PA\PL-3-Image")
    pathFile2 = Path(r"E:\PENS\PA\PL-3-Image\Upscaled")

    number = 0
    total = 0
    while number < 10:
        path_name = str(pathFile)
        path_name2 = str(pathFile2)
        image_name = path_name + '\PL3_' + str(number + 1) + '.jpg'
        image_name2 = path_name2 + '\PL3_' + str(number + 1) + '_' + 'LapSRN' + '.png'
        image = cv2.imread(image_name)
        image2 = cv2.imread(image_name2)
        value = PSNR(image, image2)
        print(f"PSNR value is {value} dB")
        number += 1
        total += value
    print('Average:', total / 10)

valPSNR2()