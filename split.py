import image_slicer
from pathlib import Path

pathFile = Path(r"E:\PENS\PA\PL-3-Image")
pathFile2 = Path(r"E:\PENS\PA\PL-3-Image\PL3-Cropped")

image_amount = 166
index = 1

while index < image_amount:
    path_name = str(pathFile)
    image_name = path_name + '\PL3_' + str(index) + '.jpg'
    # img = cv2.imread(image_name)
    tiles = image_slicer.slice(image_name, 25, save=False)
    image_slicer.save_tiles(tiles, directory=pathFile2, prefix='PL3_' + str(index))
    index += 1
    print(image_name)
