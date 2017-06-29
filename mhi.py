import numpy as np
import cv2
import time
import sys
import os.path as osp

import os
pic_path = '../picture_files/vasu_workout1'
length = 0
for dir,subdir,files in os.walk(pic_path):
    print( dir,' ', str(len(files)))
    length = len(files)
print(length)
prev_frame = cv2.resize(cv2.imread(pic_path+'/0.png',0), (0,0), fx=0.5, fy=0.5)
timestamp = 0;
h, w = prev_frame.shape[:2]

motion_history = np.zeros((h, w), np.float32)
for x in range(1,length):
    print(x)
    str1 = pic_path+'/'+str(x)+'.png'
    img = cv2.imread(str1,0)

    small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    gray_diff = cv2.absdiff(small,prev_frame)
    ret,fgmask = cv2.threshold(gray_diff,95,1,cv2.THRESH_BINARY)
    timestamp += 1
    cv2.motempl.updateMotionHistory(fgmask, motion_history, timestamp, length)
    mh = np.uint8(np.clip((motion_history - (timestamp - length)) / length, 0, 1) * 255)

    cv2.imshow('motempl', mh)

    cv2.waitKey(int(1000/30))

    #time.sleep(5)

cv2.waitKey(0)
cv2.destroyAllWindows()
