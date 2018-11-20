# -*- coding: utf-8 -*-
import cv2


def capture(cam, camid=0):

	if not cam.isOpened():
		print('cant open the cam (%d)' % camid)
		return None

	_, frame = cam.read()
	if frame is None:
		print('frame is not exist')
		return None

	print ("Shot!!")
	cv2.imwrite('image.jpg', frame, params=[cv2.IMWRITE_PNG_COMPRESSION, 0])
