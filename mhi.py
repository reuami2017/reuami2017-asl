import numpy as np
import cv2
import time
import sys
import os.path as osp

import os
pic_path2 = '../picture_files/'
save_path = 'C:/Users/CZ_Capture/PycharmProjects/picture_files/pic_mhi/'
name = ('abraham','becca','kk','shareef','vasu')
sign = ('coffee','king','workout','happy','sad')
number = ('1','2','3','4','5')
for n in name:
    for s in sign:
        for num in number:
            pic_path = pic_path2+n+'_'+s+num
            length = 0
            for dir,subdir,files in os.walk(pic_path):
                print( dir,' ', str(len(files)))
                length = len(files)
            #print(length)
            prev_frame = cv2.resize(cv2.imread(pic_path+'/0.png',0), (0,0), fx=0.5, fy=0.5)
            timestamp = 0;
            h, w = prev_frame.shape[:2]
            length2 = length/1
            motion_history = np.zeros((h, w), np.float32)
            for x in range(1,length,1):
                #print(x)
                str1 = pic_path+'/'+str(x)+'.png'
                img = cv2.imread(str1,0)

                small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
                gray_diff = cv2.absdiff(small,prev_frame)
                ret,fgmask = cv2.threshold(gray_diff,30,1,cv2.THRESH_BINARY)
                timestamp += 1
                cv2.motempl.updateMotionHistory(fgmask, motion_history, timestamp, length2)
                mh = np.uint8(np.clip((motion_history - (timestamp - length2)) / length2, 0, 1) * 255)

                #cv2.imshow('motempl', mh)

                #cv2.waitKey(int(1000/30))
                prev_frame = small
                #time.sleep(5)
            cv2.imwrite(save_path+n+'_'+s+num+'.png',mh)

cv2.waitKey(0)
cv2.destroyAllWindows()
