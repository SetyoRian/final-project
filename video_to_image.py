import cv2
import os

cap = cv2.VideoCapture(r"E:\PENS\PA\Dataset-2022-Alfany\PL-3-200-1.mp4")

# FRAMES PER SECOND FOR VIDEO
# fps = 33

index = 114
delay = 0

if not cap.isOpened():
    print("Error opening the video file. Please double check your file path for typos. Or move the movie file to the "
          "same location as this script/notebook")

# While the video is opened
path = 'E:/PENS/PA/PL-3-100-Image'
while cap.isOpened():
    # Read the video file.
    ret, frame = cap.read()
    # If we got frames show them.
    if ret:
        # time.sleep(1/fps)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('s') or delay == 20:
            filename = 'PL3_' + str(index) + '.jpg'
            frame = frame[64:964, 507:1407, :]
            print(frame.shape, index)
            # cv2.imwrite(filename, frame)
            cv2.imwrite(os.path.join(path, filename), frame)
            delay = 0
            index = index + 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        delay += 1
    # Or automatically break this whole loop if the video is over.
    else:
        break

cap.release()
cv2.destroyAllWindows()
