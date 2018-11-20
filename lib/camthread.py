import threading

from . import cameraShot as cap


class CameraThread():
	def __init__(self, cam):
		self.isCaptured = False
		self.cam = cam
		self.thread = None

	def start(self):
		print ("Cam Thread Started")
		self.thread = threading.Timer(3, self.capture)
		self.thread.start()

	def capture(self):
		print("Captured")
		cap.capture(self.cam)
		self.isCaptured = True

	def isAlive(self):
		if self.thread:
			return self.thread.isAlive()
