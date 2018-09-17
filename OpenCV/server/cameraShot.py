# -*- coding: utf-8 -*-
import cv2

def capture(cam):
    if cam.isOpened() == False:
        print ('cant open the cam (%d)' % camid)
        return None

    ret, frame = cam.read()
    if frame is None:
        print ('frame is not exist')
        return None

    # png로 압축 없이 영상 저장
    cv2.imwrite('image.jpg',frame, params=[cv2.IMWRITE_PNG_COMPRESSION,0])
    
