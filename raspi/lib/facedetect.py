#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import cv2 as cv

from . import settings

faceClassifier = os.path.join(
    settings.BASE_DIR, "lib", "haarcascades", "haarcascade_frontalface_alt.xml")
eyeClassifier = os.path.join(settings.BASE_DIR, "lib", "haarcascades",
                             "haarcascade_eye.xml")

faces = cv.CascadeClassifier(faceClassifier)
eyes = cv.CascadeClassifier(eyeClassifier)
if faces.empty():
    print ("Error: xml not found {}".format(faceClassifier))
if eyes.empty():
    print ("Error: xml not found {}".format(eyeClassifier))

def detect(img, cascade):
    rects = cascade.detectMultiScale(img,
                                     scaleFactor=1.3,
                                     minNeighbors=4,
                                     minSize=(30, 30),
                                     flags=cv.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:, 2:] += rects[:, :2]
    return rects


def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv.rectangle(img, (x1, y1), (x2, y2), color, 2)
