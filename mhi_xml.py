import numpy as np
import cv2
import time
import sys
import os.path as osp

import os
pic_path = 'C:/Users/CZ_Capture/PycharmProjects/picture_files/xml_video/abraham_coffee1.mp4'
save_path = 'C:/Users/CZ_Capture/PycharmProjects/picture_files/xml_mhi/'
length = 0
length2 = 50
video = cv2.VideoCapture(pic_path)
no_frame = video.get(cv2.CAP_PROP_POS_FRAMES)
ret, frame = video.read()
gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
timestamp = 0;
h, w = gray1.shape[:2]

motion_history = np.zeros((h, w), np.float32)
#fps    = video.get(cv2.cv.CV_CAP_PROP_FPS)
#print(fps)
while(video.isOpened()):
    ret, frame = video.read()
    if not ret:
        break
    no_frame = video.get(cv2.CAP_PROP_POS_FRAMES)

    print(no_frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #prev_frame = cv2.resize(gray, (0, 0), fx=0.5, fy=0.5)
    gray_diff = cv2.absdiff(gray,gray1)
    ret,fgmask = cv2.threshold(gray_diff,15,1,cv2.THRESH_BINARY)
    timestamp += 1
    cv2.motempl.updateMotionHistory(fgmask, motion_history, timestamp, length2)
    gray1 = gray
    cv2.imshow('frame',gray)
    mh = np.uint8(np.clip((motion_history - (timestamp - length2)) / length2, 0, 1) * 255)

    cv2.imshow('motempl', mh)

    cv2.waitKey(int(1000/30))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.imwrite(save_path+'abraham_coffee1.png',mh)
video.release()
cv2.waitKey(0)

cv2.destroyAllWindows()
