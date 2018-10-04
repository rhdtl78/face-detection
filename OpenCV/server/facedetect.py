#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv
import cameraShot as cap
import threading
import sendPic
class CameraThread() :
    def __init__(self, cam):
        self.isCaptured = False
        self.cam = cam
    def run(self):
        print ("Captured")
        cap.capture(self.cam)
        self.isCaptured = True



def detect(img, cascade):
    rects = cascade.detectMultiScale(img,
                                     scaleFactor=1.3,
                                     minNeighbors=4,
                                     minSize=(30, 30),
                                     flags=cv.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
    # 표시자 지정
    cascade = cv.CascadeClassifier("haarcascades/haarcascade_frontalface_alt.xml")
    nested = cv.CascadeClassifier("haarcascades/haarcascade_eye.xml")

    cam = cv.VideoCapture(0)

    isCaptured = False

    tread = CameraThread(cam)
    threadCount = 0;
    camThread = threading.Timer(3,tread.run,args=[cam])

    isCaptured = False

    thread = CameraThread(cam)
    threadCount = 0;
    camThread = threading.Timer(3,thread.run)
    while True:
        if(isCaptured == True): break

        ret, img = cam.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray = cv.equalizeHist(gray)

        #얼굴 감지
        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))

        #눈 감지
        if not nested.empty():
             for x1, y1, x2, y2 in rects:
                roi = gray[y1:y2, x1:x2]
                vis_roi = vis[y1:y2, x1:x2]
                subrects = detect(roi.copy(), nested)
                draw_rects(vis_roi, subrects, (255, 0, 0))
                if len(subrects) > 0 :
                    if(camThread.isAlive() == False and thread.isCaptured == False and threadCount < 1):
                        threadCount = threadCount + 1;
                        camThread.start()

        cv.imshow('facedetect', vis)

        if (cv.waitKey(1) & 0xFF == ord('q')) or (thread.isCaptured == True):
            break

   
    with open("image.jpg", "rb") as image :
        sendPic.sendPic(image)
    
    cv.destroyAllWindows()
    cam.release()
