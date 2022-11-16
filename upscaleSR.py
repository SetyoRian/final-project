import cv2
from cv2 import dnn_superres
from pathlib import Path
import os
import time


def SR():
    pathFile = Path(r"E:\PENS\PA\PL-3-Image\PL3-Cropped")
    pathFile2 = Path(r"E:\PENS\PA\PL-3-Image\PL3-Cropped\Upscaled\Dummies")

    # Create an SR object
    sr = dnn_superres.DnnSuperResImpl_create()

    # Read the desired model
    path = "ESPCN_x4.pb"
    sr.readModel(path)

    # Set the desired model and scale to get correct pre- and post-processing
    sr.setModel("espcn", 4)

    # sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    # sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    index = 1
    amount = 1
    firstIndex = 5
    secondIndex = 5
    number = 1
    totalTime = 0
    while index <= amount:
        for first in range(firstIndex):
            for second in range(secondIndex):
                # Read image
                path_name = str(pathFile)
                image_name = path_name + '\PL3_' + str(index) + '_0' + str(first + 1) + '_0' + str(second + 1) + '.png'
                image = cv2.imread(image_name)
                filename = 'PL3_' + str(index) + '_0' + str(first + 1) + '_0' + str(second + 1) + '_' \
                           + str(number) + '_ESPCN.png '

                # Upscale the image
                st = time.time()
                result = sr.upsample(image)
                et = time.time()
                elapsed_time = et - st
                totalTime += elapsed_time
                print('Execution time:', elapsed_time, 'seconds')
                # cv2.imwrite("upscaled.png", result)
                cv2.imwrite(os.path.join(pathFile2, filename), result)
                number += 1
                print(filename)
        number = 1
        index += 1

    print('Average Time:', totalTime / 25, 'Seconds')


def SR2():
    pathFile = Path(r"E:\PENS\PA\PL-3-Image\Downscaled")
    pathFile2 = Path(r"E:\PENS\PA\PL-3-Image\Upscaled")

    # Create an SR object
    sr = dnn_superres.DnnSuperResImpl_create()

    # Read the desired model
    path = "LapSRN_x4.pb"
    sr.readModel(path)

    # Set the desired model and scale to get correct pre- and post-processing
    sr.setModel("lapsrn", 4)
    number = 1
    totalTime = 0
    while number <= 10:
        path_name = str(pathFile)

        image_name = path_name + '\PL3_' + str(number) + '.png'
        filename = 'PL3_' + str(number) + '_' + 'LapSRN' + '.png'

        image = cv2.imread(image_name)

        # Upscale the image
        st = time.time()
        result = sr.upsample(image)
        et = time.time()
        elapsed_time = et - st
        totalTime += elapsed_time
        print('Execution time:', elapsed_time, 'seconds')

        cv2.imwrite(os.path.join(pathFile2, filename), result)
        print(filename, number)

        number += 1

    print('Average Time:', totalTime / 10, 'Seconds')


# SR2()
SR()
