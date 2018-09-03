#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os
import shutil

def detect(img, cascade):
    rects = cascade.detectMultiScale(img,
                                     scaleFactor=1.3,
                                     minNeighbors=4,
                                     minSize=(30, 30),
                                     flags=cv.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    return rects


def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv.rectangle(img, (x1, y1), (x2, y2), color, 2)


if __name__ == '__main__':
    # 표시자 지정
    cascade = cv.CascadeClassifier(
        "haarcascades/haarcascade_frontalface_alt.xml")

    cam = cv.VideoCapture(0)

    # 폴더 리스트 구성
    paths = []
    for root, dirs, files in os.walk('/home/kether/sdcard/tf_face/data') :
        for dir in dirs :
            paths.append(os.path.join(root, dir))

    for path in paths :
        for root, dirs, files in os.walk(path) :
            for file in files :
                full_path = os.path.join(root, file)

                img = cv.imread(full_path)
                if np.any(img) == None:
                    os.remove(full_path)
                    print "파일이 잘못되었습니다. : " + full_path
                else :
                    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                    gray = cv.equalizeHist(gray)

                    # 얼굴 감지, 1명이 아니면 사진 제거
                    rects = detect(gray, cascade)

                    if len(rects) != 1 :
                        os.remove(full_path)
                        print "delete file : " + full_path
                    else :
                        print full_path + " : {0} face detected".format(len(rects))
        for root, dirs, files in os.walk(path) :
            num_files = len(files)
            if num_files < 30 :
                shutil.rmtree(path)
                print path + " has not enough data"
            else :
                print path + " has enough data : " + str(num_files) + " files"
