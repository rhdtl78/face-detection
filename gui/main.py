# -*- coding: utf-8 -*-

from tkinter import *

import PIL
import cv2
from PIL import Image, ImageTk

from lib import facedetect as fd
from lib.camthread import CameraThread
from lib.sendPic import sendPic

class MainFrame:
	def __init__(self, cam=None):
		if cam is None:
			cam = cv2.VideoCapture(0)

		width, height = 800, 600
		self.cap = cam
		self.window = Tk()
		self.result = Frame(self.window)

		self.camera = Label(self.window, text="Camera")
		self.resultLabel = Label(self.result, text="결과창", width=20)

		self.result.grid(row=0, column=1)
		self.camera.grid(row=0, column=0)

		self.resultLabel.grid(row=0)

		self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
		self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

		self.window.bind('<Escape>', lambda e: self.end())
		self.started = False
		self.isCaptured = False
		self.thread = CameraThread(self.cap)
		self.threadCount = 0
		self.state = "init"

	def show_frame(self, snapshot=None):

		if self.isCaptured:
			return

		_, img = self.cap.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		gray = cv2.equalizeHist(gray)

		# 얼굴 감지
		rects = fd.detect(gray, fd.faces)
		vis = img.copy()
		fd.draw_rects(vis, rects, (0, 255, 0))

		# 눈 감지
		for x1, y1, x2, y2 in rects:
			roi = gray[y1:y2, x1:x2]
			vis_roi = vis[y1:y2, x1:x2]
			subrects = fd.detect(roi.copy(), fd.eyes)
			fd.draw_rects(vis_roi, subrects, (255, 0, 0))
			if len(subrects) > 0:
				if not self.thread.isAlive() and not self.thread.isCaptured and self.threadCount < 1:
					self.threadCount = self.threadCount + 1
					self.resultLabel.configure(text="촬영중")
					self.thread.start()

		b, g, r = cv2.split(vis)
		rgbimg = cv2.merge([r,g,b])
		imgPIL = PIL.Image.fromarray(rgbimg)
		imgtk = ImageTk.PhotoImage(image=imgPIL)
		self.camera.imgtk = imgtk
		self.camera.configure(image=imgtk)
		self.camera.after(10, self.show_frame)

		if self.thread.isCaptured:
			self.resultLabel.configure(text="촬영됨")
		# 	ret = 'none'
		# 	ret = self.state is "init" and sendPic() or ret
		# 	if self.state is "pending":
		# 		if ret:
		# 			print (ret)
		# 			self.state = "done"
		# 	elif self.state is "done":
		# 		self.resultLabel.configure(text=ret)

	def start(self):
		if self.started == False:
			self.window.mainloop()

	def end(self):
		self.cap.release()
		self.window.quit()
