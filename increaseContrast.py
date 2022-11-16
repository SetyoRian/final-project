import cv2
import time

# Contrast
# In the GIMP, contrast levels go from -127 to +127. I adapted the formulas from https://www.dfstudios.co.uk/articles/programming/image-programming-algorithms/image-processing-algorithms-part-5-contrast-adjustment/ to fit in that range.
# To figure out brightness, I figured out the relationship between brightness and levels and used information in this levels post to arrive at a solution.
#
# #pseudo code
# if brightness > 0
#     shadow = brightness
#     highlight = 255
# else:
#     shadow = 0
#     highlight = 255 + brightness
# new_img = ((highlight - shadow)/255)*old_img + shadow

# cara stackoverflow
def apply_brightness_contrast(input_img, brightness=0, contrast=0):
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf

# start = time.perf_counter()
#
# img = cv2.imread('PL_5_1_0.jpg')
# imgCara1 = img.copy()
# imgCara2 = img.copy()
#
# #  cara 1
# w, h, ch = img.shape
# for width in range(w):
#     for height in range(h):
#         for channel in range(ch):
#             imgCara1[width][height][channel] = img[width][height][channel] + (img[width][height][channel] * 0.3)
#             if(imgCara1[width][height][channel] > 255):
#                 imgCara1[width][height][channel] = 255
#
# stop = time.perf_counter()

# contrast = 0.3
# imgCara2 = cv2.addWeighted(imgCara2, 1, imgCara2, contrast, 0)

# stop2 = time.perf_counter()
# print(f'The first way is Finisihed in {round(stop-start, 2)} seconds')
# print(f'The second way is Finisihed in {round(stop2-stop, 2)} seconds')

image_amount = 10
start = 1
contrast = 0.3
for image_index in range(image_amount):
    image_name = 'ready_train/PL_8_' + str(start + image_index)
    image_part_index = 0
    for index_w in range(2):
        for index_h in range(2):
            img_name_full = image_name + '_' + str(image_part_index + 1) + '.jpg'
            img = cv2.imread(img_name_full)
            print(img_name_full)
            current_index = image_part_index

            # For training image set
            section_name = 'ready_train/30%_contrast/PL_8_' + str(start + image_index) + '_'
            file_name = section_name + str(image_part_index+1) + '.jpg'

            afterContrast = cv2.addWeighted(img, 1, img, contrast, 0)
            cv2.imwrite(file_name, afterContrast)
            print(file_name)
            image_part_index = image_part_index + 1

    image_index += 1
    print(f'Image {image_index} done !!')

cv2.destroyAllWindows()