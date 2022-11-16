from pathlib import Path


def Test():
    pathFile = Path(r"E:\PENS\PA\PL-3-Image\PL3-Cropped\Upscaled\Selected2")

    index = 1
    amount = 165
    firstIndex = 5
    secondIndex = 5
    number = 1
    while index <= amount:
        for first in range(firstIndex):
            for second in range(secondIndex):
                # Read file
                path_name = str(pathFile)
                file_name = path_name + '\PL3_' + str(index) + '_0' + str(first + 1) + '_0' + str(second + 1) + '_' + str(number) +'.txt'
                print(file_name)
                f = open(file_name, "r")
                number += 1
                print(f.read())
        number = 1
        index += 1


# Test()