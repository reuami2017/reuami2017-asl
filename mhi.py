import numpy as np
import cv2
import time
import sys
import os.path as osp

import os
pic_path = '../picture_files/abraham_coffee3'
length = 0
for dir,subdir,files in os.walk(pic_path):
    print( dir,' ', str(len(files)))
    length = len(files)
print(length)
prev_frame = cv2.resize(cv2.imread(pic_path+'/0.png',0), (0,0), fx=0.5, fy=0.5)

for x in range(1,length,5):
    print(x)
    str1 = pic_path+'/'+str(x)+'.png'
    img = cv2.imread(str1,0)

    small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

    cv2.imshow('image',small)
    cv2.waitKey(500)

    #time.sleep(5)

cv2.waitKey(0)
cv2.destroyAllWindows()
