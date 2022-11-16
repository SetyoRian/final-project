import cv2
from pathlib import Path
import os

pathFile = Path(r"E:\PENS\PA\PL-3-Image\PL3-Cropped\Upscaled\Selected2")

number = 0
total = 0

while number < 10:
    path_name = str(pathFile)

    image_name = path_name + '\PL3_' + str(number+1) + '.jpg'

    image = cv2.imread(image_name)
    res = cv2.resize(image, dsize=(225, 225), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(os.path.join(pathFile2, image_name2), res)
    number += 1
    print(image_name2)